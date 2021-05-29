#!/bin/sh
docker login -u $DOCKER_USER -p $DOCKER_PASSWORD
if [ "$TRAVIS_BRANCH" = "master" ]; then
    TAG="latest"
else
    TAG="$TRAVIS_BRANCH"
fi
docker build -t testapp:TAG /home/travis/build/deadlorpa/CiCdTestApp .
docker push testapp:TAG