#!/bin/bash

if [[ "$VIRTUAL_ENV" == "" ]]; then
    source venv/bin/activate
fi
export APP_CONFIG="./config/app.conf"
export LOG_DIR="./logs/error.log"
gunicorn -c config/gunicorn.py wsgi:APP
bash scripts/del_cache.sh