#!/bin/bash

cd department-app
if [[ "$VIRTUAL_ENV" == "" ]]; then
    source venv/bin/activate
fi
export APP_CONFIG="./config/app.conf"
export LOG_DIR="./logs/error.log"
gunicorn -c config/gunicorn.py wsgi:app
bash ../scripts/del_cache.sh