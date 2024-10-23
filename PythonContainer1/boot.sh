#!/bin/sh

pip install virtualenv
python -m venv .venv
. .venv/bin/activate
pip install --no-cache-dir -r requirements.txt
