#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while [ "$(pg_isready -h $SQL_HOST -p $SQL_PORT)" != "$SQL_HOST:$SQL_PORT - accepting connections" ]; do
      sleep 1
    done

    echo "PostgreSQL started"
fi

#python manage.py flush --no-input
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py createsuperuser --email="$DJANGO_SUPER_USER_EMAIL" --birth_year="1990" --no-input
django-admin compilemessages --ignore=env

exec "$@"

# To make migrations in continuous development, RUN:
# docker compose exec app_sip python manage.py makemigrations
# docker compose exec app_sip python manage.py migrate
