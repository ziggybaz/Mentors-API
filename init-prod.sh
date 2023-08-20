#!/bin/bash



export FLASK_APP=manage.py &&  python manage.py create_db && python manage.py read "./data-source/sample-2.csv" && gunicorn manage:app

