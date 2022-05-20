#!/usr/bin/env bash

set -e
set -x

poetry run flake8 app

