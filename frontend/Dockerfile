FROM node:alpine

ARG env

WORKDIR /src
ADD ./frontend /src
RUN apk update; apk add python make gcc g++ git
RUN npm install -gq gulp bower
RUN npm install -q
RUN bower install --allow-root
WORKDIR /static
ADD web/ksupcapp/static /static
WORKDIR /src
