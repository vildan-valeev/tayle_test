MANAGE := poetry run python manage.py

app_run: migrate runserver

runserver:
	$(MANAGE) runserver

makemigrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate --noinput

createsuperuser:
	$(MANAGE) createsuperuser

static:
	$(MANAGE) collectstatic --noinput
