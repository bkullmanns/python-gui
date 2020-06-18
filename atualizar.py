from Conexao import Conexao
from mostra_produtos import mostra_produtos

conexao = Conexao()
conn = conexao.abrir()

if conn.is_connected():
    cursor = conn.cursor()

    mostra_produtos()

    id = input("Informe o id do produto que voce quer editar: ")
    nome = input("Digite o nome do produto: ")
    preco = input("Preco do produto: ") 
    preco = preco.replace("," , ".")
    quantidade =  input("Quantidade do produto: ") 
    quantidade = quantidade.replace("," , ".")

    query = "UPDATE produtos SET "
    query += " nome = '" + nome + "' , "
    query += " preco = " + preco + " , " 
    query += " quantidade = " + quantidade + " "
    query += " WHERE id = " + id
    cursor.execute( query )
    conn.commit()

    mostra_produtos()

    cursor.close()
    conn.close()