from Conexao import Conexao
from FormCliente import FormCliente
from Cliente import Cliente

conexao = Conexao()
conn = conexao.abrir()

form = FormCliente()
cliente = form.show()

if conn.is_connected():
    print("Connectado!")

    cursor = conn.cursor()
    query = "INSERT INTO clientes (nome, aceitaEmail, sexo, idade) VALUES ("
    query += " '" +cliente.nome+"' , " +str(cliente.aceitaEmail) + " , '" + cliente.sexo + "' , " + str(cliente.idade) + " )"
    cursor.execute(query)
    conn.commit()
    conn.close()
