 #Aqui vai ficar todos os models referente ao COFRE
import json
from config.database import conectar
from mysql.connector import Error
from models.cofres_permissoes_model import create_new_permission

def create_new_cofre(ID_USER, NOME, DESCRICAO):
    conexao, cursor = conectar()
    if conexao and cursor:
        try:
            sql = "INSERT INTO cofres (NOME, DESCRICAO) VALUES (%s, %s)"
            cursor.execute(sql, (NOME, DESCRICAO))
            conexao.commit()
           
            print(f"Cofre criado com sucesso. ID: {cursor.lastrowid}")

            create_permission = create_new_permission(cursor.lastrowid, ID_USER, "admin")
            print(create_permission)

            return {
                'success': True, 
                'message': f"Cofre {NOME} com ID {cursor.lastrowid} criado com sucesso"
            }
        except Error as erro:
            return {
                'success': False, 
                'message': f"Houve um error ao realizar a Query: {erro}"
            }
        
        finally:
            cursor.close()
            conexao.close()

def delete_cofre(ID_COFRE):
    conexao, cursor = conectar()
    if conexao and cursor:
        try:
            sql = "DELETE FROM cofres WHERE ID_COFRE_PK = %s"
            cursor.execute(sql, (ID_COFRE, ))
            conexao.commit()

            print(f"Linhas afetadas: {cursor.rowcount}")

            return {
                'success': True if cursor.rowcount > 0 else False,
                'message': f"Cofre com ID {ID_COFRE} deletado com sucesso." if cursor.rowcount > 0 else f"Nenhum cofre encontrado com ID {id}. Nada foi deletado"
            }
        
        except Error as erro:
            return {
                    'success': False, 
                    'message': f"Houve um error ao realizar a Query: {erro}"
                }
        
        finally:
            cursor.close()
            conexao.close()

#Retorna os dados do cofre junto com as senhas que tem nele.
def search_all_passwords_in_cofre(ID_COFRE):
    conexao, cursor = conectar()
    if conexao and cursor:
        try:
            sql = """SELECT cofres.*, COUNT(senhas.ID_SENHA_PK) AS TOTAL_SENHAS,
                            CONCAT(
                                '[',
                                    GROUP_CONCAT(
                                        JSON_OBJECT(
                                        'ID_SENHA_PK', senhas.ID_SENHA_PK,
                                        'ID_COFRE_FK', senhas.ID_COFRE_FK,
                                        'NOME', senhas.NOME,
                                        'SENHA_GERADA', senhas.SENHA_GERADA
                                        )
                                    ),
                                ']'
                            ) AS SENHAS
                            
                        FROM `cofres`

                        JOIN senhas 
                        ON cofres.ID_COFRE_PK = senhas.ID_COFRE_FK
                        WHERE cofres.ID_COFRE_PK = %s
                        GROUP BY cofres.ID_COFRE_PK
                """
            cursor.execute(sql, (ID_COFRE, ))

            cofre = cursor.fetchone()   
            cofre['SENHAS'] = json.loads(cofre['SENHAS'])

            return {
                'success': cofre is not None,
                'message': f"Cofre encontrado" if cofre else f"Cofre não encontrado",
                'data': cofre,
                               
            }
        
        except Error as erro:
            return {
                    'success': False, 
                    'message': f"Houve um error ao realizar a Query: {erro}"
                }
        
        finally:
            cursor.close()
            conexao.close()
