# Dockerfile for test-faust
FROM ubuntu:19.10

MAINTAINER Pimin Konstantin Kefaloukos "pimin.konstantin.kefaloukos@maersk.com"

# install git
RUN apt-get update -y

RUN apt-get install -y python3-pip libpq-dev

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY *.py /
