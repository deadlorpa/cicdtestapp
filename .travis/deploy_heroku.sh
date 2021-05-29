wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
docker login --username=_ --password=$HEROKU_API_KEY registry.heroku.com
heroku container:login
heroku container:push web --app $HEROKU_APP_NAME
heroku container:release web