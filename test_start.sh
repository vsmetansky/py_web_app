#!/bin/sh

cd department-app
if [["$VIRTUAL_ENV" == ""]]; then
    source venv/bin/activate
fi
export TEST_CONFIG="./config/test.conf"
python -m unittest discover tests
