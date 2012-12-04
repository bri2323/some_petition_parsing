#!/bin/bash

./dl.sh
python parse.py
python ./to_csv.py
