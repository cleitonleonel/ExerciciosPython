#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
import random

class Bola:
    def __init__(self, cor, cir, material):
        self.cor = cor
        self.cir = cir
        self.material = material

    def trocaCor(self):
        new_cor = input('Qual a cor que deseja pintar a bola? ')
        self.cor = new_cor
        return self.cor

    def mostraCor(self):
        return self.cor

"""
if __name__ == '__main__':

    action = Bola('Azul', '50', 'couro')
    print(action)
    cor_da_bola = action.mostraCor()
    print(cor_da_bola)
    trocaCor = action.trocaCor()
    print('A bola agora é',action.mostraCor())

"""
class Quadrado:
    def __init__(self,lado):
        self.lado = lado

    def mudaValor(self):
        newlado = int(input('Digite um novo tamanho para os lados do quadrado: '))
        self.lado = newlado

    def valorLado(self):
        return self.lado

    def CalculaArea(self):
        self.total_area = self.lado * self.lado
        return self.total_area

"""
if __name__ == '__main__':

    action = Quadrado('9')
    print(action)
    tamanho_do_lado = action.valorLado()
    print(tamanho_do_lado)
    novo_tamanho = action.mudaValor()
    tamanho_do_lado = action.valorLado()
    print(tamanho_do_lado)
    soma_area = action.CalculaArea()
    print(soma_area)
"""

class Retangulo:
    def __init__(self,comprimento,largura):
        self.comprimento = comprimento
        self.largura = largura

    def mudar_lados(self):
        comprimento_informado = input('Informe o comprimento do retângulo: ')
        largura_informada = input('Informe a largura do retângulo: ')
        self.comprimento = comprimento_informado
        self.largura = largura_informada

    def retornar_valor(self):
        return (int(self.comprimento),'metros' ,int(self.largura),'metros')

    def calcular_area(self):
        self.area = (int(self.largura) * int(self.comprimento))
        return self.area

    def calcular_perimetro(self):
        self.perimetro = (int(self.largura) + int(self.comprimento))*2
        return self.perimetro
'''
action = Retangulo('9','4')
print(action)
tamanho_do_comprimento = action.mudar_lados()
tamanho_das_coisas = action.retornar_valor()
print(tamanho_das_coisas)
soma_area = action.calcular_area()
print(f'Você vai precisar de {soma_area} pisos para cobrir a área.')
soma_perimetro = action.calcular_perimetro()
print(f'Também vai precisar de {soma_perimetro} metros de rodapé para calçar todas as paredes.')
'''

class Pessoa:
    def __init__(self,nome,idade,peso,altura):
        self.nome = 'Lucas'
        self.idade = 0
        self.peso = 2
        self.altura = 50
        self.emagrecer = [1,2]
        self.definir = random.choice(self.emagrecer)

    def Envelhecer(self):
        while self.idade < 100:
            self.idade += 1
        return self.idade
    def Engordar(self):
        while self.idade < 10:
            self.peso += random.randint(1,5)
        if self.idade > 10 and self.definir == 1:
            self.peso += 1
        return self.peso

    def Emagrecer(self):
        if self.idade > 10 and self.definir == 2:
            self.peso += 1
        return self.peso
    def Crescer(self):
        while self.idade < 21:
            self.altura += 0.5
        return self.altura

alguem = Pessoa('João',0,2,50)
print(self.idade)