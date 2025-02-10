-- 1. Criação do banco de dados
CREATE DATABASE aviation_db;

-- 2. Criação do usuário e definição da senha
CREATE USER 'aviation_user'@'%' IDENTIFIED BY 'password';

-- 3. Conceder permissões ao usuário no banco de dados
GRANT ALL PRIVILEGES ON aviation_db.* TO 'aviation_user'@'%';

-- 4. Atualizar as permissões
FLUSH PRIVILEGES;

-- 5. Criar a tabela de aviões
USE aviation_db;

CREATE TABLE aviões (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(120) NOT NULL,
    prefixo VARCHAR(20) NOT NULL,
    foto_url VARCHAR(255) NOT NULL
);
