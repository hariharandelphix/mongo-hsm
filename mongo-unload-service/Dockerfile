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

# Install MongoDB tools and mongosh utility
# Install dependencies
RUN apt-get update && \
    apt-get install -y wget && \
    wget https://fastdl.mongodb.org/tools/db/mongodb-database-tools-rhel80-x86_64-100.7.2.tgz && \
    wget https://downloads.mongodb.com/compass/mongosh-1.10.0-linux-x64.tgz && \
    tar -zxvf mongodb-database-tools-rhel80-x86_64-100.7.2.tgz -C /app && \
    mv /app/mongodb-database-tools-rhel80-x86_64-100.7.2 /app/mongodb-database-tools && \
    tar -zxvf mongosh-1.10.0-linux-x64.tgz -C /app && \
    mv /app/mongosh-1.10.0-linux-x64 /app/mongosh && \
    find /app/mongodb-database-tools/bin ! -name 'mongoexport' -type f -exec rm -f {} \; && \
    mv /app/mongosh/bin/mongosh /app/mongodb-database-tools/bin && \
    rm -rf mongodb-database-tools-*.tgz mongosh-1.10.0-*.tgz /app/mongosh && \
    apt-get remove -y wget && \
    apt-get autoremove -y && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/*

COPY ./container_conf/app_files/* /app
COPY ./container_conf/root_files/* /

COPY ./src /app/src

WORKDIR /app
ENTRYPOINT ["../start.sh"]

