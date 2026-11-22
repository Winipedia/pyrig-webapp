FROM python:3.15-slim
WORKDIR /pyrig-webapp

COPY --from=docker.io/oven/bun:slim /usr/local/bin/bun /usr/local/bin/bun
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
COPY LICENSE README.md pyproject.toml rxconfig.py uv.lock ./
COPY src/pyrig_webapp src/pyrig_webapp

ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1

RUN uv sync --no-group=dev

RUN useradd --create-home --uid=1000 appuser \
    && chown appuser:appuser .
USER 1000

ENTRYPOINT ["uv", "run", "--no-sync", "reflex", "run", "--env=prod"]
