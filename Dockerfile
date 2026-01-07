FROM python:3.13-slim

WORKDIR /code

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-cache

COPY ./app /code/app

RUN mkdir -p /code/uploads

ENV PATH="/code/.venv/bin:$PATH"

EXPOSE 80

CMD ["fastapi", "run", "app/main.py", "--port", "80"]
