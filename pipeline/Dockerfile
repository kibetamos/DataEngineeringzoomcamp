FROM python:3.13.11-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /code


# Add virtual environment to PATH so we can use installed packages
ENV PATH="/code/.venv/bin:$PATH"


# RUN pip install pandas pyarrow
COPY pyproject.toml .python-version uv.lock ./


RUN uv sync --locked

# COPY pipeline.py .
COPY ingest_data.py .

ENTRYPOINT ["python", "ingest_data.py" ]

