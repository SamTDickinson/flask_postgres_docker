# Boilerplate project template



Project setup for a Flask app with PostgresSQL running in Docker


##Installing Requirements:

Dev:

```css
 pip install -r requirements/development.txt
```

Testing:

```css
 pip install -r requirements/testing.txt
```

Production:

```css
 pip install -r requirements/production.txt

 pip install -r requirements.txt
```


## Running the application:

From project root run:

Dev:

``` css 
FLASK_CONFIG="development" flask run 
```
or
``` css
python manage.py flask run
```

Testing:

``` css 
FLASK_CONFIG="development" flask run 
```

## Building the application:

Dev: 

```css
 FLASK_ENV="development" FLASK_CONFIG="development" docker-compose -f docker/development.yml build web
```


## Running application through Docker
Dev: 

```css
 FLASK_ENV="development" FLASK_CONFIG="development" docker-compose -f docker/development.yml up
```

or

```css
python ./manage.py compose up -d
```


## Creating and Upgrading Databse:

```css
python ./manage.py flask db migrate

python ./manage.py flask db upgrade
```


## Running tests:

```css
 python ./manage.py test
```

## First time running:
If this is the first time to spin up the environment you have to create the application database and
initialise the migrations
```css
 python ./manage.py create-initial-db
```


## Connect to the Postgres Docker image

```css
python ./manage.py compose exec db psql -U postgres 
```

##### Connect to database:

```css
\c application
```

##### List tables:
```css
\dt
```

##### Query tables:
```css
select * from alembic_version;
```

##### Describe tables:
```css
\d users
```