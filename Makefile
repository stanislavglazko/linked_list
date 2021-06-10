install:
	@poetry install

lint:
	@poetry run flake8 linked_list

publish:
	poetry publish -r foo3

selfcheck:
	poetry check

check: selfcheck lint

build: check
	@poetry build

test:
	poetry run pytest --cov=linked_list --cov-report xml tests/

.PHONY: install test lint selfcheck check build publish
