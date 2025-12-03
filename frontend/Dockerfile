FROM node:20-alpine

# Set working directory
WORKDIR /app

# Copy dependency files
COPY package.json package-lock.json ./

# Install dependencies
RUN npm ci

# Copy application code
COPY . .

# Expose port
EXPOSE 3000

# Run the application in development mode
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
