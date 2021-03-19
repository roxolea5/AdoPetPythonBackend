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
Mofify urls.py on app folder to access corresponding views
```
 from django.urls import path
  from . import views

  urlpatterns = [
 path('', views.index, name="index"),
  ]
```