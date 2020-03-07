#!/bin/sh

cd department-app
if [["$VIRTUAL_ENV" == ""]]; then
    source venv/bin/activate
fi
export APP_CONFIG="./config/app.conf"
export FLASK_APP="./wsgi.py"
flask run
