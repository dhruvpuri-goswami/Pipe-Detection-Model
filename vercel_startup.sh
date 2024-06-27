#!/bin/bash
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --no-input
gunicorn pipedetection.wsgi:application --bind 0.0.0.0:$PORT --workers 3
