#!/bin/bash

source deploy.env

sudo docker build -t $IRTV_IMAGE_NAME .
sudo docker run -d --name   $IRTV_CONTAINER_NAME $IRTV_IMAGE_NAME
