import mysql.connector
from mysql.connector import Error

#Conexao cria uma instancia com o banco   
#Cursor serve para executar os comandos sql
DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = ""
DB_NAME = "Gerenciador_Senhas"


def conectar():

    try:
        conexao = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS
        )

        if conexao.is_connected():

            cursor = conexao.cursor()
            cursor.execute(f'CREATE DATABASE IF NOT EXISTS {DB_NAME}')

            print('\n> Banco de dados criado com sucesso')

            cursor.close()
            conexao.close()

            conexao = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASS,
                database=DB_NAME
            )
            if conexao.is_connected():
                print("> Banco conectado com sucesso\n")
                cursor = conexao.cursor(dictionary=True)
                return conexao, cursor
               
    except Error as erro:
        print(f"> Houve um error ao tentar se conectar no MySQL: {erro}")
        return None, None
        

