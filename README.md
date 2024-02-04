# Fast-API quickstart

A starter project I made for myself that is complete with a FastAPI service, Postgres, tests,
API documentation, docker compose, linting, type checking, and pre-commit hooks.

## Quickstart, using docker compose

See below for more detailed info, this section aims to get you up and running quickly.

### Running

Create an empty `.env` file: `touch .env`, then `docker compose up` (or `docker-compose up`
if your version of Docker is not super recent).

That's it!

If you already have another instance of postgres running on port 5432, add `DB_PORT=5433`
to your `.env` file and try again. Add `DEBUG=true` if you want your code to reload
on changes.

### API Docs

With the server running, go to `http://localhost:8000/docs`.

You can send requests from the docs, which is nice!

### Tests

Run `./scripts/tests`.

## Slow start, using local Python and dockerized Postgres

My preferred way to develop locally is to run dependencies like Postgres in Docker,
but run the main Python program locally. You can run just the dependencies using
the helper script `./scripts/deps up`.

### The database

This has a dockerized Postgres database, whose data is persisted in a docker-managed volume.
If you want to run only the DB in docker, run `./scripts/deps up`.

On startup if no database is found, the container will run the scripts found in `/sql`
to populate the database.

If you want to delete the database, just run `docker compose down --volumes`.

Regarding the helper script `./scripts/deps`, all that is is a shortcut to run using only the `docker-compose.yml`
file, deliberately excluding `docker-compose.override.yml` which would otherwise be included by default.
You can use any `docker compose` command with it. For example, if the db was already running and you wanted
to get into a `psql` console, you could run `./scripts/deps exec db psql -U postgres -d records`.

### Local Python

My preferred way to set up Python locally for a situation like this, is to manage virtual
environments with `conda` (or `mamba`, which is loads faster), and install most packages with
`poetry`.

#### Set up virtual environment

If you don't already have strong opinions:

1. Install [micromamba](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html)
2. Create the environment with `micromamba create -f environment.yml`
3. Activate the environment with `micromamba activate fast-api-quickstart`

#### Install remaining packages

With your virtual environment activated: `poetry install`

#### Update .env

If you've elected to run local Python + dockerized db, update these fields in your `.env` file:

```dotenv
DB_USER=postgres
DB_PASSWORD=awesomeness
DB_HOST=localhost
```

These match the values used in the `docker-compose.yml`, except we set the host to be
`localhost` instead of using docker's networking (`db`).

To see what environment variables are available, look at `records/config.py`.

#### Run the server

After the prior setup above, run `python -m records`.

#### Running tests

`pytest`

## Pre-commit hooks

This repo runs the `flake8` linter, the `black` formatter, and the type checker
`mypy` using `pre-commit` hooks. These hooks are defined in `.pre-commit-config.yml`.

When first setting up run: `pre-commit install`.

Then the next time you commit, the hooks will be installed.

They can be skipped with `git commit --no-verify -m "My messsage"`

Run an individual hook with `pre-commit run <hook-name>`.

By default they only run on staged files. You can pass `--all-files` to
run against all the files.

Some hooks will automatically correct errors ("files were modified by this hook").
Simply run your commit command again and those hooks should come back green.

Sometimes things get out of whack, and pre-commit hooks are tricky to debug.
You could run this to reinstall and clear its package cache:

```
pre-commit uninstall
pre-commit clean
pre-commit install
```

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
