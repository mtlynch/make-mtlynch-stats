# Make mtlynch Stats

[![CircleCI](https://circleci.com/gh/mtlynch/make-mtlynch-stats.svg?style=svg)](https://circleci.com/gh/mtlynch/make-mtlynch-stats) [![Coverage Status](https://coveralls.io/repos/github/mtlynch/make-mtlynch-stats/badge.svg?branch=master)](https://coveralls.io/github/mtlynch/make-mtlynch-stats?branch=master)

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