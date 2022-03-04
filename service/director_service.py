from dao.director_dao import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def post(self, data):
        return self.dao.post(data)

    def put(self, uid, data):
        director = self.get_one(uid)
        director.id = data.get("id")
        director.name = data.get("name")
        return self.dao.put(director)

    def delete(self, uid):
        return self.dao.delete(uid)
