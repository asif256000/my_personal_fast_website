FROM python:3.12.1-slim

WORKDIR /app

# Copy only the necessary files for dependencies installation
COPY src/requirements.txt /app/src/
# COPY test/requirements.txt /app/test/

# Install any dependencies
RUN pip install --no-cache-dir -r src/requirements.txt
# RUN pip install --no-cache-dir -r test/requirements.txt
RUN apt-get update && apt-get install -y logrotate

# Copy the contents into the container at /app/
COPY src /app/src/
# COPY test /app/test
COPY static /app/static/
COPY templates /app/templates/
COPY logs /app/logs/
COPY .env /app/
COPY profile.db /app/
# COPY run_server.sh /run_server.sh
# # Make sure the script is executable
# RUN chmod +x /run_server.sh

# Expose the port that Uvicorn will run on
EXPOSE 80

# Command to run the application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]

