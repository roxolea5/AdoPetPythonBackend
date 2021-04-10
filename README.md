# AdoPetPythonBackend

## Starting Django Project

This project was created inside a virtual environment. If is not there use:

```
pip install virtualenv
```

Once virtualenv is installed and folder project created. Create a virtual env:

```
virtualenv virtualenv_name
```

Activate virtualenv (for Windows):

```
virtualenv_name\Scripts\activate.bat
```

Install django
```
pip install django
```

Create Django project
```
django-admin startproject project_name
```

Create Django app
```
python manage.py startapp app_name
```
### Map project urls to app urls
Create file urls.py inside app folder and modify project urls.py file
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("app.urls")), 
    path('admin/', admin.site.urls),
]
```
Modify urls.py on app folder to access corresponding views
```
 from django.urls import path
  from . import views

  urlpatterns = [
 path('', views.index, name="index"),
  ]
```
Modify views.py on app folder to display something on index (index function)

Create folder templates to add html files in there.

Install mysql
```
pip install mysqlclient
```

Create docker image
```
docker create --name djangosql -e MYSQL_ROOT_PASSWORD=password -p 3306:3306 mysql
```

Start image
```
docker start djangosql
```
If port is not available go to task manager and end task "mysqld"

To see docker image execute
```
docker ps
```
Create pets.sql file to initialize db
docker exec -i djangosql mysql -hlocalhost -upet -p < adopet/sql/adopet_db.sql

Confirm connection
docker exec -it djangosql mysql -hlocalhost -upet -p adopet_django

install mysql connector

pip install mysql-connector-python

pip install click

python register_list.py

TO create add_user.py file as example

python add_user.py

python add_user.py "sofy03" "Sofia" "Gonzalez" "sofy0303@gmail.com" "SofyGonzalez03" "1990-03-03" "sofyphoto" 1 3

TO create update_user.py file as example}

python update_user.py 6 None None Martinez None None None None None None


Now create entities with django models

then apply migrations

python manage.py makemigrations
python manage.py migrate

To use default django CRUD super user is necessary

python manage.py createsuperuser (roxana05)

login on http://localhost:8000/admin

To see our model on admin modify admin.py and import there

Pillow dependencie is necessary to use ImageField

pip install Pillow

import os -> settings.py

Generate MEDIA_URL

import on urls.py

python manage.py makemigrations --dry-run --verbosity 3

based on https://testdriven.io/blog/django-custom-user-model/


