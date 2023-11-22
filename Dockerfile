# Container image that runs code
FROM ubuntu:latest

# Setup environment
RUN apt-get install -y python3
RUN apt-get install python-pip -y
RUN pip install flask

# Copies code file from your action repository to the filesystem path `/` of the container
COPY . .

# Download the necessary libraries
RUN pip install -r requirements.txt

# Executes when the Docker container starts up
ENTRYPOINT gunicorn app:app
