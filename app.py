from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from route.route import main as index_routes


app = Flask(__name__, static_url_path='')

app.register_blueprint(index_routes)
# app.register_blueprint(topic_routes, url_prefix='/topic')


if __name__ == '__main__':

    config = {
        'host': '0.0.0.0',
        'port': 3000,
        'debug': True,
    }
    app.run(**config)
