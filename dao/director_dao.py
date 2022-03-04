from dao.model.director_model import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(Director).filter(Director.id == uid).one()

    def get_all(self):
        return self.session.query(Director).all()

    def post(self, data):
        director = Director(**data)
        with self.session.begin():
            self.session.add(director)
        return director

    def put(self, director):
        with self.session.begin():
            self.session.add(director)
        return director

    def delete(self, uid):
        director = self.get_one(uid)
        with self.session.begin():
            self.session.delete(director)
