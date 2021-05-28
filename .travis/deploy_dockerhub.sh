#!/bin/sh
docker login -u $DOCKER_USER -p $DOCKER_PASSWORD
if [ "$TRAVIS_BRANCH" = "master" ]; then
    TAG="latest"
else
    TAG="$TRAVIS_BRANCH"
fi
docker build tag alpine-img:latest $DOCKER_USER/alphine:latest .
docker push $DOCKER_USER/alphine:latest