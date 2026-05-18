 #Aqui vai ficar todos os models referente ao COFRE_PERMISSOES

from config.database import conectar
from mysql.connector import Error
import json

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

#Retorna a lista de cofres que o usuario tem permissão
def search_cofres_with_permission(ID_USER):
    conexao, cursor = conectar()
    if conexao and cursor:
        try:
            sql = """ SELECT cofres_permissoes.*, 
                        CONCAT(
                            '[',
                            GROUP_CONCAT(
                                JSON_OBJECT(
                                    'ID_COFRE_PK', cofres.ID_COFRE_PK,
                                    'NOME', cofres.NOME,
                                    'DESCRICAO', cofres.DESCRICAO,
                                    'CREATED_AT', cofres.CREATED_AT,
                                    'TOTAL_SENHAS', ( SELECT COUNT(*) AS COUNT_SENHAS FROM senhas WHERE senhas.ID_COFRE_FK = cofres.ID_COFRE_PK )
                                )
                            ),
                            ']'
                        ) AS COFRES

                        FROM cofres_permissoes
                        JOIN cofres
                        ON cofres_permissoes.ID_COFRE_FK = cofres.ID_COFRE_PK
                        WHERE cofres_permissoes.ID_USUARIO_FK = %s
                        GROUP BY cofres_permissoes.ID_USUARIO_FK
                """
            cursor.execute(sql, (ID_USER, ))

            cofre = cursor.fetchone() 
            cofre['COFRES'] = json.loads(cofre['COFRES'])
            return {
                'success': cofre is not None,
                'message': f"Cofre encontrado" if cofre else f"Cofre não encontrado",
                'data': cofre                
            }
        
        except Error as erro:
            return {
                    'success': False, 
                    'message': f"Houve um error ao realizar a Query: {erro}"
                }
        
        finally:
            cursor.close()
            conexao.close()

#Verifica se tem permissão no cofre
def check_permission_for_cofre(ID_USER, ID_COFRE):
    conexao, cursor = conectar()
    if conexao and cursor:
        try:
            sql = "SELECT * FROM cofres_permissoes WHERE ID_USUARIO_FK=%s AND ID_COFRE_FK=%s"
            cursor.execute(sql, (ID_USER, ID_COFRE))

            permissao = cursor.fetchone()
            cursor.fetchall()

            return {
                'success': permissao is not None,
                'message': f"Permissão encontrado" if permissao else f"Permissão não encontrado",
                'data': permissao                
            }
        
        except Error as erro:
            return {
                'success': False,
                'message': f"Houve um error ao realizar a Query: {erro}",              
            }
        
        finally:
            cursor.close()
            conexao.close() 