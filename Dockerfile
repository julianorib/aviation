# Usando a imagem oficial do Python
FROM python:3.10-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia os arquivos de dependências e instala as dependências
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia o código da aplicação para dentro do container
COPY . .

# Define a variável de ambiente Flask para rodar em modo de desenvolvimento
ENV FLASK_ENV=development

# Expõe a porta que o Flask vai rodar
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["flask", "run", "--host=0.0.0.0"]
