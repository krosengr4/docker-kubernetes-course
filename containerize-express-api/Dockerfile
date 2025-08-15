# Base image
FROM node:22

# Set working directory for the rest of the file
WORKDIR /app

# Copy the package.json and the package-lock.json
# Can use the * here to include both json files
COPY package*.json .

# Install dependencies
RUN npm ci

# Copy the source code of our app(src/index.js) into the index.js file
COPY index.js index.js

# Expose the application port
EXPOSE 3000

# Start application
# ["Environment the app is in", "The source code/file"]
CMD ["node", "index.js"]
