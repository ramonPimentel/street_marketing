FROM python:3.8-slim

RUN mkdir -p /src
WORKDIR /src

RUN apt-get update && \
    apt-get -y install build-essential

ADD . .

RUN pip install --upgrade pip \
    pip install setuptools wheel --no-cache-dir --upgrade \
    pip install --no-cache-dir -r ./base.txt
  
EXPOSE 9000