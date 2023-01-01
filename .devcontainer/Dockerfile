FROM python:3.11

RUN apt-get update

WORKDIR /workspace
COPY requirements/ requirements/
RUN pip3 install -r requirements/dev.txt
