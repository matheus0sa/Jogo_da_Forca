import situacao
import palavras
import random

status = situacao.situacao
palavra = random.choice(palavras.palavras)


class Forca():
    def __init__(self, palavra):
        self.chave = palavra
        self.acertos = []
        self.erros = 0
        self.mostrar = ""


    def entrada(self):
        if self.chave == self.mostrar:
            print('Você venceu!')
        else:
            letra = input('Digite uma letra: ')

            if letra in self.chave:
                self.acertos.append(letra)
            else:
                self.erros += 1
            self.fim()

    def quadro(self):
        global status
        print(status[self.erros])
        self.painel()

    def painel(self):
        self.mostrar = ""
        for letra in self.chave:
            if letra in self.acertos:
                self.mostrar += letra
            else:
                self.mostrar += '_'
        print(f'Acertos: {self.mostrar}')
        self.entrada()

    def fim(self):
        global status
        if self.erros == 6:
            print(status[6])
            print("Você perdeu!")
        else:
            self.quadro()

jogo = Forca(palavra)
jogo.quadro()