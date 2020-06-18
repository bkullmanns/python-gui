import PySimpleGUI as gui 
from listar_produtos import listar_produtos 

gui.theme('DarkAmber')

class mostraProduto:
    def __init__(self):
        conteudo = []
        result = listar_produtos()

        for i, cada, in enumerate(result):
            id = cada[0]
            nome = cada[1]
            preco = cada[2]
            quantidade = cada[3]

            produto = [gui.Text("Id: " + str(id), size=(8,2), font=(18)), gui.Text("Nome: " + nome, size=(8,2), font=(18)), gui.Text("Preço: " + str(preco), font=(18), size=(8,2)), gui.Text("Quantidade: " + str(quantidade), size=(8,2), font=(18))]
            conteudo.append(produto)

        self.tela = gui.Window("lista de produtos").layout(conteudo)
    def show(self):
        self.valores = self.tela.Read()

produto = mostraProduto()
produto.show()
