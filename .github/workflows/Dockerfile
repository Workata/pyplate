FROM python:3.14.0-slim-trixie

# * install uv
# * https://docs.astral.sh/uv/guides/integration/docker/#installing-uv
COPY --from=ghcr.io/astral-sh/uv:0.9.8 /uv /uvx /bin/

# copy project files (see exlucded files in `.dockerignore`)
COPY . .

# sync packages (without dev)
RUN uv sync
