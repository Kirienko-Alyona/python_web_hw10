# python_web_hw10

poetry add Django

django-admin startproject project_name

docker run --name noteapp-postgres -p 5432:5432 -e POSTGRES_PASSWORD=567234 -d postgres

poetry add psycopg2

python manage.py migrate

python manage.py createsuperuser

Ctrl+C и прекращаем работу сервера.

python manage.py startapp app_mysite

python manage.py makemigrations

python manage.py migrate


Домашнее задание #10

В прошлой домашней работы вы выполняли скрапинг сайта http://quotes.toscrape.com.

Вам необходимо самостоятельно реализовать аналог такого сайта на Django.

Реализуйте возможность регистрации на сайте и вход на сайт. Возможность добавления нового автора на сайт, только для зарегистрированного пользователя. Возможность добавления новой цитаты на сайт, с указанием автора, только для зарегистрированного пользователя. Выполните миграцию базы данных с MongoDB, которая у вас есть, в Postgres для вашего сайта. Можно реализовать кастомным скриптом. (При желании можете оставить и работать с цитатами и авторами в MongoDB, а с пользователями в Postgres) Можно зайти на страницу каждого автора без аутентификации пользователя Все цитаты доступны для просмотра без аутентификации пользователя



якщо видалили таблиці з бази даних: 
python manage.py migrate --fake APPNAME zero 
This will make your migration to fake. Now you can run the migrate script

python manage.py migrate APPNAME 
Tables will be created and you solved your problem.. Cheers!!!

якщо помилка  --> django.db.utils.ProgrammingError: relation  already exists
python manage.py migrate --fake



django админка http://127.0.0.1:8000/admin/
my site http://127.0.0.1:8000
