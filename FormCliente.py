import PySimpleGUI as gui 
from Cliente import Cliente

gui.theme('DarkAmber')

class FormCliente:
    def __init__(self):
        conteudo = [
            [gui.Text("nome: "), gui.Input(size=(30, 0), key='txtNome') ],
            [gui.Checkbox("aceita receber e-mail", key='aceitaEmail') ],
            [gui.Text("sexo: ")  ], 
            [gui.Radio("Feminino",'sexo', key='feminino'), 
                gui.Radio("masculino", 'sexo', key='masculino'), 
                gui.Radio("não informar", 'sexo', key='naoInformado')  ],
            [gui.Text("idade: ") , gui.Slider(range=(0,150), orientation='h' , key='idade', default_value=18)] ,
            [gui.Button("enviar") ] 
        ]
        self.tela = gui.Window("cadastro de cliente").layout(conteudo)
    def show(self):
        self.button , self.valores = self.tela.Read()
        cliente = Cliente()
        cliente.nome = self.valores['txtNome']
        cliente.aceitaEmail = self.valores['aceitaEmail']
        if  self.valores['feminino'] :
            cliente.sexo = "feminino"
        elif self.valores['masculino']: 
            cliente.sexo = "masculino"
        else:
            cliente.sexo = "não informado"
        cliente.idade = self.valores['idade']
        return cliente

