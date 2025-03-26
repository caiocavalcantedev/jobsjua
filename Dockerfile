# Stage de Build
FROM python:3.11-slim AS build

WORKDIR /app

# Instalação do Node.js e Yarn usando corepack
RUN apt-get update && apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_18.x | bash -
RUN apt-get install -y nodejs
RUN corepack enable

COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


COPY theme/static_src/package*.json ./theme/static_src/
COPY theme/static_src/package-lock.json ./theme/static_src/

WORKDIR /theme/static_src/
RUN yarn install

WORKDIR /app/


COPY templates /app/templates
COPY core /app/core
COPY secret /app/secret
COPY jobs /app/jobs
COPY theme/ /app/theme/
COPY manage.py /app/manage.py
COPY requirements.txt /app/requirements.txt
COPY .env /app/.env

RUN python manage.py tailwind build
RUN python manage.py collectstatic --noinput

COPY staticfiles /app/staticfiles

# Stage de Runtime
FROM python:3.11-slim

WORKDIR /app

COPY --from=build /app/staticfiles /app/staticfiles
COPY --from=build /app/core /app/core
COPY --from=build /app/secret /app/secret
COPY --from=build /app/jobs /app/jobs
COPY --from=build /app/theme/ /app/theme/
COPY --from=build /app/manage.py /app/manage.py
COPY --from=build /app/requirements.txt /app/requirements.txt
COPY --from=build /app/.env /app/.env

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000", "--settings", "core.settings.base"]
