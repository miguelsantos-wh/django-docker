# Imagen base de Python
FROM python:2.7

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de tu proyecto al contenedor
COPY . /app

# Instalar las dependencias del proyecto
RUN pip install -r requirements.txt

# Exponer el puerto que utiliza tu aplicación de Django (por ejemplo, 8000)
EXPOSE 8000

# Comando para ejecutar tu aplicación de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
