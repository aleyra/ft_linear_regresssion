#!/usr/bin/sh

# to call: `source set_env.sh`

python3 -m venv ENV_linear_regression
source ENV_linear_regression/bin/activate
pip install -r requirements.txt