#!/bin/bash

export API_TEST_CONFIG="./config/test_travis.conf"
python -m unittest discover tests
