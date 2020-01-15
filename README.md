# testing production wagtail issue - docker

docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml run web /usr/local/bin/python manage.py migrate

## Issue

DEBUG: 'true' in docker-compose.prod.yml
http://0.0.0.0 works
http://0.0.0.0/admin works


DEBUG: 'false' in docker-compose.prod.yml
http://0.0.0.0 works
http://0.0.0.0/admin ERROR:

Internal server error
Sorry, there seems to be an error. Please try again soon.

## tried

1)

Tried to make a 'forgiving' collectstatic with

#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
STATICFILES_STORAGE = 'website.forgiving_collect.ForgivingManifestStaticFilesStorage'
for more info: https://timonweb.com/tutorials/make-djangos-collectstatic-command-forgiving/

docker-compose -f docker-compose.prod.yml run web /usr/local/bin/python manage.py collectstatic

Also, collectstatic should not give internal server error anyway, right?
