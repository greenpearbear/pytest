from dao.model.genre_model import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(Genre).filter(Genre.id == uid).one()

    def get_all(self):
        return self.session.query(Genre).all()

    def post(self, data):
        genre = Genre(**data)
        with self.session.begin():
            self.session.add(genre)
        return genre

    def put(self, genre):
        with self.session.begin():
            self.session.add(genre)
        return genre

    def delete(self, uid):
        genre = self.get_one(uid)
        with self.session.begin():
            self.session.delete(genre)
