Установка:

http: git clone https://github.com/anza-afk/mailer-django-test.git
ssh: git clone git@github.com:anza-afk/mailer-django-test.git

pip install -r requirements.txt

далее в файл .env по образцу .env example заполняются переменные:
почта, хост, пароль и django secret key

cd mailer

Создание суперпользователя:
python manage.py createsuperuser


Запуск Celery для пересылок отложенных писем:
celery -A mailer worker -l info -B

Запуск проекта:
python manage.py runserver