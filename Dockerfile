# Use a imagem base Python
FROM python:3.11-slim

# Instala o FFmpeg
RUN apt-get update && apt-get install -y ffmpeg

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

RUN pip install Flask 

# Instala as dependências do aplicativo
#RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos para o diretório de trabalho
COPY . .

# Expõe a porta 9090
EXPOSE 9090

# Comando para iniciar o aplicativo quando o contêiner for executado
CMD ["python", "app.py"]