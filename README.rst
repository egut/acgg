Welcome to acgg homepage
========================


DEV. SETUP
----------

Need in system:

* sudo pip install virtualenv

Run: 

1) virtualenv tmp_acgg
2) source venv/bin/activate
3) pip install -r requirements.txt
4) See to it that DEBUG = True in acgg/settings.py
5) ./manage.py syncdb --all
6) ./manage.py migrate --fake
7) DEVELOP!

Deactivte:

Run: deactivate


SETUP
-----


Run:

1) sudo pip install -r requirements.txt
2) ./manage.py syncdb --all
3) ./manage.py migrate --fake


CONFIUGRE
---------

Add social auth codes for Google and Facebook you need both client_id and secret 
see: https://github.com/pennersr/django-allauth#providers

This is controlled by what apps are in INSTALLED_APPS. Look for: allauth.socialaccount.providers.<something>

