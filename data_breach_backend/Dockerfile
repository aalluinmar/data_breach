# This dockerfile is used to build data_breach_backend

ARG BUILD_DATE
ARG VCS_REF

#Pull base image
FROM python:3.7.3

MAINTAINER Allu Aravind <aravind.edu2021@gmail.com>

ADD . /code/
WORKDIR /code
COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh
RUN pip install -r ./requirements/test.txt