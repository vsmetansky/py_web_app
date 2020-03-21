#!/bin/bash

cd ..
if [["$VIRTUAL_ENV" == ""]]; then
    source venv/bin/activate
fi
export APP_CONFIG="./config/app.conf"
python wsgi.py
