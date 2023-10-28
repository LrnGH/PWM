FROM python:3.12-alpine3.18 AS base
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

FROM base AS app 
COPY ./app /app
WORKDIR /app
EXPOSE 8001