#!/bin/bash
app="docker.test_9"
docker build -t ${app} .
docker run -d -p 56732:80 \
  --name=${app} \
  -v $PWD:/app ${app}
