###########
# BUILDER #
###########

# pull official base image
FROM python:3.9.1-slim as builder

# set environment variables
ARG REPO_PATH
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV VIRTUAL_ENV=/opt/venv

RUN apt-get update
# Install i18n requirements
RUN apt-get install gettext -y
# Install Postgres requirements
RUN apt-get install libpq-dev python3-dev -y
RUN apt-get install build-essential -y
# Install Postgres alive checker (pg_isready)
RUN apt install -y postgresql-client

# pip requirements
RUN pip install --upgrade pip
RUN pip install virtualenv && python -m virtualenv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ADD $REPO_PATH/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /tmp/wheels -r /tmp/requirements.txt


#########
# FINAL #
#########

# pull official base image
FROM python:3.9.1-slim

# create the app_user user
RUN addgroup app_user && useradd app_user -g app_user

RUN apt-get update
# Install i18n requirements
RUN apt-get install gettext -y
# install dependencies
RUN apt-get install libpq-dev python3-dev -y
RUN apt-get install build-essential -y
# Install Postgres alive checker (pg_isready)
RUN apt install -y postgresql-client

COPY --from=builder /tmp/wheels /wheels
COPY --from=builder /tmp/requirements.txt .
RUN pip install --no-cache /wheels/*

# copy entrypoint.prod.sh
COPY entrypoint.prod.sh /srv/entrypoint.prod.sh
RUN sed -i 's/\r$//g' /srv/entrypoint.prod.sh
RUN chmod +x /srv/entrypoint.prod.sh

COPY $REPO_PATH /srv/app_sip
# set work directory
WORKDIR /srv/app_sip

# chown all the files to the app_user user
RUN chown -R app_user:app_user /srv/app_sip

# change to the app_user user
USER app_user

ENTRYPOINT ["/srv/entrypoint.prod.sh"]
