from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.movie_views import movies_ns
from views.director_views import directors_ns
from views.genre_views import genres_ns
from views.user_views import users_ns
from views.auth_views import auth_ns


def create_app(config_object: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config_object)
    application.app_context().push()
    configurate_app(application)
    return application


def configurate_app(application: Flask):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(users_ns)
    api.add_namespace(auth_ns)
    create_data(application, db)


def create_data(application, db_create):
    with application.app_context():
        db_create.create_all()


app = create_app(Config())


if __name__ == '__main__':
    app.run()
