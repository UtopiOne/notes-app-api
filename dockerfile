FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN mkdir /good_notes
WORKDIR /good_notes

ADD . /good_notes/

RUN pip install -r requirements.txt