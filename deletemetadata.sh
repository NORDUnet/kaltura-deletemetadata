#!/bin/bash
set -e
source venv/bin/activate
python deletemetadata.py "$@"
