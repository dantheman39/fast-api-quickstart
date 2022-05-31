# Fast-API quickstart

A starter project I made for myself that is complete with .env file, pre-commit hooks,
postgres, Docker, docker-compose, tests, etc.

## Environment variables: .env file

Create a .env file at the topmost part of the repo. See myproject/config.py
for possible values. Note: if running in linux in Docker, I had to set host
to 0.0.0.0 to access the container, and for docker-compose I set DB_HOST to "db".

## Pre-commit hooks

The hooks are defined in `.pre-commit-config.yml`.

When first setting up run: `pre-commit install`.

Then the next time you commit, the hooks will be installed.

They can be skipped with `git commit --no-verify -m "My messsage"`

Run an individual hook with `pre-commit run <hook-name>`.

By default they only run on staged files. You can pass `--all-files` to
run against all the files.

Some hooks will automatically correct errors ("files were modified by this hook").
Simply run your commit command again and those hooks should come back green.

Sometimes things get out of whack, and pre-commit hooks are tricky to debug.
Run this to reinstall and clear its package cache:

```
pre-commit uninstall
pre-commit clean
pre-commit install
```

## Running in docker-compose

To run in docker compose, run `docker-compose up`.

To run tests: `docker-compose server pytest`

## Running in Python

### Dependencies
If you don't have conda, install miniconda, then:

```shell
conda env create -f environment.yml
conda activate fast-api-qs
poetry install
```

### Run the server

`python -m records`

Run tests:

`pytest`


### Create DB tables

I haven't worked in an ORM or anything for this yet, so I'm using asyncpg and writing
queries directly. Run `bash scripts/create_db.sh` to create a new table using docker-compose.
If you're not using docker-compose, you can use the `scripts/create_db.sql` with your
instance of postgres.


## API Docs

With the server running, go to `http://localhost:8000/docs`.

### Note for how I generated pyproject.toml

I created the conda environment, then ran:

```shell
# Used the same python as I got from conda
poetry init --python=~3.10.4
# Followed their prompts to create pyproject.toml
# Then started adding dependencies
poetry add fastapi
poetry add --dev black
# etc...
```
