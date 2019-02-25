# Dockerfile

# Use base python image with python 3.6
# FROM directive instructing base image to build upon
FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

ADD . /app/

# Set working directory to /app/
WORKDIR /app/

# Add requirements.txt to the image
#ADD requirements.txt /app/

#RUN apk update && apk install add build-base postgresql-dev libffi-dev

#RUN apk update
#RUN apk add --virtual=build-dependencies tzdata ca-certificates \
#curl gcc py-cffi py-cryptography python-dev libffi-dev openssl-dev build-base linux-headers

# Install python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# Create unprivileged user
#RUN adduser --disabled-password --gecos '' myuser

# Add startup script into known file location in container
#ADD run_celery.sh /app/

# CMD specifcies the command to execute to start the server running.
CMD python manage.py celery worker -B --loglevel=INFO
# done!
