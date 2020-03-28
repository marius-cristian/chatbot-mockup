IMAGE=chatbot/django:2

build:
	docker build -t $(IMAGE) .

create-project:
	docker-compose run rest django-admin startproject DataService .

create-chat:
	docker-compose run rest django-admin startapp chat

create-migration:
	docker-compose run rest python manage.py makemigrations &&\
	docker-compose run rest python manage.py migrate

create-superuser:
	docker-compose run rest echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python manage.py shell

start-rest:
	docker-compose up 