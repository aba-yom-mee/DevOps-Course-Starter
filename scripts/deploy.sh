#!/usr/bin/env bash

docker login --username=$HEROKU_LOGIN --password=$HEROKU_API_KEY registry.heroku.com
docker build --target production --tag olutiab/olutiab-todo-app .
docker tag olutiab/olutiab-todo-app registry.heroku.com/olutiab-todo-app/web
docker push olutiab/olutiab-todo-app
docker push registry.heroku.com/olutiab-todo-app/web
heroku container:release web --app olutiab-todo-app
