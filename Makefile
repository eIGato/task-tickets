.PHONY: up down logs test format migrate makemigrations static createsuperuser

up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

test:
	docker compose run --rm web pytest

format:
	docker compose run --rm web black .

migrate:
	docker compose run --rm web python manage.py migrate

migrations:
	docker compose run --rm web python manage.py makemigrations

static:
	docker compose run --rm web python manage.py collectstatic

createsuperuser:
	docker compose run --rm web python manage.py createsuperuser
