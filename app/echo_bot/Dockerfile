FROM python:3.11-buster

RUN apt-get update
RUN apt-get install -y vim

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
