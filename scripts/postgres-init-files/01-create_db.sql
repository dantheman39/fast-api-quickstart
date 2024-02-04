DROP TABLE IF EXISTS artists CASCADE;
DROP TABLE IF EXISTS albums;

CREATE TABLE artists(
    id INT GENERATED ALWAYS AS IDENTITY,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE albums(
    id INT GENERATED ALWAYS AS IDENTITY,
    name VARCHAR(255) NOT NULL,
    artist_id INT,
    PRIMARY KEY(id),
    CONSTRAINT fk_artist
      FOREIGN KEY(artist_id)
        REFERENCES artists(id)
);

CREATE INDEX frn_albums_artist_id ON albums(artist_id);
