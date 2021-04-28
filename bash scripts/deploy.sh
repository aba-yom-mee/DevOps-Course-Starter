#!/usr/bin/env bash

docker login --username=$HEROKU_LOGIN --password=$HEROKU_API_KEY registry.heroku.com
docker build --target production --tag olutiab/my-heroku-build .
docker tag olutiab/my-heroku-build registry.heroku.com/olutiab-todo-app/web
docker push registry.heroku.com/olutiab-todo-app/web
heroku container:release web --app olutiab-todo-app
