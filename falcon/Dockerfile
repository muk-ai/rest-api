FROM python:3.5
MAINTAINER Kenta Mukai

RUN mkdir -p /var/apps/project
WORKDIR /var/apps/project
ADD requirements.txt /var/apps/project
RUN pip install -r requirements.txt
ADD uwsgi.ini /var/apps/project
ADD hello.py /var/apps/project

EXPOSE 3031
CMD ["/usr/local/bin/uwsgi", "/var/apps/project/uwsgi.ini"]
