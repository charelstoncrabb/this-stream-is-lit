FROM ubuntu:22.04


RUN apt-get update && apt-get install -y
    python3-venv

RUN mkdir /usr/src
COPY common.py /usr/src/common.py

WORKDIR /usr/src

