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

COPY theme/static_src/package*.json ./theme/static_src/
COPY theme/static_src/package-lock.json ./theme/static_src/

WORKDIR /theme/static_src/
RUN yarn install

WORKDIR /app/

COPY . /app

RUN python manage.py tailwind build
RUN python manage.py collectstatic --noinput

# ETAPA DE RUNTIME
FROM python:3.11-slim

WORKDIR /app

COPY --from=build /app /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
