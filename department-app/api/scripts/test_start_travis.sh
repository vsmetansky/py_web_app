#!/bin/bash

cd department-app/api
export API_TEST_CONFIG="./config/test_travis.conf"
python -m unittest discover tests
