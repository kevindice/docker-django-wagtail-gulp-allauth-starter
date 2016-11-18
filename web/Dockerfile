FROM python:3.5
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD requirements/base.txt /app/requirements/base.txt
RUN pip install -r requirements/base.txt
ADD . /app

#COPY ./docker-entrypoint.sh /
#ENTRYPOINT ["/docker-entrypoint.sh"]
