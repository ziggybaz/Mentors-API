#!/bin/sh

set -eu

echo "[Checking database connection]"

i=0
until [ $i -ge 25 ]
do
  nc -z mentors-db 5432 && break

  i=$(( i + 1 ))

  echo "$i: Waiting for database to start after $i second(s)..."
  sleep $i
done



if [ $i -eq 25 ]
then
  echo "Database connection refused, terminating ..."
  exit 1
fi

echo "Database is up ..."

export FLASK_APP=manage.py &&  python manage.py create_db && python manage.py run -h 0.0.0.0



