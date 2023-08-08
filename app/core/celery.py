from celery import Celery
from settings import settings


celery = Celery("tasks", broker=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}")


"""
RUN CELERY APP: celery -A core.celery:celery worker --loglevel=INFO
RUN FLOWER: celery -A core.celery flower (to localhost:5555)
"""
