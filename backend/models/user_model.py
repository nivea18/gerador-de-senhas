#Aqui vai ficar todos os models referente ao USUARIO

from config.database import conectar
from mysql.connector import Error

def create_new_user(NOME, EMAIL, SENHA_HASH):
    conexao, cursor = conectar()
    if conexao and cursor:
        try:
            sql = "INSERT INTO usuarios (NOME, EMAIL, SENHA_HASH) VALUES (%s, %s, %s)"
            cursor.execute(sql, (NOME, EMAIL, SENHA_HASH))
            conexao.commit()

            print(f"User criado com sucesso. ID: {cursor.lastrowid}")
            return {
                'success': True, 
                'message': f"Usuário {cursor.lastrowid} criado com sucesso"
            }
        except Error as erro:
            return {
                'success': False, 
                'message': f"Houve um error ao realizar a Query: {erro}"
            }
        
        finally:
            cursor.close()
            conexao.close()

def delete_user(ID_USER):
    conexao, cursor = conectar()
    if conexao and cursor:
        try:
            sql = "DELETE FROM usuarios WHERE ID_USER_PK = %s"
            cursor.execute(sql, (ID_USER, ))
            conexao.commit()

            print(f"Linhas afetadas: {cursor.rowcount}")

            return {
                'success': True if cursor.rowcount > 0 else False,
                'message': f"Usuário com ID {ID_USER} deletado com sucesso." if cursor.rowcount > 0 else f"Nenhum usuário encontrado com ID {id}. Nada foi deletado"
            }
        
        except Error as erro:
            return {
                    'success': False, 
                    'message': f"Houve um error ao realizar a Query: {erro}"
                }
        
        finally:
            cursor.close()
            conexao.close()

def update_username(ID_USER, NOME):
    conexao, cursor = conectar()
    if conexao and cursor:
        try:
            sql = "UPDATE usuarios SET NOME=%s WHERE ID_USER_PK = %s "
            cursor.execute(sql, (NOME, ID_USER ))
            conexao.commit()

            print(f"Linhas afetadas: {cursor.rowcount}")

            return {
                'success': True if cursor.rowcount > 0 else False,
                'message': f"Usuário foi atualizado." if cursor.rowcount > 0 else f"Nenhum usuário foi atualizado"
            }
        
        except Error as erro:
            return {
                    'success': False, 
                    'message': f"Houve um error ao realizar a Query: {erro}"
                }
        
        finally:
            cursor.close()
            conexao.close()

def search_user_for_email(EMAIL):
    conexao, cursor = conectar()
    if conexao and cursor:
        try:
            sql = "SELECT * FROM usuarios WHERE email = %s"
            cursor.execute(sql, (EMAIL, ))

            usuario = cursor.fetchone()

            return {
                'success': usuario is not None,
                'message': f"Usuário encontrado" if usuario else f"Usuário não encontrado",
                'data': usuario                
            }
            
        except Error as erro:
            return {
                'success': False,
                'message': f"Houve um error ao realizar a Query: {erro}",              
            }
        
        finally:
            cursor.close()
            conexao.close()

def search_user_for_id(ID_USER):
    conexao, cursor = conectar()
    if conexao and cursor:
        try:
            sql = "SELECT * FROM usuarios WHERE ID_USER_PK = %s"
            cursor.execute(sql, (ID_USER, ))

            usuario = cursor.fetchone()

            return {
                'success': usuario is not None,
                'message': f"Usuário encontrado" if usuario else f"Usuário não encontrado",
                'data': usuario                
            }
        
        except Error as erro:
            return {
                'success': False,
                'message': f"Houve um error ao realizar a Query: {erro}",              
            }
        
        finally:
            cursor.close()
            conexao.close()