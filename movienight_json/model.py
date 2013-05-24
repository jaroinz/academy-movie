import sqlalchemy as sql
import sqlalchemy.orm as orm
import sqlalchemy.types as types
import sqlalchemy.ext.declarative

Table = sql.ext.declarative.declarative_base()

class Movie(Table):
    __tablename__ = 'movies'
    movie_id    = sql.Column(types.Integer, primary_key=True)
    title       = sql.Column(types.Text, nullable=False)
    genre       = sql.Column(types.Text, nullable=False)
    cover_image = sql.Column(types.LargeBinary)
    location    = sql.Column(types.Text)

    def json(self):
        return """{
            "movie_id" : "%s",
            "title"    : "%s",
            "genre"    : "%s",
            "location" : "%s"
        }""" % (self.movie_id, self.title, self.genre, self.location)

class User(Table):
    __tablename__ = 'users'
    user_id     = sql.Column(types.Integer, primary_key=True)
    name        = sql.Column(types.Text, nullable=False, unique=True)

    def json(self):
        return """{
            "user_id"  : "%s",
            "name"     : "%s"
        }""" % (self.user_id, self.name)

class Vote(Table):
    __tablename__ = 'votes'
    user_id     = sql.Column(types.Integer, sql.ForeignKey('users.user_id'), primary_key=True)
    movie_id    = sql.Column(types.Integer, sql.ForeignKey('movies.movie_id'), primary_key=True)

    def json(self):
        return """{
            "user_id"  : "%s",
            "movie_id" : "%s"
        }""" % (self.user_id, self.movie_id)

