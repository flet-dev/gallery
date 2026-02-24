FROM python:3.10-slim

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV UV_PYTHON_DOWNLOADS=never
ENV UV_LINK_MODE=copy

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project --python /usr/local/bin/python

COPY . .
RUN uv sync --frozen --no-dev --python /usr/local/bin/python

EXPOSE 8080

CMD ["/app/.venv/bin/python", "src/main.py"]
