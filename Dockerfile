FROM python:2.7

MAINTAINER Pooya Moradi <ibtkm2009@gmail.com>

RUN mkdir -p /home/irtv
WORKDIR /home/irtv

COPY confs/requirements.txt /tmp/requirementst.txt
RUN pip install -r /tmp/requirementst.txt && rm /tmp/requirementst.txt

COPY ./src /home/irtv

CMD ["python", "main.py"]
