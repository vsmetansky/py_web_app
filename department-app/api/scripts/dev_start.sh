#!/bin/bash

if [[ "$VIRTUAL_ENV" == "" ]]; then
    source venv/bin/activate
fi
export API_CONFIG="./config/app.conf"
export API_BASE_URL="localhost:8000"
export API_LOG_DIR="./logs/error.log"
gunicorn -c config/gunicorn.py wsgi:APP --reload
bash scripts/del_cache.sh
