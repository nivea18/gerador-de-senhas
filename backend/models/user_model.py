#Aqui vai ficar todos os models referente ao USUARIO

from config.database import conectar
from mysql.connector import Error

def search_user_for_email(email):
    conexao, cursor = conectar()
    if conexao and cursor:
        try:
            sql = "SELECT * FROM usuarios WHERE email = %s"
            cursor.execute(sql, (email, ))

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

def search_user_for_id(id):
    conexao, cursor = conectar()
    if conexao and cursor:
        try:
            sql = "SELECT * FROM usuarios WHERE ID_USER_PK = %s"
            cursor.execute(sql, (id, ))

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

def create_new_user(dados):
    conexao, cursor = conectar()
    if conexao and cursor:
        try:
            sql = "INSERT INTO usuarios (NOME, EMAIL, SENHA_HASH) VALUES (%s, %s, %s)"
            cursor.execute(sql, (dados["nome"], dados["email"], dados["senha_hash"]))
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

def delete_user(id):
    conexao, cursor = conectar()
    if conexao and cursor:
        try:
            sql = "DELETE FROM usuarios WHERE ID_USER_PK = %s"
            cursor.execute(sql, (id, ))
            conexao.commit()

            print(f"Linhas afetadas: {cursor.rowcount}")

            return {
                'success': True if cursor.rowcount > 0 else False,
                'message': f"Usuário com ID {id} deletado com sucesso." if cursor.rowcount > 0 else f"Nenhum usuário encontrado com ID {id}. Nada foi deletado"
            }
        
        except Error as erro:
            return {
                    'success': False, 
                    'message': f"Houve um error ao realizar a Query: {erro}"
                }
        
        finally:
            cursor.close()
            conexao.close()

def update_username(id, nome):
    conexao, cursor = conectar()
    if conexao and cursor:
        try:
            sql = "UPDATE usuarios SET NOME=%s WHERE ID_USER_PK = %s "
            cursor.execute(sql, (nome, id ))
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