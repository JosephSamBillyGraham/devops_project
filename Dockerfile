# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Expose Flask port
EXPOSE 5000

# Run the app
CMD ["python", "app/app.py"]
