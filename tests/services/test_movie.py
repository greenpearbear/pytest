from unittest.mock import MagicMock
import pytest
from dao.model.movie_model import Movie
from dao.movie_dao import MovieDAO
from service.movie_service import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    movie_1 = Movie(id=1, title='Test_Movie_1', description='description_1', trailer='trailer_1', year=2011,
                    rating=8.1, genre_id=1, director_id=1)
    movie_2 = Movie(id=2, title='Test_Movie_2', description='description_2', trailer='trailer_2', year=2012,
                    rating=8.2, genre_id=2, director_id=2)
    movie_3 = Movie(id=3, title='Test_Movie_3', description='description_3', trailer='trailer_3', year=2013,
                    rating=8.3, genre_id=3, director_id=3)

    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2, movie_3])

    movie_dao.get_all_filter_year = MagicMock(return_value=movie_1)
    movie_dao.get_all_filter_genre = MagicMock(return_value=movie_2)
    movie_dao.get_all_filter_director = MagicMock(return_value=movie_3)

    movie_dao.post = MagicMock(return_value=Movie(id=4, title='Test_Movie_4', description='description_4',
                                                  trailer='trailer_4', year=2014, rating=8.4,
                                                  genre_id=4, director_id=4))
    movie_dao.put = MagicMock(return_value=Movie(id=3, title='Test_Movie_3_update', description='description_3',
                                                 trailer='trailer_3', year=2013, rating=8.3,
                                                 genre_id=3, director_id=3))
    movie_dao.delete = MagicMock()

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert len(movies) == 3

    def test_get_all_filter_year(self):
        movie = self.movie_service.get_all_filter_year(2011)

        assert movie is not None
        assert movie.id is not None

    def test_get_all_filter_genre(self):
        movie = self.movie_service.get_all_filter_genre(2)

        assert movie is not None
        assert movie.id is not None

    def test_get_all_filter_director(self):
        movie = self.movie_service.get_all_filter_director(3)

        assert movie is not None
        assert movie.id is not None

    def test_post(self):
        movie_d = {
            'id': 4,
            'title': 'Test_Movie_4',
            'description': 'description_4',
            'trailer': 'trailer_4',
            'year': 2014,
            'rating': 8.4,
            'genre_id': 4,
            'director_id': 4
        }
        movie = self.movie_service.post(movie_d)

        assert movie.id is not None

    def test_put(self):
        movie_d = {
            'title': 'Test_Movie_3_update',
            'description': 'description_3',
            'trailer': 'trailer_3',
            'year': 2013,
            'rating': 8.3,
            'genre_id': 3,
            'director_id': 3
        }
        movie = self.movie_service.put(3, movie_d)

        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(1)
