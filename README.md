# Make mtlynch Stats

[![CircleCI](https://circleci.com/gh/mtlynch/make-mtlynch-stats.svg?style=svg)](https://circleci.com/gh/mtlynch/make-mtlynch-stats)

## Overview

Makes stats for the mtlynch.io blog.

## Installation

```bash
mkdir -p ./venv
virtualenv --python python3 ./venv
. venv/bin/activate
pip install --requirement requirements.txt
pip install --requirement dev_requirements.txt
```

## Run

```bash
CSV_URL="your CSV url"
wget -qO- "$CSV_URL" | ./app/main.py
```