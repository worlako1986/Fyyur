import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://worlako:AVNS_N8Bf2y3yVWBRdSTbmag@db-worlako-do-user-12149207-0.b.db.ondigitalocean.com:25060/fyyurapp'
