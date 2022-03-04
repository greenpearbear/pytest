from unittest.mock import MagicMock
import pytest
from dao.model.director_model import Director
from dao.director_dao import DirectorDAO
from service.director_service import DirectorService


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    director_1 = Director(id=1, name='Test_Director_1')
    director_2 = Director(id=2, name='Test_Director_2')
    director_3 = Director(id=3, name='Test_Director_3')

    director_dao.get_one = MagicMock(return_value=director_1)
    director_dao.get_all = MagicMock(return_value=[director_1, director_2, director_3])
    director_dao.post = MagicMock(return_value=Director(id=4, name='Test_Director_4'))
    director_dao.put = MagicMock(return_value=Director(id=3, name='Test_Director_3_update'))
    director_dao.delete = MagicMock()

    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert len(directors) == 3

    def test_post(self):
        director_d = {
            "name": "Test_Director_4"
        }
        director = self.director_service.post(director_d)

        assert director.id is not None

    def test_put(self):
        director_d = {
            "name": "Test_Director_3_update"
        }
        director = self.director_service.put(3, director_d)

        assert director.id is not None

    def test_delete(self):
        self.director_service.delete(1)
