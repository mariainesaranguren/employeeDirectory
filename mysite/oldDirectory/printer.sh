#!/bin/sh
IFS=","
while read f1 f2 f3
do
  # echo "Names:"
  # echo $(cut -d "," -f1 Employee.csv)
  #
  # echo
  # echo "Team:"
  # echo $(cut -f2 Employee.csv)
  echo "Name is: $f1, team is: $f2"

  #Put something here so that each entry is added to database
  #Ex DASDASDA($f1, $f2, ...).save()

done < Employee.csv
