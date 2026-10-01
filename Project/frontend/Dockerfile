FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen
COPY . .
ENV PATH="/app/.venv/bin:$PATH"
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]