 #Aqui vai ficar todos os models referente ao COFRE_PERMISSOES

from config.database import conectar
from mysql.connector import Error


def create_new_permission(ID_COFRE, ID_USER, ROLE):
    conexao, cursor = conectar()
    if conexao and cursor:
        try:
            sql = "INSERT INTO cofres_permissoes (ID_COFRE_FK, ID_USUARIO_FK, ROLE) VALUES (%s, %s, %s)"
            cursor.execute(sql, (ID_COFRE, ID_USER, ROLE))
            conexao.commit()
 
            return {
                'success': True, 
                'message': f"Permissão de {ROLE} para cofre [{ID_COFRE}] criada para user [{ID_USER}] com sucesso."
            }
        except Error as erro:
            return {
                'success': False, 
                'message': f"Houve um error ao realizar a Query: {erro}"
            }
        
        finally:
            cursor.close()
            conexao.close()

def delete_permission(ID_COFRE, ID_USER):
    conexao, cursor = conectar()
    if conexao and cursor:
        try:
            sql = "DELETE FROM cofres_permissoes WHERE ID_COFRE_FK = %s AND ID_USUARIO_FK = %s"
            cursor.execute(sql, (ID_COFRE, ID_USER))
            conexao.commit()

            print(f"Linhas afetadas: {cursor.rowcount}")

            return {
                'success': True if cursor.rowcount > 0 else False,
                'message': f"Permissão para cofre com [ID: {ID_COFRE}] do user [ID: {ID_USER}] deletado com sucesso." if cursor.rowcount > 0 else f"Nenhuma permissão com cofre [ID: {ID_COFRE}] encontrada. Nada foi deletado"
            }
        
        except Error as erro:
            return {
                    'success': False, 
                    'message': f"Houve um error ao realizar a Query: {erro}"
                }
        
        finally:
            cursor.close()
            conexao.close()