from Conexao import Conexao 

conexao = Conexao()
conn = conexao.abrir()

if conn.is_connected():
    cursor = conn.cursor()

    query = "create table produtos (" 
    query += " id int not null primary key auto_increment,  " 
    query += " nome varchar(50),  " 
    query += " preco double,       " 
    query += " quantidade double) "
    cursor.execute(query)

    cursor.close()
    conn.close()

else:
    print("nao conectado")

