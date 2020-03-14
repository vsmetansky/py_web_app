#!/bin/bash

cd department-app
if [[ "$VIRTUAL_ENV" == "" ]]; then
    source venv/bin/activate
fi
export APP_CONFIG="./config/app.conf"
gunicorn -c config/gunicorn.py wsgi:app
