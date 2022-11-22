# 

# Install Commands
1. pip(3) install -r requirements.txt
2. flask run
3. flask --debug run
4. pytest
5. flask db upgrade

## Fix Mac Permission Error after docker compose up --build  command - Run these on the terminal 
* chmod +x ./development.sh
* chmod +x ./production.sh


# Readings
* https://hackersandslackers.com/flask-routes
* https://zetcode.com/python/faker/


# Docker Commands
* docker compose up --build <- builds the image in development mode and shares the volume
* docker compose up <- runs the previously built image without redoing the build process
* docker build -t myapp . <- builds it to run with gunicorn in production mode
* docker run -itp 80:8080 myapp <- runs the website / flask in console output mode
* docker exec -it <containerid> bash <- logs into container (replace <containerid> with the container id)
* docker run -itp 80:8080 myapp pytest <-runs pytest in the container image

# Flask Migrate / Alembic Commands - Must delete the migrations and instance folder / database.  These will reset it 
* flask db init <-initializes migrations (don't need to do this the project has its first migration)
* flask db migrate -m "Initial migration." <-change the message to whatever describes the schema change
* flask db upgrade <- applies the migrations

# Libraries
* https://flask.palletsprojects.com/en/2.2.x/
* https://www.sqlalchemy.org/
* https://alembic.sqlalchemy.org/en/latest/
* https://github.com/miguelgrinberg/flask-migrate
