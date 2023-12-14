FROM python:3

RUN apt-get -y update \
	&& pip install scapy

WORKDIR /usr/src/app

COPY inquisitor.py .

CMD ["tail", "-f", "/dev/null"]
