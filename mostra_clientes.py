def mostra_clientes(cursor):
    cursor.execute("select * from clientes")
    result = cursor.fetchall()

    for cliente in result:
        print(cliente)
    
    return result