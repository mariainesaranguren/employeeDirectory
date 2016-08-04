import shutil
import os
import yaml
import re
from fabric.api import env, local, run
from fabric.colors import red, green
from fabric.context_managers import prefix

##############################
# configuration
##############################


env.development = {
    'url': 'https://development-dot-wizeline-employee-directory.appspot.com',
    'branch': 'development'
}

env.packages_dir = 'lib/python2.7/site-packages'
env.gae_port = '8085'
env.gae_admin_port = '8005'
env.remote_shell_script = 'remote_api_shell.py'

uname = local('uname -a', shell='/bin/bash', capture=True)

# TODO: look for another way to identify the deploy server
if 'Debian' in uname:
    env.packages_dir = "%s/%s" % (env.remote_virtualenv_path, env.packages_dir,)

APPLICATION_ID = 'wizeline-employee-directory'
CONFIGS = ['app.yaml']
EXTRA_FILES = ['appengine_config.py']

# used on both app source and site-packages
IGNORE = (
    '*.c',
    '*.pyc',
    '*.pyo',
    'tests',
    'testsuite',
    'numpy',
    'virtualenv',
    'flake8'
)

# only used while copying from site-packages
IGNORE_PACKAGES = (
    'mapreduce',
)

BUILD_DIR = 'dist'
APP_DIR = '.'
DEPLOY_DIR = 'deploy'

##############################
# commands
##############################


def clean():
    """
    Removes the build folder and the APP_DIR softlinks
    """
    shutil.rmtree(BUILD_DIR, ignore_errors=True)


def build(environment, version=None):
    """
    Setups a build folder ready to upload to app engine.
    """
    env.environment = environment

    env.app_version = env.environment

    # make sure the correct environment vars are set
    env.environment_file = "environment-%s.sh" % (env.environment,)
    if not os.path.isfile(env.environment_file):
        print(red("Could not find the environments variables file: %s" % (env.environment_file)))
        raise SystemExit()

    with prefix("source %s" % (env.environment_file,)):
        clean()
        copy_libraries()
        copy_app()
        copy_configs(destination=BUILD_DIR)
        copy_extra_files(destination=BUILD_DIR)


def local_deploy(environment, version=None):
    env.environment = environment
    if version:
        git_tag(version)
    build(environment, version)
    local('pip install -r requirements.txt', shell='/bin/bash')
    local("appcfg.py update %s" % (BUILD_DIR,), shell='/bin/bash')


def remote_shell(environment):
    namespace_file = 'appengine_config.py'
    version = 'theversiondoesntmatters' if environment == 'production' else None
    host = 'localhost:%s' % env.gae_port if environment == 'local' else 'wizeline-product-tracker.appspot.com'

    if environment == 'local':
        response = local("ps aux | grep %s" % (env.gae_port,), capture=True)

        # if only the grep returns from ps aux, it will return 2 lines.
        if len(response.splitlines()) < 3:
            print(red("Your local server needs to be running to use the shell."))
            return
    else:
        build(environment, version)

    local("cp scripts/%s %s/" % (env.remote_shell_script, BUILD_DIR,))
    local("sed -i .bkp \"s/return current_app.config.get('APP_ENVIRONMENT')/return '%s'/g\" %s/%s" % (environment, BUILD_DIR, namespace_file,))
    local("cd %s && %s -s %s" % (BUILD_DIR, env.remote_shell_script, host,))


def git_tag(version):
    tag = version.replace('-', '.')
    local('git fetch --tags', shell='/bin/bash')
    local('git tag %s' % tag, shell='/bin/bash')
    local('git push --tags', shell='/bin/bash')


def help():
    print("environments:")
    print("    development")
    print("")
    print("command:")
    print("    clean")
    print("    build:<environment>")
    print("    deploy:<environment>")


##############################
# helpers
##############################


def copy_libraries():
    ignored = IGNORE + IGNORE_PACKAGES
    patterns = shutil.ignore_patterns(*ignored)
    shutil.copytree(env.packages_dir, BUILD_DIR, ignore=patterns)


def copy_app():
    app_ignore = IGNORE + ('bin', 'include', 'lib', 'scripts')

    patterns = shutil.ignore_patterns(*app_ignore)
    hard_copytree(APP_DIR, BUILD_DIR, ignore=patterns)


def copy_configs(destination=None):
    """
    Copies all configs, such as `app.yaml`, to the indicated folder. All files are expected to be yamls

    Merges configurations depending on the environment.
    """
    if not env.environment or not destination:
        raise SystemExit()

    for config in CONFIGS:
        config_file = "%s/%s" % (DEPLOY_DIR, config,)
        env_config_file = "%s/%s/%s" % (DEPLOY_DIR, env.environment, config,)
        output_file = "%s/%s" % (destination, config)

        if os.path.isfile(config_file):
            config = yaml.load(open(config_file, 'r'))
            if os.path.isfile(env_config_file):
                env_config = yaml.load(open(env_config_file, 'r'))
                config = merge(env_config, config)

            with open(output_file, 'w') as outfile:
                outfile.write(yaml.dump(config, default_flow_style=False))

            replace_env_vars(output_file)

            if env.environment == 'production':
                replace_version(output_file, env.app_version)

def copy_extra_files(destination=None):
    """
    Copy any kind of file from the deploy folder to the destination.
    """
    if not env.environment or not destination:
        raise SystemExit()

    for file in EXTRA_FILES:
        file = "%s/%s" % (DEPLOY_DIR, file,)
        if os.path.isfile(file):
            shutil.copy2(file, destination)


def remove_configs(destination=None):
    if not destination:
        raise SystemExit()

    for config in CONFIGS:
        config_file = "%s/%s" % (destination, config)
        if os.path.isfile(config_file):
            os.remove(config_file)


def hard_copytree(src, dst, symlinks=False, ignore=None):
    """
    Allows to copy into an existing directory. Which shutil's copytree doesn't allow.
    """
    ignored_files = ['.DS_Store', '.Python', 'include', 'lib', 'bin', 'scripts']
    for item in os.listdir(src):
        if item in ignored_files:
            continue
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


def merge(a, b):
    """
    Merges a into b, leaving b as a default
    """
    if isinstance(a, dict) and isinstance(b, dict):
        for k, v in b.iteritems():
            if k not in a:
                a[k] = v
            else:
                a[k] = merge(a[k], v)
    return a


def replace_env_vars(filename):
    """
    Replaces any string in the the given filename sorrounded with double underscore
    with the environment variable of the same name

    i.e: given `test=one`, the string `__test__` in the given filename will be replaced with `one`.
    """
    with open(filename, 'r') as sources:
        lines = sources.readlines()

    with open(filename, 'w') as sources:
        for line in lines:
            match = re.search('.*(__(.+)__).*', line)
            if match:
                env_var = local("echo $%s" % match.group(2), capture=True, shell='/bin/bash')
                if env_var:
                    sources.write(re.sub(match.group(1), env_var, line))
            else:
                sources.write(line)


def replace_version(filename, version):
    """
    Replaces the application version on the app.yaml if necessary.
    """
    with open(filename, 'r') as sources:
        lines = sources.readlines()

    with open(filename, 'w') as sources:
        for line in lines:
            sources.write(re.sub('--APP_VERSION--', version, line))


def create_softlinks():
    """
    Creates softlinks for the python libraries (site-packages on the virtualenv)
    on the APP_DIR so we are able to run dev_appserver.py
    """
    remove_softlinks()
    local("cd %s && ln -sf ../%s/* ." % (APP_DIR, env.packages_dir,), shell='/bin/bash')


def remove_softlinks():
    """
    Removes softlinks from the APP_DIR
    """
    local("find %s -maxdepth 1 -type l -exec rm {} \;" % (APP_DIR,), shell='/bin/bash')
