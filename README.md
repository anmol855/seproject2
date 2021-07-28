#SETUP:
The first thing to do is to clone the repository:

$ git clone https://github.com/anmol855/seproject2.git
$ cd sample-django-app


Create a virtual environment to install dependencies in and activate it:

$ virtualenv2 --no-site-packages env
$ source env/bin/activate


Then install the dependencies:

(env)$ pip install -r requirements.txt


Once pip has finished downloading the dependencies:

(env)$ cd project
(env)$ python manage.py runserver


And finally navigate to http://127.0.0.1:8000/


# STEPS FOR DEPLOYMENT:
Step 1. Create a Procfile in your project root.

Procfile

web: gunicorn project_name.wsgi

Step 2:
pip install gunicorn
pip install django-heroku
pip install whitenoise

pip freeze > requirements.txt

Step 3: create file runtime.txt in project root

python-3.6.4


Step 3. Do this in your app/settings.py

settings.py

ALLOWED_HOSTS = ['seproject20.herokuapp.com']

# Under Middleware
'whitenoise.middleware.WhiteNoiseMiddleware',

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"), )

import django_heroku 
# Then all the way at the bottom of the file
# ... 
django_heroku.settings(locals())


Step 3. Then do this in your command line (bash) and goto your folder.

# login to your heroku
heroku login

git init


# create new app if one doesn't yet exist
heroku create "ar"

# if old app then
heroku git:remote -a ar

# create a new postgres database for your app
heroku addons:create heroku-postgresql:hobby-dev -a "ar"

git add .
git commit -am "first_save"

git push heroku master
 
# migrate your database to the heroku app
heroku run python manage.py collectstatic
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
