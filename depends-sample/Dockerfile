FROM python:3.7-alpine

COPY app/requirements.txt /usr/src
WORKDIR /usr/src

RUN apk add --no-cache gcc libc-dev postgresql-dev \
    && pip install -r requirements.txt