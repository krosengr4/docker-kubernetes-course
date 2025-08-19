# Base image
FROM node:22-alpine3.20

# Set the working directory
WORKDIR /app

# Copy dependencies
COPY package*.json .

# Run commands to install the dependencies 
RUN npm ci

# Copy the source folder into source folder of our container
COPY src src

# Run the command to run the application
CMD ["npm", "start"]