FROM ubuntu:18.04

RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN apt -y update && \
    apt -y upgrade && \
    apt-get install -y \
        build-essential \
        libffi-dev \
        libfontconfig \
        libpq-dev \
        libssl-dev \
        python3-dev \
        python3-pip \
        openssh-client \
        net-tools \
        curl \
        traceroute \
        iputils-ping \
        vim \
        dnsutils

RUN pip3 install --upgrade pip
RUN pip3 install virtualenv

ENV WORKON_HOME /home/.virtualenvs
RUN mkdir $WORKON_HOME
RUN virtualenv -p python3 $WORKON_HOME/vtest
ENV HOME /home/macoui
RUN mkdir -p $HOME
COPY src /home/macoui/src
COPY scripts /home/macoui/scripts
COPY requirements.txt /home/macoui/requirements.txt
RUN chmod +x /home/macoui/scripts/startup.sh

RUN source $WORKON_HOME/vtest/bin/activate; \
    pip3 install -r /home/macoui/requirements.txt

WORKDIR /home/macoui/src

RUN source $WORKON_HOME/vtest/bin/activate