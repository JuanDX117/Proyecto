# Usa la imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requisitos y instala las dependencias
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido de la carpeta al contenedor
COPY . .

# Expone el puerto donde la aplicación escuchará
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
