# Container image that runs code
FROM 3.12.0-alpine3.18

# Setup environment
RUN apt -U update

# Copies code file from your action repository to the filesystem path `/` of the container
COPY . .

# Download the necessary libraries
RUN pip install -r requirements.txt

# Executes when the Docker container starts up
ENTRYPOINT  ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
# CMD ["gunicorn", "--bind", "0.0.0.0", "app:app"]
