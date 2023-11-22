# Container image that runs code
FROM ubuntu:22.04
#FROM python:3.8-alpine

# Setup environment
RUN apt-get update
# RUN apt-get install -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
# RUN pip install flask

# Copies code file from your action repository to the filesystem path `/` of the container
COPY . .

# Download the necessary libraries
RUN pip install -r requirements.txt

# Executes when the Docker container starts up
ENTRYPOINT gunicorn app:app
