#!/bin/bash

[ ! -d .venv ] && python -m venv .venv
source .venv/bin/activate
pip install -U -r requirements.txt
python main.py
