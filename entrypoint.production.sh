#!/bin/sh

cd simplezat
pipenv run python manage.py migrate migrate --setting=simplezat.setting.prod
pipenv run python manage.py runserver 0.0.0.0:8000 --setting=simplezat.setting.prod
