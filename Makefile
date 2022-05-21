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


# Test and Code Quality
# -----------------------------------------------------------------------------
_black:
	docker-compose run --rm --no-deps server black --check .

_black_fix:
	docker-compose run --rm --no-deps server black .

_isort:
	docker-compose run --rm --no-deps server isort --diff --check-only .

_isort_fix:
	docker-compose run --rm --no-deps server isort .

_mypy:
	docker-compose run --rm --no-deps server mypy . --exclude migrations

lint: _isort _black _mypy

format-code: _isort_fix _black_fix
