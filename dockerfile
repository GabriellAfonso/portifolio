FROM python:3.12.6-alpine3.20
LABEL maintainer="gabrieldelimaafonso@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

copy django /django
copy scripts /scripts

WORKDIR /django

RUN chmod +x /scripts/commands.sh && \
    chmod -R a+rw /django


EXPOSE 8000

RUN python -m venv /venv && \
  /venv/bin/pip install --upgrade pip && \
  /venv/bin/pip install -r /django/requirements.txt && \
  adduser --disabled-password --no-create-home duser

ENV PATH="/scripts:/venv/bin:${PATH}"

CMD ["commands.sh"]