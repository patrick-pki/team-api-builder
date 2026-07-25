# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first (for better caching)
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy ALL the files from your project into the container
COPY . .

# Expose port 8080 so we can access the web app
EXPOSE 8080

# Command to run the application when the container starts
CMD ["python", "app.py"]
