def mostra_produtos(cursor):
    cursor.execute("select * from produtos")
    result = cursor.fetchall()

    for prod in result:
        print(prod)

    return result