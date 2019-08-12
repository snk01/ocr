FROM ubuntu:18.04
RUN apt-get update \
    && apt-get install tesseract-ocr -y \
    python3 \
    #python-setuptools \
    python3-pip \
    && apt-get clean \
    && apt-get autoremove

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

ADD . /home/app
WORKDIR /home/app
COPY . .

