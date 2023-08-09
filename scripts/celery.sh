#! /bin/bash

src app

if [[ "${1}" == "celery" ]]; then
  echo "Starting Celery worker..."
  celery --app=core.celery:celery worker -l INFO

elif [[ "${1}" == "flower" ]]; then
  echo "Starting Flower..."
  celery --app=core.celery:celery flower

fi
