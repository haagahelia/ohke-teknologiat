FROM ubuntu:latest

RUN apt update
RUN apt install -y nodejs
RUN apt install -y curl
RUN curl -L https://fly.io/install.sh | sh

WORKDIR /app

COPY *.js .

CMD ["node", "app.js"]
