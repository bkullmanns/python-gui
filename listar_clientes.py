from Conexao import Conexao
from mostra_clientes import mostra_clientes

def listar_clientes():
    conexao = Conexao()
    conn = conexao.abrir()

    if conn.is_connected():
        cursor = conn.cursor()

        result = mostra_clientes(cursor)
        cursor.close()
        conn.close()
        return result     

listar_clientes()