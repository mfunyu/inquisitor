FROM python:3

RUN apt-get -y update \
	&& pip install scapy

WORKDIR /usr/src/app

COPY inquisitor.py .
RUN sed -i "s;#!/usr/bin/python3;#!/usr/local/bin/python3;" inquisitor.py

CMD ["tail", "-f", "/dev/null"]
