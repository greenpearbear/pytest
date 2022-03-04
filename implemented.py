from dao.director_dao import DirectorDAO
from dao.genre_dao import GenreDAO
from dao.movie_dao import MovieDAO
from dao.user_dao import UserDAO
from service.director_service import DirectorService
from service.genre_service import GenreService
from service.movie_service import MovieService
from service.user_service import UserService
from service.auth_service import AuthService
from setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

user_dao = UserDAO(db.session)
user_service = UserService(user_dao)

auth_service = AuthService(user_service)
