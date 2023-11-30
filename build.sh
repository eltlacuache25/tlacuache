#!/usr/bin/env bash
# exit on error
set -o errexit

#poetry install
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

echo "from django.contrib.auth.models import User; User.objects.create_superuser('educative', 'edu@example.com', 'edu123')" | python3 manage.py shell