# db init scripts

As noted in the postgres docker container [docs](https://hub.docker.com/_/postgres),
when the postgres container starts up, if there is no existing database,
it'll run any SQL and bash scripts found in `/docker-entrypoint-initdb.d`. This folder
is mounted into the container by docker compose. To ensure they're run in the
correct order, I've numbered the filenames.

## Why so many small files?

These same SQL statements are re-used by the application, so they're broken
up into more atomic pieces.
