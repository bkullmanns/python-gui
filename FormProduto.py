import PySimpleGUI as gui 
from Produto import Produto

gui.theme('DarkAmber')

class FormProduto:

    def __init__(self):
        conteudo = [
            [gui.Text("nome: "), gui.Input()],
            [gui.Text("preço: "), gui.Input(key='txtPreco') ],
            [gui.Text("quantidade: "), gui.Input(key='txtQtd') ],
            [gui.Button("enviar")]
        ]
        self.tela = gui.Window("cadastro produto").layout(conteudo)

    def show(self):
        self.button, self.valores = self.tela.Read()
        prod = Produto()
        prod.nome = self.valores[0]
        preco = self.valores['txtPreco']
        preco = float(preco.replace(",", ".") )
        prod.preco = preco
        qtd = self.valores['txtQtd']
        qtd = float( qtd.replace(",", ".") )
        prod.quantidade = qtd
        return prod