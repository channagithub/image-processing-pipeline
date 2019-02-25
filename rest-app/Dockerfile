FROM python:3.5.3

WORKDIR /app/

RUN apt update
RUN apt install -y supervisor
RUN pip install gunicorn setuptools

COPY ./../rest-app/requirements.txt /app/
RUN pip install -r ./requirements.txt

COPY build_tokenizer.py /app/
RUN python build_tokenizer.py

# Setup supervisord
RUN mkdir -p /var/log/supervisor
RUN mkdir -p /var/log/granular
COPY ./../rest-app/app_configs/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY ./../rest-app/app_configs/granular.conf /etc/supervisor/conf.d/

COPY ./../rest-app/ /app/