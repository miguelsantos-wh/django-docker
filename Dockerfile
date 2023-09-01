# Usar la imagen base de Python
FROM python:3.6

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requerimientos
COPY requirements.txt .

# Instalar las dependencias
RUN pip install -r requirements.txt

# Copiar el código de la aplicación
COPY pokemones_asyncio/ .

# Exponer el puerto en el que se ejecutará la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
