<h1>Cursos de Platzi</h1>
<p>
    <a href="{% url "courses:new" %}">Agregar curso</a>
</p>
<ul>
    {% for course in object_list %}
        <li>
            <p>{{ course.name }}</p>
            <p>
                <a href="{% url "courses:detail" course.id %}">Ver</a> | 
                <a href="{% url "courses:edit" course.id %}">Editar</a> | 
                <a href="{% url "courses:delete" course.id %}">Borrar</a> 
            </p>
        </li>
    {% endfor %}
</ul>
