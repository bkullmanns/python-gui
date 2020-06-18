import PySimpleGUI as gui 
from listar_clientes import listar_clientes

gui.theme('DarkAmber')

class mostraCliente:
    def __init__(self):
        conteudo = []
        result = listar_clientes()

        for i, cada, in enumerate(result):
            id = cada[0]
            nome = cada[1]
            email = cada[2]
            genero = cada[3]
            idade = cada[4]
            if email == 1:
                email = "aceita receber email"
            else:
                email = "nao aceita receber email"

            cliente = [gui.Text("Id: " + str(id), size=(8,2), font=(18)), gui.Text("Nome: " + nome, size=(8,2), font=(18)), gui.Text("Email: " + email, size=(15,2), font=(18)), gui.Text("Sexo: " + genero, size=(8,2), font=(18)), gui.Text("Idade: " + str(idade), font=(18), size=(8,2))]
            conteudo.append(cliente)

        self.tela = gui.Window("lista de clientes").layout(conteudo)
    def show(self):
        self.valores = self.tela.Read()

cliente = mostraCliente()
cliente.show()
