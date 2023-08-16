# Book Catalog

Simple Book Catalog Website that allows users to browse and explore a collection of books.

## Run the application
    $ python -m venv <virtual env path>
    $ source <virtual env path>/bin/activate
    $ pip install -r requirements/local.txt
    $ createdb book_catalog_db
    $ python manage.py migrate
    $ python manage.py runserver

## Basic Commands

### Setting Up Your Users

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser


## Environment variables

Please make sure you create a `.env` file and write include this variables.

```bash
DJANGO_READ_DOT_ENV_FILE=True
CELERY_BROKER_URL="redis://localhost:6379/0"
```
