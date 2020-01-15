FROM python:3.7.4
MAINTAINER thp44

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt
RUN apt-get update
RUN apt-get install gdal-bin -y

RUN mkdir /web
WORKDIR /web
COPY ./web /web

#RUN useradd -ms /bin/bash newuser
#USER newuser
