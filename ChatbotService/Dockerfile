FROM python:3
ENV PYTHONUNBUFFERED 2
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY simpleclient.py /app
