#!/bin/bash

cd department-app
export TEST_CONFIG="./config/test_travis.conf"
python -m unittest discover tests
