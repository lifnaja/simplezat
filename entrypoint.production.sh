#!/bin/sh

cd simplezat
pipenv run python manage.py migrate --settings=simplezat.settings.prod
pipenv run python manage.py collectstatic --noinput --settings=simplezat.settings.prod
pipenv run uwsgi --ini uwsgi.prod.ini
