### crypto currencies---django--tracker
schedule authomated binance scrapping and store in a database using celery-beat, django and redis

### get up and running
```
  1. pip install requirements.txt
```
```
  2 - start server. python manage.py runserver
```
```
  3 - make migrations. 
  
        . python manage.py makemigrations 
        
          . python manage.py migrate
```
```
  4 - start celery. celery -A cryptostalker worker --loglevel=info
```
```
  5 - create superuser. python manage.py createsuperuser
```
```
  6 - login to django admin dashboard 
```
