# Use Node.js base image
FROM node:18

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY ./package.json ./package.json
COPY ./package-lock.json ./package-lock.json
RUN npm install

# Copy the source code
COPY ./ ./

# Expose the React port
EXPOSE 3000

# Start the React application
CMD ["npm", "start"]