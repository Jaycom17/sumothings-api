from decouple import config
from flask_mysqldb import MySQL

mysql = MySQL()

def configure_database(app):

    print(f"MYSQL_HOST: {config('MYSQL_HOST', default='localhost')}")
    print(f"MYSQL_USER: {config('MYSQL_USER')}")
    print(f"MYSQL_PASSWORD: {config('MYSQL_PASSWORD')}")
    print(f"MYSQL_DB: {config('MYSQL_DB')}")

    app.config['MYSQL_DATABASE_HOST'] = config('MYSQL_HOST', default='localhost')
    app.config['MYSQL_DATABASE_USER'] = config('MYSQL_USER')
    app.config['MYSQL_DATABASE_PASSWORD'] = config('MYSQL_PASSWORD')
    app.config['MYSQL_DATABASE_DB'] = config('MYSQL_DB')

    mysql.init_app(app)

def get_db():
    return mysql.connection