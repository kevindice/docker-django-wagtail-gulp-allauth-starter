FROM python:3.5
ENV PYTHONUNBUFFERED 1

# User defined.  See docker-compose.yml at web.build.args
ARG env

WORKDIR /app
ADD requirements/*.txt /app/requirements/
RUN pip install -r requirements/$env.txt
ADD . /app

#COPY ./docker-entrypoint.sh /
#ENTRYPOINT ["/docker-entrypoint.sh"]
