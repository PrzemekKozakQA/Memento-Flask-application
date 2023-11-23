# Container image that runs code
FROM python:3.12.0-alpine3.18

# Update environment
RUN apk -U update

# Copies code file from your action repository to container
COPY ./app/ ./app/

# Download the requir libraries
RUN pip install -r ./app/requirements.txt

# Run app with gunicorn
RUN cd app
ENTRYPOINT  ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

# Expose ports
EXPOSE 5000
