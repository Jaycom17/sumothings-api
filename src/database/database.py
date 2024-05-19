from flask_sqlalchemy import SQLAlchemy
from decouple import config

db = SQLAlchemy()

def configure_database(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)