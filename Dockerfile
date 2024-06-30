# Use uma imagem base oficial do Python
FROM python:3.12

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo de requisitos para o contêiner
COPY requirements.txt requirements.txt

# Instale as dependências do Python
RUN pip install -r requirements.txt

# Copie o código do aplicativo para o contêiner
COPY . .

# Exponha a porta que o Flask usará
EXPOSE 3000

# Comando para rodar o aplicativo
CMD ["python", "app.py"]
