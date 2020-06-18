from Conexao import Conexao

conexao = Conexao()
conn = conexao.abrir()

if conn.is_connected():
    cursor = conn.cursor()
    query = "create table clientes (" 
    query += " id int not null primary key auto_increment,  " 
    query += " nome varchar(100), " 
    query += " aceitaEmail boolean, " 
    query += " sexo varchar(50), "
    query += " idade int) "
    cursor.execute(query)
    
    cursor.close()
    conn.close()

else:
    print("nao conectado")

