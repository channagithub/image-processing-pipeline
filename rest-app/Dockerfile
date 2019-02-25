FROM python:3.5.3

WORKDIR /app/

RUN apt update
RUN apt install -y supervisor
RUN pip install gunicorn setuptools

COPY requirements.txt /app/
RUN pip install -r ./requirements.txt

# make dir to mount config files
RUN mkdir -p /var/log/supervisor
RUN mkdir -p /var/log/granular