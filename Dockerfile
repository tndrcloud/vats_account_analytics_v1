FROM python:3.11-slim

RUN mkdir ./vats_account_analytics_v1
COPY . ./vats_account_analytics_v1
WORKDIR /vats_account_analytics_v1/app
RUN python3 -m pip install -r ../requirements.txt
EXPOSE 8088
