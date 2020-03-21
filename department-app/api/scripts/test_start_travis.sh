#!/bin/bash

cd ..
export TEST_CONFIG="./config/test_travis.conf"
python -m unittest discover tests
