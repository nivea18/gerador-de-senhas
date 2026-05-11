from config.database import conectar
from mysql.connector import Error


def init_db():

    conexao, cursor = conectar()

    if conexao and cursor:
        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios ( 
                                    ID_USER_PK INT AUTO_INCREMENT PRIMARY KEY,
                                    NOME varchar(255) NOT NULL,
                                    EMAIL VARCHAR(255) NOT NULL UNIQUE,
                                    SENHA_HASH VARCHAR(255) NOT NULL,
                                    CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                                    )""")
            
           
        except Error as erro:
            print(f"Error ao tentar criar tabela: {erro}")
