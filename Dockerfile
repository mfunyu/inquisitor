FROM ubuntu:latest

RUN apt-get -y update \


CMD ["tail", "-f", "/dev/null"]
