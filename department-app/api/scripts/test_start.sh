#!/bin/bash

cd ..
if [[ "$VIRTUAL_ENV" == "" ]]; then
    source venv/bin/activate
fi
export API_TEST_CONFIG="./config/test.conf"
python -m unittest discover tests
bash scripts/del_cache.sh