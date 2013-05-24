CREATE TABLE movies (
    movie_id    SERIAL  NOT NULL PRIMARY KEY,
    title       TEXT    NOT NULL,
    genre       TEXT ,
    cover_image BYTEA,
    location    TEXT
);

CREATE TABLE users (
    user_id     SERIAL  NOT NULL PRIMARY KEY,
    name        TEXT    NOT NULL UNIQUE
);

CREATE TABLE votes (
    user_id     INTEGER NOT NULL REFERENCES users(user_id),
    movie_id    INTEGER NOT NULL REFERENCES movies(movie_id),
    CONSTRAINT votes_once UNIQUE (user_id, movie_id)
);

// a different configuration would be with unique vote user:

CREATE TABLE votes (
    user_id     INTEGER NOT NULL REFERENCES users(user_id),
    movie_id    INTEGER NOT NULL REFERENCES movies(movie_id),
    CONSTRAINT votes_once UNIQUE (user_id)
);

INSERT INTO movies ( movie_id, title ) VALUES (1, 'The Hobbit');
INSERT INTO movies ( movie_id, title ) VALUES (2, 'Les Miserables');

INSERT INTO users ( user_id, name ) VALUES (1, 'Joanne');
INSERT INTO users ( user_id, name ) VALUES (2, 'John');
