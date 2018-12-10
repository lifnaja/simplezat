#!/bin/sh

cd simplezat
pipenv run python manage.py migrate --settings=simplezat.settings.dev
pipenv run python manage.py collectstatic --noinput --settings=simplezat.settings.dev
pipenv run uwsgi --ini uwsgi.dev.ini
