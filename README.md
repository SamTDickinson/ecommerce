# ecommerce

# Setup

## Create a vitual environment:
```text
python -m venv venv
```

## Activate your virtual environment
macos
```text
source venv/bin/activate
```

Windows
```text
source venv/Scripts/activate
```

## Deactivate virtual environment
```text
deactivate
```

## Install production requirements
``` 
pip install -r requirements.txt
```

## Install Development requirements
``` 
pip install -r requirements-dev.txt
```

## Starting the applicaion
```text
cd src

python manage.py runserver

application will run locallay on
http://127.0.0.1
```

## Setting up a superuser

```text
python manage.py createsuperuser

add username
add email address
add password
verify password

Access Admin panel:
http://127.0.0.1/admin
```