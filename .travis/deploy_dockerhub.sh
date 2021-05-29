#!/bin/sh
docker login -u $DOCKER_USER -p $DOCKER_PASSWORD
if [ "$TRAVIS_BRANCH" = "master" ]; then
    TAG="latest"
else
    TAG="$TRAVIS_BRANCH"
fi
echo $TRAVIS_BRANCH
echo $TRAVIS_REPO_SLUG
docker build -t testapp:TAG $TRAVIS_REPO_SLUG .
docker push testapp:TAG