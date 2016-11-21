FROM node:alpine

ARG env

WORKDIR /src
ADD ./frontend /src
RUN apk update; apk add python make gcc g++ git
RUN npm install -gq gulp bower
RUN npm install -q
RUN bower install --allow-root
ADD web/ksupcapp /ksupcapp
