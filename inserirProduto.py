from Conexao import Conexao 
from FormProduto import FormProduto
from Produto import Produto

conexao = Conexao()
conn = conexao.abrir()

form = FormProduto()
produto = form.show()

if conn.is_connected():
    print("Conectado!")

    cursor = conn.cursor()
    query = "INSERT INTO produtos (nome, preco , quantidade) VALUES ("
    query += " '" +produto.nome+"' , " +str(produto.preco) + " , " + str(produto.quantidade) + " )"

    cursor.execute(query)
    conn.commit()
    conn.close()
