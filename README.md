# pokemones-asyncio

## Paso 1: Hacer git clone
    git clone https://github.com/miguelsantos-wh/django-docker.git

## Paso 2: Crear entorno
    mkvirtualenv venv -p=3.6
    o 
    mkvirtualenv venv /path/pyhton3.6/
    o 
    virtualenv venv -p=3.6
    o
    mkvirtualenv --python=`which python3.8` venv

## Paso 3: Iniciar entorno
    source venv/bin/activate

#### Confirmar que sea en python 3.6
    python -V

## Paso 4: Parar Nginx
    sudo systemctl stop nginx.service

## Paso 5: Correr compose
    sudo docker-compose up --build

## Paso 6: Verificar que corra el proyecto
    localhost
