.PHONY: help init lint fmt test test-coverage

help:
	@echo "Available commands:"
	@echo "  make init    - Install dependencies"
	@echo "  make lint    - Lint and fix code"
	@echo "  make fmt     - Format code"
	@echo "  make test    - Run tests"
	@echo "  make test-coverage - Run tests and generate coverage report"

init:
	uv sync

lint:
	uvx ruff check --fix --config ruff.toml

fmt:
	uvx ruff format --config ruff.toml

test:
	uv run pytest --capture=tee-sys --junitxml=pytest.xml

test-coverage:
	uv run pytest --cov=. --cov-report=xml

test-all: test test-coverage

update-api-spec-submodule:
	git submodule update --init --recursive

build-openapi-yaml: update-api-spec-submodule
	cd api-spec && make merge-all

openapi-update-python-client: post-openapi-update build-openapi-yaml
	@echo "Generating Python client from OpenAPI definition..."
	openapi-generator-cli generate -i api-spec/openapi.yaml -g python -o . -c .openapi-generator/config.yaml

post-openapi-update: openapi-update-python-client
	@echo "Running post-update tasks..."
	./scripts/move_model_docs.sh
