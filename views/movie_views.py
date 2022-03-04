from flask_restx import Resource, Namespace
from flask import request
from dao.model.movie_model import MovieSchema
from implemented import movie_service
from helpers.decorators import auth_required, admin_required

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    @auth_required
    def get(self):
        genre_id = request.args.get('genre_id')
        director_id = request.args.get('director_id')
        year = request.args.get('year')
        if genre_id:
            all_movies_filter_genre = movie_service.get_all_filter_genre(genre_id)
            return MovieSchema(many=True).dump(all_movies_filter_genre), 200
        if director_id:
            all_movies_filter_director = movie_service.get_all_filter_director(director_id)
            return MovieSchema(many=True).dump(all_movies_filter_director), 200
        if year:
            all_movies_filter_year = movie_service.get_all_filter_year(year)
            return MovieSchema(many=True).dump(all_movies_filter_year), 200
        all_movies = movie_service.get_all()
        return MovieSchema(many=True).dump(all_movies), 200

    @admin_required
    def post(self):
        req_json = request.json
        new_movie = movie_service.post(req_json)
        return "", 201, {"location": f"/movies/{new_movie.id}"}


@movies_ns.route('/<int:uid>')
class MovieView(Resource):
    @auth_required
    def get(self, uid: int):
        try:
            movie = movie_service.get_one(uid)
            return MovieSchema().dump(movie), 200
        except Exception as e:
            return str(e), 404

    @admin_required
    def put(self, uid: int):
        try:
            req_json = request.json
            movie = movie_service.put(uid, req_json)
            return MovieSchema().dump(movie), 200
        except Exception as e:
            return str(e), 404

    @admin_required
    def delete(self, uid: int):
        try:
            movie_service.delete(uid)
            return "", 204
        except Exception as e:
            return str(e), 404
