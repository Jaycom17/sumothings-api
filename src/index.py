from flask import Flask
from config.config import config
from database.database import configure_database

# Routes
from routes.DealersRoutes import setupRoutesDealer

app = Flask(__name__)


def init_app(config):
    # Configuration
    app.config.from_object(config)

    configure_database(app)
    setupRoutesDealer(app)

    return app

configuration = config['development']
app = init_app(configuration)

if __name__ == '__main__':
    app.run()