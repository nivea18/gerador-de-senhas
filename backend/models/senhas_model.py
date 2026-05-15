#Aqui vai ficar todos os models referente ao SENHAS

from config.database import conectar
from mysql.connector import Error

def create_password(ID_COFRE, NOME, SENHA_GERADA):
    conexao, cursor = conectar()
    if conexao and cursor:
        try:
            sql = "INSERT INTO senhas (ID_COFRE_FK, NOME, SENHA_GERADA) VALUES (%s, %s, %s)"
            cursor.execute(sql, (ID_COFRE, NOME, SENHA_GERADA))
            conexao.commit()

            return {
                'success': True, 
                'message': f"Senha [{SENHA_GERADA}] criado para o cofre [{ID_COFRE}] criado com sucesso"
            }
        except Error as erro:
            return {
                'success': False, 
                'message': f"Houve um error ao realizar a Query: {erro}"
            }
        
        finally:
            cursor.close()
            conexao.close()    

def search_password_in_cofre(ID_COFRE):
    conexao, cursor = conectar()
    if conexao and cursor:

        try:
            sql = "SELECT * FROM senhas WHERE ID_COFRE_FK = %s"
            cursor.execute(sql, (ID_COFRE, ))

            senhas = cursor.fetchall()

            return {
                'success': senhas is not None,
                'message': f"Senhas encontradas" if senhas else f"Senhas não encontradas",
                'data': senhas                
            }
        except Error as erro:
            return {
                'success': False,
                'message': f"Houve um error ao realizar a Query: {erro}",              
            }
        
        finally:
            cursor.close()
            conexao.close()  

def delete_password(ID_SENHA_PK):
    conexao, cursor = conectar()
    if conexao and cursor:
        try:
            sql = "DELETE FROM senhas WHERE ID_SENHA_PK = %s"
            cursor.execute(sql, (ID_SENHA_PK, ))
            conexao.commit()

            print(f"Linhas afetadas: {cursor.rowcount}")

            return {
                'success': True if cursor.rowcount > 0 else False,
                'message': f"Senha com ID {ID_SENHA_PK} deletada com sucesso." if cursor.rowcount > 0 else f"Nenhum senha encontrada com ID {ID_SENHA_PK}. Nada foi deletado"
            }
        
        except Error as erro:
            return {
                    'success': False, 
                    'message': f"Houve um error ao realizar a Query: {erro}"
                }
        
        finally:
            cursor.close()
            conexao.close()
