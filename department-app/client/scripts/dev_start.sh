#!/bin/bash

if [[ "$VIRTUAL_ENV" == "" ]]; then
    source venv/bin/activate
fi
export CLIENT_CONFIG="./config/app.conf"
export CLIENT_BASE_URL="localhost:7000"
export API_BASE_URL="localhost:8000"
export CLIENT_LOG_DIR="./logs/error.log"
gunicorn -c config/gunicorn.py wsgi:APP --reload --reload-extra-file ./templates
bash scripts/del_cache.sh
