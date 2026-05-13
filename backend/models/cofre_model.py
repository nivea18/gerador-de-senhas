 #Aqui vai ficar todos os models referente ao COFRE

from config.database import conectar
from mysql.connector import Error
from models.cofres_permissoes_model import create_new_permission

def create_new_cofre(dados):
    conexao, cursor = conectar()
    if conexao and cursor:
        try:
            sql = "INSERT INTO cofres (NOME, DESCRICAO) VALUES (%s, %s)"
            cursor.execute(sql, (dados["nome"], dados["descricao"]))
            conexao.commit()
           
            print(f"Cofre criado com sucesso. ID: {cursor.lastrowid}")

            create_permission = create_new_permission(cursor.lastrowid, dados['id_user'], "admin")
            print(create_permission)

            return {
                'success': True, 
                'message': f"Cofre {dados['nome']} com ID {cursor.lastrowid} criado com sucesso"
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

def search_all_passwords_in_cofre(ID_COFRE):
    conexao, cursor = conectar()
    if conexao and cursor:
        try:
            sql = """SELECT cofres.*, 
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




""" SELECT cofres.*, cofres_permissoes.* FROM cofres
JOIN cofres_permissoes
ON cofres.ID_COFRE_PK = cofres_permissoes.ID_COFRE_FK
WHERE cofres_permissoes.    =1 """