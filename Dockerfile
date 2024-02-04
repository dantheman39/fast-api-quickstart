FROM mambaorg/micromamba:bullseye

# Needed for asyncpg
USER root
RUN apt-get update && apt-get install -y gcc
USER $MAMBA_USER

WORKDIR "/app"

COPY --chown=$MAMBA_USER:$MAMBA_USER environment.yml /tmp/environment.yml
RUN micromamba install -y -n base -f /tmp/environment.yml && \
    micromamba clean --all --yes


COPY pyproject.toml ./
COPY poetry.lock ./
RUN micromamba run poetry config virtualenvs.create false \
    && micromamba run poetry install --no-dev --no-interaction

COPY records ./records

CMD ["python", "-m", "records"]
