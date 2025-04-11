# ETAPA DE BUILD
FROM python:3.11-slim AS build

WORKDIR /app

RUN apt-get update && apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_18.x | bash -
RUN apt-get install -y nodejs
RUN npm install -g yarn

COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY .env-example /app/.env-example

COPY theme/static_src/package*.json ./theme/static_src/
COPY theme/static_src/package-lock.json ./theme/static_src/

WORKDIR /theme/static_src/
RUN yarn install

WORKDIR /app/

COPY manage.py /app/
COPY .env-example /app/
COPY create_superuser.py /app/

COPY static /app/static/
COPY core /app/core/
COPY jobs /app/jobs/
COPY secret /app/secret/
COPY theme /app/theme/
COPY templates /app/templates/

# Criar um .env temporário para fazer o build
RUN cp .env-example .env

RUN python manage.py tailwind build
RUN python manage.py collectstatic --noinput

# Remover o .env temporário 
RUN rm .env

# ETAPA DE RUNTIME
FROM python:3.11-slim

WORKDIR /app

# Copia Arquivos individuais da fase de build para o runtime
COPY --from=build /app/requirements.txt /app/
COPY --from=build /app/manage.py /app/
COPY --from=build /app/create_superuser.py /app/
COPY --from=build /app/.env-example /app/

# Pastas específicas da fase de build para o runtime
COPY --from=build /app/core /app/core/
COPY --from=build /app/jobs /app/jobs/
COPY --from=build /app/secret /app/secret/
COPY --from=build /app/theme /app/theme/
COPY --from=build /app/templates /app/templates/

# Arquivos estáticos da fase de build para o runtime
COPY --from=build /app/static /app/static/
COPY --from=build /app/staticfiles /app/staticfiles/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
