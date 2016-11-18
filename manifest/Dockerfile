FROM python:2.7
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
ADD . /app
