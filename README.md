# Site Aviation

Este site tem como objetivo estudos.

É um cadastro e visualização de fotos de Aviões.

Utiliza:
- Python
- Docker
- MySQL
- S3

Em desenvolvimento.


## Variáveis:

.env

```
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=password
MYSQL_DB=aviation_db
AWS_ACCESS_KEY_ID=your-access-key-id
AWS_SECRET_ACCESS_KEY=your-secret-access-key
AWS_BUCKET_NAME=your-bucket-name
```

## Build

```
docker build -t aviation .
```

## Execução:

```
docker run -d -p 5000:5000 -env-file .env aviation
```
