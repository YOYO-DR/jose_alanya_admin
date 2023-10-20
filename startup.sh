#para ejecutar en el azure en el despliegue
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --no-input
python manage.py test core.crm
gunicorn config.wsgi