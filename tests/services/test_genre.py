from unittest.mock import MagicMock
import pytest
from dao.model.genre_model import Genre
from dao.genre_dao import GenreDAO
from service.genre_service import GenreService


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    genre_1 = Genre(id=1, name='Test_Genre_1')
    genre_2 = Genre(id=2, name='Test_Genre_2')
    genre_3 = Genre(id=3, name='Test_Genre_3')

    genre_dao.get_one = MagicMock(return_value=genre_1)
    genre_dao.get_all = MagicMock(return_value=[genre_1, genre_2, genre_3])
    genre_dao.post = MagicMock(return_value=Genre(id=4, name='Test_Genre_4'))
    genre_dao.put = MagicMock(return_value=Genre(id=3, name='Test_Genre_3_update'))
    genre_dao.delete = MagicMock()

    return genre_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)

        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genres = self.genre_service.get_all()

        assert len(genres) == 3

    def test_post(self):
        genre_d = {
            "name": "Test_Genre_4"
        }
        genre = self.genre_service.post(genre_d)

        assert genre.id is not None

    def test_put(self):
        genre_d = {
            "name": "Test_Genre_3_update"
        }
        genre = self.genre_service.put(3, genre_d)

        assert genre.id is not None

    def test_delete(self):
        self.genre_service.delete(1)