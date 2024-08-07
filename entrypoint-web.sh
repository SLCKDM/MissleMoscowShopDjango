#!/bin/sh

echo "Flush the manage.py command it any"

while ! python manage.py flush --no-input 2>&1; do
  echo "Flusing django manage command"
  sleep 3
done

echo "Migrate the Database at startup of project"

# Wait for few minute and run db migraiton
while ! python manage.py migrate  2>&1; do
  echo "Migration is in progress status"
  sleep 3
done
# python ./backend/manage.py loaddata ./backend/recipes/TasksAPp/initial_data.json
# FOR DEBUG
echo "Django is fully configured successfully and running."
# y | python manage.py migrate && python3 manage.py createsuperuser --no-input && python3 manage.py collectstatic
gunicorn MissleMoscowShopBackend.wsgi:application --bind 0.0.0.0:8000
# python manage.py runserver 0.0.0.0:8000