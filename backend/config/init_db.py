from config.database import conectar
from mysql.connector import Error


def init_db():

    conexao, cursor = conectar()

    if conexao and cursor:

        #CRIAÇÃO DA TABELA USUARIOS
        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios ( 
                                    ID_USER_PK INT AUTO_INCREMENT PRIMARY KEY,
                                    NOME VARCHAR(255) NOT NULL,
                                    EMAIL VARCHAR(255) NOT NULL UNIQUE,
                                    SENHA_HASH VARCHAR(255) NOT NULL,
                                    CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                                    )""")
            
        except Error as erro:
            print(f"Error ao tentar criar tabela USUARIOS: {erro}")

        #CRIAÇÃO DA TABELA COFRES
        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS cofres ( 
                                    ID_COFRE_PK INT AUTO_INCREMENT PRIMARY KEY,
                                    NOME VARCHAR(255) NOT NULL,
                                    DESCRICAO VARCHAR(255),
                                    CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                                    )""")

        except Error as erro:
            print(f"Error ao tentar criar tabela COFRES: {erro}")     
        
        #CRIAÇÃO DA TABELA COFRES_PERMISSOES
        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS cofres_permissoes ( 
                                    ID_PERMISSAO_PK INT AUTO_INCREMENT PRIMARY KEY,
                                    ID_COFRE_FK INT,
                                    ID_USUARIO_FK INT,
                                    ROLE ENUM('admin', 'editor', 'membro') DEFAULT 'membro',
                                    CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                           
                                    FOREIGN KEY (ID_COFRE_FK) REFERENCES cofres(ID_COFRE_PK),
                                    FOREIGN KEY (ID_USUARIO_FK) REFERENCES usuarios(ID_USER_PK)
                                    )""")

        except Error as erro:
            print(f"Error ao tentar criar tabela COFRES_PERMISSOES: {erro}")  

        #CRIAÇÃO TABELA SENHAS
        try:
           cursor.execute("""CREATE TABLE IF NOT EXISTS senhas ( 
                                    ID_SENHA_PK INT AUTO_INCREMENT PRIMARY KEY,
                                    ID_COFRE_FK INT,
                                    NOME VARCHAR(255) NOT NULL, 
                                    SENHA_GERADA VARCHAR(255) NOT NULL,
                                    FOREIGN KEY (ID_COFRE_FK) REFERENCES cofres(ID_COFRE_PK)
                                    )""") 

        except Error as erro:
            print(f"Error ao tentar criar tabela SENHAS: {erro}")  
