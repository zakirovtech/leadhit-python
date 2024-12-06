FROM python:3.13-slim

WORKDIR /usr/app/src/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONDONUNBUFFERED 1

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt 

COPY . .
