FROM python:3.14.3-slim-trixie

# * install uv
# * https://docs.astral.sh/uv/guides/integration/docker/#installing-uv
COPY --from=ghcr.io/astral-sh/uv:0.9.8 /uv /uvx /bin/

# install Git to run pre-commit hooks
RUN apt-get update && \
    apt-get install -y --no-install-recommends git

# copy project files (see exlucded files in `.dockerignore`)
COPY . .

# sync packages (without dev)
RUN uv sync
