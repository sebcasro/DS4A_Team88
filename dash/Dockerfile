FROM python:3.7-slim-buster

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

WORKDIR /dash_app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt