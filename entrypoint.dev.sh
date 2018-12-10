#!/bin/sh

cd simplezat
pipenv run python manage.py migrate --settings=simplezat.settings.dev
pipenv run python manage.py runserver 0.0.0.0:8000 --settings=simplezat.settings.dev
