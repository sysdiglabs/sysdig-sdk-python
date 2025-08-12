

.PHONY: test
test:
	uv run mamba -f documentation

.coverage:
	uv run coverage run $(shell uv run which mamba) -f documentation || true

cover: .coverage
	uv run coverage report --include 'sdcclient/*'

.PHONY: cover-html
cover-html: .coverage
	uv run coverage html -d coverage --include 'sdcclient/*'

init:
	uv sync

lint:
	uvx ruff check --fix --config ruff.toml

fmt:
	uvx ruff format --config ruff.toml

test-all: cover
