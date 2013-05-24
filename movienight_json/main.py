"""
Rudimentary JSON service for Movie Night
----------------------------------------

This service is implemented using Bottle and SQLAlchemy. It has three ReST
functions:

/movies    
    - provide a list of all movies.
    
/users
    - provide a list of all users.

/vote/<user_id>/<movie_id>
    - allow a user to vote for a movie, using the IDs.

More functions should be added, for instance:

    - suggesting a new movie
    - deleting an old movie (and probably its votes)
    - nuking everyone's votes from orbit (reset)
    - un-voting a movie

"""
import bottle
from bottle import route, request, response
import sqlalchemy as sql
import sqlalchemy.orm
from model import Movie, User, Vote

# hard-coded database config for now, but it should be in a nice config file.
engine = sql.create_engine("postgresql:///movienight_json")

# connect to the database using magic ponies
db = sql.orm.scoped_session(sql.orm.sessionmaker(autoflush=True, autocommit=True))
db.configure(bind=engine)

# set up the Bottle HTTP request manager
service = bottle.Bottle()
service.DEBUG = True

"""
Get the list of all movies.
"""
@service.route('/')
@service.route('/movies')
def do_movielist():
    response.content_type='application/json'
    movies = db.query(Movie).order_by(Movie.title)
    movielist = []
    for movie in movies:
        movielist.append(movie.json())
    json = '{"movies" : [%s]}' % ','.join(movielist)
    return json

"""
Get the list of all users.
"""
@service.route('/users')
def do_userlist():
    response.content_type='application/json'
    users = db.query(User).order_by(User.name)
    userlist = []
    for user in users:
        userlist.append(user.json())
    json = '{"users" : [%s]}' % ','.join(userlist)
    return json

"""
Get the list of all votes.
"""
@service.route('/votes')
def do_userlist():
    response.content_type='application/json'
    votes = db.query(Vote).order_by(Vote.movie_id)
    votelist = []
    for vote in votes:
        votelist.append(vote.json())
    json = '{"votes" : [%s]}' % ','.join(votelist)
    return json


"""
Submit a vote, one user to one movie. Return whether the vote was cast.
"""
@service.route('/vote/:userid/:movieid', method='GET')
def do_vote(userid, movieid):
    response.content_type='application/json'
    vote = Vote(user_id=userid, movie_id=movieid)
    existing = db.query(Vote).filter_by(user_id=userid).filter_by(movie_id=movieid).first()
    if existing != None:
        return '{"result": "ERROR", "message": "User has already voted for this movie."}'
    else:
        db.add(vote)
        # following line is to try to force the commit
        existing = db.query(Vote).filter_by(user_id=userid).filter_by(movie_id=movieid).first()
        return '{"result": "OK", "message" : "Vote registered."}'

"""
Same functionality as above but using jsonp
"""
@service.route('/votejsonp', method='GET')
def do_votejsonp():
    response.content_type='application/javascript'
    callbackProcess = request.query.callback
    vote = Vote(user_id=request.query.userId, movie_id=request.query.movieId)
    existing = db.query(Vote).filter_by(user_id=request.query.userId).filter_by(movie_id=request.query.movieId).first()

    if existing != None:
        votes = db.query(Vote).order_by(Vote.movie_id)
        votelist = []
        for vote in votes:
            votelist.append(vote.json())
        jsonVotes = '"votes" : [%s]' % ','.join(votelist)
        return callbackProcess + '({"result": "ERROR", "message": "User has already voted for this movie.",' +jsonVotes+'})'
    else:
        db.add(vote)
        
        votes = db.query(Vote).order_by(Vote.movie_id)
        votelist = []
        for vote in votes:
            votelist.append(vote.json())
        jsonVotes = '"votes" : [%s]' % ','.join(votelist)
        
        # following line is to try to force the commit
        existing = db.query(Vote).filter_by(user_id=request.query.userId).filter_by(movie_id=request.query.movieId).first()
        return callbackProcess + '({"result": "OK", "message" : "Vote registered.",' +jsonVotes+'})'


"""
Same functionality as above but using jsonp
"""
@service.route('/modeljsonp', method='GET')
def do_modeljsonp():
    response.content_type='application/javascript'
    callbackProcess = request.query.callback
    users = db.query(User).order_by(User.name)
    userlist = []
    for user in users:
        userlist.append(user.json())
    jsonUsers = '"users" : [%s]' % ','.join(userlist)

    movies = db.query(Movie).order_by(Movie.title)
    movielist = []
    for movie in movies:
        movielist.append(movie.json())
    jsonMovies = '"movies" : [%s]' % ','.join(movielist)

    return callbackProcess + '({' + jsonUsers + ',' + jsonMovies +'})'

# run the HTTP service
bottle.run(service, host='0.0.0.0', port='9980')

