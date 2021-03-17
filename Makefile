build:
	docker-compose build

mypy:
	docker-compose run --rm web mypy . --ignore-missing-imports

lint:
	docker-compose run --rm web pylint mldeploy --disable=missing-function-docstring,missing-module-docstring

init-db:
	docker-compose up -d
	docker-compose run --rm web flask init-db
