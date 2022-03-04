from dao.model.movie_model import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_all_filter_genre(self, uid):
        return self.session.query(Movie).filter(Movie.genre_id == uid)

    def get_all_filter_director(self, uid):
        return self.session.query(Movie).filter(Movie.director_id == uid)

    def get_all_filter_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year)

    def get_one(self, uid):
        return self.session.query(Movie).filter(Movie.id == uid).one()

    def post(self, data):
        movie = Movie(**data)
        with self.session.begin():
            self.session.add(movie)
        return movie

    def put(self, movie):
        with self.session.begin():
            self.session.add(movie)
        return movie

    def delete(self, uid):
        movie = self.get_one(uid)
        with self.session.begin():
            self.session.delete(movie)
