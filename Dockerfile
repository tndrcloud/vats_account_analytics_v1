FROM python:3.11-slim-buster as build

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/source \
    LANG=ru_RU.UTF-8 \
    LANGUAGE=ru_RU.UTF-8 

WORKDIR /source

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /source/wheels -r requirements.txt


FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/vats_account_analytics_v1 \
    LANG=ru_RU.UTF-8 \
    LANGUAGE=ru_RU.UTF-8 

WORKDIR /vats_account_analytics_v1

COPY --from=build /source/wheels /wheels
RUN pip install --no-cache /wheels/* 

COPY alembic ./alembic
COPY app ./app
COPY .env alembic.ini config.py pyproject.toml ./

CMD ["python", "app/main.py"]
