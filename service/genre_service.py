from dao.genre_dao import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def post(self, data):
        return self.dao.post(data)

    def put(self, uid, data):
        genre = self.get_one(uid)
        genre.id = data.get("id")
        genre.name = data.get("name")
        return self.dao.put(genre)

    def delete(self, uid):
        return self.dao.delete(uid)
