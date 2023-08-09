#! /bin/bash

export $(cat .env | xargs)

cd ../
alembic upgrade head
cd app
gunicorn main:app --workers ${WORKERS} --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:${APP_PORT}
