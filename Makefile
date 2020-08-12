

.PHONY: test
test:
	pipenv run mamba -f documentation

.coverage:
	pipenv run coverage run $(shell pipenv run which mamba) -f documentation || true

cover: .coverage
	pipenv run coverage report --include 'sdcclient/*'

.PHONY: cover-html
cover-html: .coverage
	pipenv run coverage html -d coverage --include 'sdcclient/*'

