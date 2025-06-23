#!/bin/sh

echo "==> Aplicando migrações..."
python manage.py migrate --noinput

echo "==> Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

echo "==> Iniciando Gunicorn..."
exec gunicorn recursos.wsgi:application --bind 0.0.0.0:${PORT:-8000}
