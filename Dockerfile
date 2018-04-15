FROM resin/rpi-raspbian:stretch

# Install dependencies
RUN apt-get update && apt-get install -y python3 python3-pip virtualenv

RUN mkdir /srv/project
WORKDIR /srv/project
ADD ./requirements.txt /srv/project/

RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install -r requirements.txt

COPY . /srv/project/

CMD /usr/bin/python3 sensor.py