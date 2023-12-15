FROM python:3

RUN apt-get -y update \
	&& apt-get -y install openssh-server \
	&& pip install scapy

EXPOSE 22

RUN useradd -m -s /bin/bash user \
	&& echo "user:password" | chpasswd

WORKDIR /usr/src/app

COPY inquisitor.py .
RUN sed -i "s;#!/usr/bin/python3;#!/usr/local/bin/python3;" inquisitor.py

CMD ["tail", "-f", "/dev/null"]
