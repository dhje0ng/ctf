#!/bin/sh
docker build . -t ppower --platform linux/amd64
docker rm -f $(docker ps -aq)
docker run -d --rm --name ppower -p 8000:8000 ppower
