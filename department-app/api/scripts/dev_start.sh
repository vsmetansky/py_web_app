#!/bin/bash

cd ..
if [["$VIRTUAL_ENV" == ""]]; then
    source venv/bin/activate
fi
export API_CONFIG="./config/app.conf"
export API_BASE_URL="localhost:8000"
python wsgi.py
