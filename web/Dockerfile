FROM python:3.5
ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD requirements/*.txt /app/requirements/
RUN pip install -r requirements/dev.txt
ADD . /app

#COPY ./docker-entrypoint.sh /
#ENTRYPOINT ["/docker-entrypoint.sh"]
