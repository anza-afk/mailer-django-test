## Установка:

Для работы требуется Python версии 2.7.18

    http: git clone https://github.com/anza-afk/mailer-django-test.git
    ssh: git clone git@github.com:anza-afk/mailer-django-test.git

    pip install -r requirements.txt
    pip install redis-server

В файле .env по образцу .env example заполняются переменные:
почта, хост, пароль и django secret key

    cd mailer

### Создание суперпользователя:
  
python manage.py createsuperuser

*Для добавления шаблонов писем их необходимо класть в mail_factory/templates/email_templates
и регистрировать в базе данных - в поле title - название, которе будет отображаться при выборе шаблона
в поле content - путь до шаблона вида "email_templates/название_файла.html"*

 *Для отслеивания открытия письма в шаблон нужно добавить строку:
    <img src="{{ image_url }}?client={{ client.id }}&mailing={{mailing}}" height="0px" width="0px"/>
(однако, для работоспособности этого подхода проект необходимо деплоить.)*

### Запуск Celery для пересылок отложенных писем:
    celery -A mailer worker -l info -B

### Запуск проекта:
    python manage.py runserver
