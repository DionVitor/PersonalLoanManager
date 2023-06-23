FROM node:16

ENV HOST=0.0.0.0

WORKDIR /app
COPY package*.json ./
RUN npm install

COPY *.js ./
COPY *.html ./

EXPOSE 8080