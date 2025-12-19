#!/bin/bash
set -e
if [ ! -d venv ]; then
  python3 -m venv venv
fi
. venv/bin/activate
pip install -U -r requirements.txt
