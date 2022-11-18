Для работы требуется Python версии 2.7.18

## Установка:


http: 

    git clone https://github.com/anza-afk/mailer-django-test.git
ssh: 

    git clone git@github.com:anza-afk/mailer-django-test.git

### В случае запуска в контейнере с Python версии 2.7.18:

    cd mailer-django-test/

В файле .env по образцу .env example заполняются переменные:
почта, хост, пароль и django secret key

*(Если используется утилита для работы с несколькими версиями интерпретатора (например Pyenv), 
в директории mailer-django-test используется интерпретатор python 2.7.18 и создаётся виртуальное окружение для него)* 

### Создание виртуального окружения при помощи pyenv:

    pyenv install 2.7.18
    pyenv local 2.7.18
    pyenv virtualenv venv
    pyenv local venv
    
    cd mailer

    pip install -r requirements.txt


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
