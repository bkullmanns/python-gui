from Conexao import Conexao
from mostra_produtos import mostra_produtos

def listar_produtos():
    conexao = Conexao()
    conn = conexao.abrir()

    if conn.is_connected():
        cursor = conn.cursor()

        result = mostra_produtos(cursor)
        cursor.close()
        conn.close()
        return result 

listar_produtos()