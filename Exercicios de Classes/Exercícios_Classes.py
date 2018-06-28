#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
import random
import datetime

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


class Retangulo1:

    def __init__(self, base,altura):
        self.base = base
        self.altura = altura

    def muda_valor_lados(self):
        new_base = int(input('Digite um novo tamanho para a base: '))
        self.base = new_base
        new_altura = int(input('Digite um novo tamanho para a altura: '))
        self.altura = new_altura

    def mostraValor(self):
        return self.base,self.altura
    
    def calculaArea(self):
        self.total_area = self.base * self.altura / 2
        return self.total_area

    def calculaPerimetro(self):
        self.total_area = self.base + self.altura * 2
        return self.total_area


if __name__ == '__main__':

    """
    base = int(input('Digite um para a base: '))
    altura = int(input('Digite um para a altura: '))
    action = Retangulo(base, altura)
    print(action)
    novo_tamanho = action.muda_valor_lados()
    print(novo_tamanho)
    tamanho_dos_lados = action.mostraValor()
    print(tamanho_dos_lados)
    soma_area = action.calculaArea()
    print(soma_area)
    soma_perimetro = action.calculaPerimetro()
    print(soma_perimetro)
"""
"""
    # USO DO LADO DO CLIENTE
    base = int(input('Digite um para a base: '))
    altura = int(input('Digite um para a altura: '))
    action = Retangulo(base, altura)
    soma_area = action.calculaArea()
    soma_perimetro = action.calculaPerimetro()
    print('Você vai gastar %s metros quadarados em pisos e %s metros em rodapés'%(soma_area, soma_perimetro))
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
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

        self.gordura = 0



        self.opcoes_biotipo = ['magro', 'gordo']
        self.opcoes_doencas_hereditarias = {
            1:{'doenca':'hipertensão', 'idade_inicio':25, 'probabilidade':10, 'reducao_vida':1}, # perde 1 ano
            2:{'doenca':'diabetes', 'idade_inicio':10, 'probabilidade':12, 'reducao_vida':2},  # perde 2 anos
            3:{'doenca':'cancer', 'idade_inicio':2, 'probabilidade':15, 'reducao_vida':3} # perde 3 anos
        }

        self.pre_disposicao = self.opcoes_doencas_hereditarias[random.randint(1, 3)]
        # probabilidade de ter a doenca aumenta a cada ano.. mas seu crescimento eh aleatorio.
        # probabilidade aumenta de 0, 1 ou 2 por cento ao ano.
        print(self.pre_disposicao)
        print(self.pre_disposicao['doenca'])


        self.biotipo = random.choice(self.opcoes_biotipo)
        print("MEU BIOTIPO VAI SER: ",self.biotipo)


    def Envelhecer(self):
        idade_esperada = random.randint(20, 90)
        self.pre_disposicao['diagnosticado'] = False
        doente = 0

        while self.idade < idade_esperada:
            if self.pre_disposicao['diagnosticado'] == False:
                if self.idade >= self.pre_disposicao['idade_inicio']:
                    chance = random.randint(0,100)
                    if chance <= self.pre_disposicao['probabilidade']:
                        self.pre_disposicao['diagnosticado'] = True
                    else:
                        self.pre_disposicao['probabilidade'] += random.randint(0,3)
            else:
                idade_esperada = idade_esperada - self.pre_disposicao['reducao_vida']


            if self.idade < 10:
                self.Engordar()
                self.Crescer()
            else:
                if self.idade <= 21:
                    self.Crescer()

                variacao = random.randint(0,100)
                if variacao <= 50:
                    if self.biotipo == "magro":
                        self.Emagrecer()
                    else:
                        self.Engordar()

                elif variacao <= 80:
                    pass

                else:
                    if self.biotipo == "magro":
                        self.Engordar()
                    else:
                        self.Emagrecer()
            self.idade += 1
            #print('Envelheci um ano.')
            if self.peso <= 19 and self.idade > 13:
                print('Morri de anorexia')
                break
        print('probabilidade:', self.pre_disposicao['probabilidade'])
        print('anos restante: ',idade_esperada)
        print('idade esperada antes:', idade_esperada,'idade:', self.idade)
        return self.idade

    def Engordar(self):
        if self.idade < 10:
            self.peso += 5
            #print('Engordei 5 kilos')
        self.peso += 2
        #print('Engordei um kilo')
        return self.peso

    def Emagrecer(self):
        self.peso -= 1
        #print('Emagreci um quilo')
        return self.peso

    def Crescer(self):
        if self.idade <= 17:
            self.altura += random.randrange(3,7)
            #print('Cresci 10 cm')
        self.altura += random.randrange(3,6)
        #print('Cresci 5 cm')
        return self.altura

    #def __str__(self):
    #    return ('Nome:'+ self.nome+'idade:'+self.idade+'peso:'+self.peso+'altura:'+self.altura)
'''
nomes = ['João', 'Lucas', 'Cleiton', 'Diego', 'Adenildo', 'Cesar', 'Luana', 'Roza']

alguem = Pessoa(nomes[random.randint(0, len(nomes))],0,2,0)
alguem.Envelhecer()
print(alguem)
print('Nome: '+ alguem.nome+' idade: '+str(alguem.idade)+' peso: '+str(alguem.peso)+' altura: '+str(alguem.altura)+ ' Biotipo: ' + str(alguem.biotipo))
'''

class Conta:
    def __init__(self, nome, saldo=0):
        self.numero_conta = str(random.randint(10000,99999))+'-'+str(random.randint(1,9))
        self.nome_correntista = nome
        self.saldo = saldo
        self.historico = []

    def alterarNome(self):
        self.nome_correntista = input('Digite um novo nome de correntista: ')
        return self.nome_correntista

    def deposito(self):
        valor = int(input('Qual o valor do depósito? '))
        self.saldo += valor
        print(f'Contando dinheiro, aguarde...\nSalvando no histórico de depósitos...\nR${valor} depositados em sua conta. Seu novo saldo é de: R${self.saldo}')
        self.historico.append(f'Depósito no valor de R${valor}')
        return self.saldo

    def saque(self):
        valor = int(input('Qual o valor do saque? '))
        if valor > self.saldo:
            print('Saldo insuficiente!')
        else:
            self.saldo -= valor
            print(f'Separando o seu dinheiro, aguarde...\nSalvando no histórico de saques...\nR${valor} debitados de sua conta. Seu novo saldo é de: R${self.saldo}')
            self.historico.append(f'Saque no valor de R${valor}')
            return self.saldo

    def extrato(self):
        print(f'\nNome do correntista: {conta.nome_correntista} | Número da conta: {conta.numero_conta}')
        for transacoes in self.historico:
            print(transacoes)
        print(f'Saldo final: R${self.saldo}')

'''
conta = Conta('José Roserbaldo Pereira',random.randint(0,10000))
while True:
    opcao = int(input('1. Alterar nome do titular\n2. Fazer um depósito\n3. Fazer um saque\n4. Tirar extrato\n0. Sair\nO que você gostaria de fazer? '))
    if opcao == 1:
        conta.alterarNome()
    elif opcao == 2:
        conta.deposito()
    elif opcao == 3:
        conta.saque()
    elif opcao == 4:
        conta.extrato()
    elif opcao == 0:
        break
    else:
        print('Comando inválido!')


print(f'\nNome do correntista: {conta.nome_correntista}\nNúmero da conta: {conta.numero_conta}\nSaldo: {conta.saldo} ')
'''

class TV:
    def __init__(self):
        self.estado = False
        self.volume = 0
        self.canal = 0
    def ligar_desligar(self):
        if self.estado == False:
            self.estado = True
            print('TV ligada')
        else:
            self.estado = False
            print('TV desligada')
    def aumentar_volume(self):
        self.volume += 1
        print(f'Volume: {self.volume}')
        return self.volume
    def diminuir_volume(self):
        self.volume -= 1
        print(f'Volume: {self.volume}')
        return self.volume

    def trocar_canal(self):
        self.canal = input('2. TVE\n4. TV Gazeta/Globo\n6. TV Vitória/Record\n7. TV Tribuna/SBT\n10. TV Capixaba/Band\n'
                           'Digite o número do canal que você quer: ')
        print(f'Agora você está no canal {self.canal}')
        return self.canal

"""
tv = TV()
while True:
    opcao = int(input('0. Ligar/Desligar a TV\n1. Mudar canal\n2. Aumentar o volume\n3. Abaixar o volume\n'
                      'O que você gostaria de fazer? '))
    if opcao == 0:
        tv.ligar_desligar()
    elif opcao == 1:
        tv.trocar_canal()
    elif opcao == 2:
        tv.aumentar_volume()
    elif opcao == 3:
        tv.diminuir_volume()
"""


class Tamagushi:

    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def obter_nome(self):
        return self.nome

    def altera_nome(self):
        self.nome = input('Dê um novo nome ao bichinho: ')
        return self.nome

    def obter_fome(self):
        return self.fome

    def alterar_fome(self):
        self.fome = int(input('Digite um novo percentual de fome para o bichinho: '))
        self.humor()
        return self.fome

    def obter_saude(self):
        return self.saude

    def alterar_saude(self):
        self.humor()
        self.saude = int(input('Digite um novo percentusl de saúde para o bichinho: '))
        return self.saude

    def obter_idade(self):
        return self.idade

    def alterar_idade(self):
        self.idade = input('Dê uma nova idade para o bichinho: ')

    def humor(self):
        if self.fome >= self.saude:
            print('%s está com fome e está ficando doente.' % self.nome)
        elif (self.fome * self.saude) >= 80 :
            print('%s está com fome e mal humorado.' % self.nome)
        else:
            print('%s está ótimo.' % self.nome)
        return self.fome * self.saude


bicho = Tamagushi('Tamagoshi', 6, 5, 10)
trocar_nome = bicho.altera_nome()
print('O Nome do nosso bichinho agora é %s' % trocar_nome)
nome = bicho.obter_nome()
print('Olá %s' % nome)
humor = bicho.humor()
print(humor)
trocar_fome = bicho.alterar_fome()
print(trocar_fome)


