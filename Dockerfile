# Use the official Python image as the base image
FROM python:3.12.1-slim

# Set the working directory
WORKDIR /app

# Copy only the necessary files for dependencies installation
COPY src/requirements.txt /app/src/
# COPY test/requirements.txt /app/test/

# Install any dependencies
RUN pip install --no-cache-dir -r src/requirements.txt
# RUN pip install --no-cache-dir -r test/requirements.txt

# Copy the contents into the container at /app/
COPY src /app/src/
COPY static /app/static/
COPY templates /app/templates/
COPY logs /app/logs/
COPY .env /app/
COPY profile.db /app/

# Expose the port that Uvicorn will run on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "src.main:app"]
