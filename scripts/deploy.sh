#!/usr/bin/env bash

echo "$HEROKU_API_KEY" | docker login -u "$HEROKU_LOGIN" --password-stdin registry.heroku.com
docker build --target production --tag olutiab/olutiab-todo-app --tag registry.heroku.com/olutiab-todo-app/web .
# docker build --target production --tag olutiab/olutiab-todo-app .
# docker tag olutiab/olutiab-todo-app registry.heroku.com/olutiab-todo-app/web
docker push olutiab/olutiab-todo-app
docker push registry.heroku.com/olutiab-todo-app/web
heroku container:release web --app olutiab-todo-app
