# Creating a Django Project
>   django-admin startproject {{ProjectName}}

# Running the project
>   python manage.py runserver

# Creating a new App
>   python manage.py startapp {{APP_NAME}}

# Migrations
>   python manage.py makemigrations
>   python manage.py migrate

# Admin
>   python manage.py createsuperuser

# Creating a model
>   see - HelloDjango/Home/models.py

# Registering a Model
>   Before Migrating, we need to register pur model
>   Register here - HelloDjango/Home/admin.py
>   Copy Name of Home app from - HelloDjango/Home/apps.py
>   add in Project's Settings Installed app
>   Now run Migration commands
>   Check via admin login

