# AI Code Generator using OPEN AI & Django Settings File

---
## Starting Django project 
Starting a Django project with name 'codebot' and then navigating to that directory.
In directory we will find 'manage.py' file that will allow us to run all our django commands.

```
django-admin startproject [project_name]
```

## Creating App
To create Django App 'userinterface' within the Django project 'codebot'.

```
python manage.py startapp [app_name]
```

## Migrating the stuff

```
python manage.py migrate
```

## Running the Django Server
To run the Django server on the local host we will use follwing command.

```
pyhon manage.py runserver
```

---

## Adding App to Django setting file
Go to ' codebot > setting.py > in INSTALLED APP section add the app name 

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'userinterface', # Added my app name here
]
```

## Setting up [urls]
Evry Django project comes with 'urls.py' file. We need to create this file in out app folder in my case in 'userinterface' and we add the content of orifional 'urls.py' file in ut file.

```
# My app urls.py file

from django.urls import path

urlpatterns = [ ]
```
After that we need to update the original 'urls.py' folder to include this urls file.

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('userinterface.urls'))
]
```

---

## HOME PAGE

Creating a page in Django is three step process:
- Creating a url in urls.py file 
- Need a view ( Here we will render the hrml file )
- Actual html file

1: Adding the url to the 'urls.py' file

```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home')
]
```

2: Creating a Viwe in 'views.py' file
```
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})
```

3: Creating a html file. But first we need to create a templates folder and then we will create html files in that folder.

