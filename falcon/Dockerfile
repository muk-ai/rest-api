FROM python:3.5
MAINTAINER Kenta Mukai

ENV app_dir /var/apps/rest-api

RUN mkdir -p $app_dir
WORKDIR $app_dir
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD uwsgi.ini .
ADD hello.py .

EXPOSE 3031
CMD ["/usr/local/bin/uwsgi", "uwsgi.ini"]
