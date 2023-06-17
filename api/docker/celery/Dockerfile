FROM python:3.11

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /code

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY ../.. /code/
