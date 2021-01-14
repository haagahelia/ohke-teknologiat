# Source: https://nodejs.org/en/docs/guides/nodejs-docker-webapp/
FROM node:12-slim

# Create app directory
WORKDIR /usr/src/app

# Set port variable for Express
ENV PORT=80

# Copy package and package-lock
COPY package*.json .

# Install app dependencies
RUN npm install

# Copy app source to container
COPY . .

# Open port 80
EXPOSE 80

CMD [ "node", "index.js" ]