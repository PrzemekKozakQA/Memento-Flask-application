# Container image that runs code
FROM ubuntu:latest

# Setup environment
RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y

# Copies code file from your action repository to the filesystem path `/` of the container
COPY . .

# Download the necessary libraries
RUN pip install -r requirements.txt

# Executes when the Docker container starts up
#ENTRYPOINT gunicorn app:app
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
