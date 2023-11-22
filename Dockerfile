# Container image that runs code
FROM ubuntu:latest

# Setup environment
RUN apt-get update -y
RUN apt-get install -y
RUN apt-get install python3 -y
RUN apt-get install python-pip -y
RUN pip3 install flask

# Copies code file from your action repository to the filesystem path `/` of the container
COPY . .

# Download the necessary libraries
RUN pip install -r requirements.txt

# Executes when the Docker container starts up
ENTRYPOINT gunicorn app:app
