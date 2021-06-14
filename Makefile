POETRY_EXPORT := poetry export --without-hashes -f requirements.txt

# Requirements
requirements.txt: poetry.lock
	$(POETRY_EXPORT) -o $@

requirements-dev.txt: poetry.lock
	$(POETRY_EXPORT) --dev -o $@

# Testing
.PHONY: test-lint
test-lint:
	-poetry run flake8

.PHONY: test-unit
test-unit:
	-poetry run pytest -s

.PHONY: tests
tests: test-lint test-unit

# Utilities
.PHONY: clean
clean:
	find . | grep [py]cache | xargs rm -rf
