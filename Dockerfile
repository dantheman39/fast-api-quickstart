FROM condaforge/mambaforge:4.12.0-0

WORKDIR "/app"

COPY environment.yml ./
RUN mamba env update -n base --file environment.yml --quiet && conda clean -afy

COPY pyproject.toml ./
COPY poetry.lock ./
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction

COPY alembic.ini ./alembic.ini
COPY alembic ./alembic
COPY records ./records

CMD ["python", "-m", "records"]
