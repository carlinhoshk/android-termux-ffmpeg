
FROM python:3.9

WORKDIR /app

RUN pip install -r requirements.txt
RUN apt-get -y update
RUN APT-get install ffmpeg libsm6 libxext6  -y

ADD . /app
