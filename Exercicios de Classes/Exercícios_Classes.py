#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#


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

