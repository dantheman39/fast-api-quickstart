# Quickstart

## Dependencies
If you don't have conda, install miniconda.

```shell
conda env create -f environment.yml
conda activate fast-api-qs
poetry install
```

### Note for how I generated pyproject.toml

I created the conda environment, then ran:

```shell
# Used the same python as I got from conda
poetry init --python=~3.10.4
# Followed their prompts to create pyproject.toml
# Then started adding dependencies
poetry add fastapi
```

## Pre-commit hooks

The hooks are defined in `.pre-commit-config.yml`.

When first setting up run: `pre-commit install`.

Then the next time you commit, the hooks will be installed.

They can be skipped with `git commit --no-verify -m "My messsage"`

Run an individual hook with `pre-commit run <hook-name>`.

By default they only run on staged files. You can pass `--all-files` to
run against all the files.

Sometimes things get out of whack, and pre-commit hooks are tricky to debug.
Run this to reinstall and clear its package cache:

```
pre-commit uninstall
pre-commit clean
pre-commit install
```
