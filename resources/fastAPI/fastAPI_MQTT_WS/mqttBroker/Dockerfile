FROM debian:buster

RUN apt-get update -y \
 && apt-get install -y mosquitto


WORKDIR /code 

COPY ./test.conf /code/test.conf

RUN mosquitto -c test.conf
