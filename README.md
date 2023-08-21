# LagCity Project

Developed by Palas x MOFRAD - 2023

## Setting up the project

in the root dir where the lagcity is located in , make a .env file at fill it as this :
```

SECRET_KEY = 'django-insecure-<your-secret-key>'

MERCHANT_CODE = 'your-merchant-code'

X_SANDBOX = 1 # 0 disable, 1 active

DEBUG = True # whatever you prefer to have it true which means debug in on and your developin
# or set it to False which means the project is on production

```

and after that set up a venv and activate it in the main dir:

```
python -m venv <your-venv-name>
cd <your-venv-name>/Scripts/
activate 

#if youre using windows powershell then run this
Activate.bat
```
after that its time to install libraries needed which include django , Pillow and more...
```
pip3 install -r pkgreq.txt 
```


## Migrations and Migrate
to use db features and models in this repo you need to migrate them , then:
```
#the app name is optional , you can dont use it and still getting all migratios
python manage.py makemigrations <app_name>
python manage.py migrate
```
## Collecting Statics
to use styles in this repo you need to run this commond which collect staticfiles:
```
python manage.py collectstatic
```
and then create super user and probably you're done! ❤️
```
python manage.py createsuperuser
#then enter a username and password , the email is optional !
```
at the end dont forget to setup allauth setting in admin panel .

# Palas x MOFRAD
# star the repo on github | Made by ❤️ 

