FROM python:3.11-bullseye

WORKDIR /workspace

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/workspace
ENV POETRY_HOME=/opt/poetry

RUN apt-get update && apt-get install -y jq vim \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && curl -sSL https://install.python-poetry.org | python - \
    && cd /usr/local/bin \
    && ln -s /opt/poetry/bin/poetry \
    && poetry config virtualenvs.create false

COPY ./pyproject.toml* ./poetry.lock* ./

RUN poetry install --only main
