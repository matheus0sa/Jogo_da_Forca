import situacao
import random

with open('palavras.txt',  encoding='utf-8') as file:
    palavras = file.readlines()
status = situacao.situacao
palavra = random.choice(palavras)


class Forca():
    def __init__(self, palavra):
        self.chave = palavra[:len(palavra)-1].lower()
        self.acertos = []
        self.erros = 0
        self.mostrar = ""


    def entrada(self):
        if self.chave == self.mostrar:
            print('Você venceu!')
        else:
            letra = input('Digite uma letra: ').lower()

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
            print(f'A palavra era {self.chave}')
        else:
            self.quadro()

jogo = Forca(palavra)
jogo.quadro()