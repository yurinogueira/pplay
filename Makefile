#!/bin/bash
.PHONY: default
.SILENT:


default:

bash:
	docker compose run --rm server bash

build:
	docker compose run --rm server python setup.py sdist bdist_wheel

requirements:
	docker compose run --rm server python -m pip install --upgrade pip && pip install -r requirements.txt

docker-rebuild:
	docker compose build --force-rm --no-cache --pull
