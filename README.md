# Ativar conda
conda activate web-sites-django-3

# Criar projeto django
django-admin startproject blog

# Rodar o projeto django
python manage.py runserver

# Criar tabelas no banco de dados
python manage.py migrate

# Criar super usuário
python manage.py createsuperuser