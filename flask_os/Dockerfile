FROM python:3.10-slim

COPY . /app
WORKDIR /app

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
