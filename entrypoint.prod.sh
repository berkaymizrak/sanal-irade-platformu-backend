#!/bin/sh

if [ "$DATABASE" = "postgres" ]; then
  echo "Waiting for postgres..."

  while [ "$(pg_isready -h $SQL_HOST -p $SQL_PORT)" != "$SQL_HOST:$SQL_PORT - accepting connections" ]; do
    sleep 1
  done

  echo "PostgreSQL started"
fi

#if [ "$RUNNER" = "app" ]; then
#  django-admin compilemessages --ignore=env
#fi

exec "$@"
