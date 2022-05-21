FROM python:bullseye

LABEL maintainer="yurinogueira@id.uff.br"
LABEL vendor="Yuri Nogueira"

# Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONHASHSEED random
ENV PYTHONBREAKPOINT ipdb.set_trace

# Pip
ENV PIP_NO_CACHE_DIR off
ENV PIP_DISABLE_PIP_VERSION_CHECK on
ENV PIP_DEFAULT_TIMEOUT 100

# Dependencies
COPY ./requirements.txt .

RUN apt-get update -yq && apt-get install -yq --no-install-recommends gettext && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /usr/src/app

COPY ./ /usr/src/app
