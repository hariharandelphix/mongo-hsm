# pull uvicorn-gunicorn-fast-api-slim image that is optimised for performance
FROM python:3.9-slim

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV MODULE_NAME=src.main
ENV PORT=8080
ENV LOG_LEVEL=debug
ENV PYTHONPATH=/app

# for log file
RUN mkdir -p /opt/delphix/logs/

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

RUN mkdir -p /app
COPY ./container_conf/app_files/* /app
COPY ./container_conf/root_files/* /

COPY ./src /app/src

WORKDIR /app
ENTRYPOINT ["../start.sh"]

