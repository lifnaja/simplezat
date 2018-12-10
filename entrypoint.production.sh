#!/bin/sh

cd simplezat
pipenv run python manage.py migrate --settings=simplezat.settings.prod
pipenv run python manage.py runserver 0.0.0.0:8000 --settings=simplezat.settings.prod
