POETRY_EXPORT := poetry export --without-hashes -f requirements.txt
POETRY_RUN := poetry run
SHELL := /bin/bash

# Installing
.make.install: poetry.lock
	poetry install --no-dev
	touch $@

.PHONY: install
install: .make.install

.make.install-dev: poetry.lock
	poetry install
	touch $@

.PHONY: install-dev
install-dev: .make.install-dev

# Virtual environment
poetry.lock: pyproject.toml
	poetry lock
	touch $@

requirements-dev.txt: poetry.lock
	$(POETRY_EXPORT) --dev -o $@

# Testing
.PHONY: test-lint
test-lint: | .make.install-dev
	$(POETRY_RUN) flake8

.PHONY: test-unit
test-unit: | .make.install-dev
	$(POETRY_RUN) pytest -s

.PHONY: tests
tests: test-lint test-unit

# Utilities
.PHONY: clean
clean:
	find . | grep [py]cache | xargs rm -rf
	rm -f .make.*
