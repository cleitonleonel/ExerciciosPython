import math, random

def diagonal(largura,altura, origem_x, origem_y, destino_x,destino_y):
    #largura e altura
    largura = largura
    altura = altura

    # pontos
    #x = random.randint(-50,50)
    #y = random.randint(-50,50)

    #divisões iniciais
    dividir_largura = largura / 4
    dividir_altura = altura / 4
    centro_x = largura / 2
    centro_y = altura / 2

    #posições
    pontoA = destino_x,destino_y
    centro = centro_x,centro_y


    #direções
    '''
    norte --> y alto
    sul --> y baixo
    leste --> x alto
    oeste --> x baixo
    '''

    #prints
    print(f'A = {pontoA},C = {centro}')
    print(f'Uma área = {dividir_largura} x {dividir_altura}')

    #ifs
    if destino_x > (centro_x + 2.5) and destino_y > (centro_y + 2.5):
        print('Moveu para sudeste')
    if destino_x > (centro_x  + 2.5) and destino_y < (centro_y - 2.5):
        print('Moveu para nordeste')
    if destino_x < (centro_x  - 2.5) and destino_y > (centro_y + 2.5):
        print('Moveu para sudoeste')
    if destino_x < (centro_x  - 2.5) and destino_y < (centro_y - 2.5):
        print('Moveu para noroeste')

    else:
        if destino_x > (centro_x + 2.5) and destino_y > (centro_y - 2.5) and destino_y < (centro_y + 2.5):
            print('Moveu para leste')
        elif  destino_x < (centro_x + 2.5) and destino_y > (centro_y - 2.5) and destino_y < (centro_y + 2.5):
            print('Moveu para oeste')
        else:
            pass

        if destino_y > (centro_y + 2.5) and destino_x > (centro_x - 2.5) and destino_x < (centro_x + 2.5):
            print('Moveu para sul')
        elif destino_y < (centro_y - 2.5) and destino_x > (centro_x - 2.5) and destino_x < (centro_x + 2.5):
            print('Moveu para  norte')
        else:
            pass

def simular_distancia(x1,y1,x2,y2):
    #pontos
    pontoA = x1,y1
    pontoB = x2,y2

    #prints
    print('A:',pontoA)
    print('B:',pontoB)
    diagonal(10,10, pontoA[0],pontoA[1],pontoB[0],pontoB[1])

    #pitágoras
    cateto1 = int(x2) - int(x1)
    cateto2 = int(y2) - int(y1)
    hipotenusa = math.hypot(cateto1,cateto2)

    #prints2
    print(f'Cateto 1: {cateto1} | Cateto 2: {cateto2}')
    print('Hipotenusa:',round(hipotenusa,2))

    #equação
    velocidade = 4
    distancia = hipotenusa
    tempo = distancia / velocidade

    #prints3
    print('Tempo:', round(tempo,2))

    #conta no t1
    hipotenusa_intervalo = tempo
    cateto1_intervalo = cateto1 / velocidade #x
    cateto2_intervalo = cateto2 / velocidade #y

    #prints4
    print(f'Cat.Int1: {cateto1_intervalo} | Cat.Int2: {cateto2_intervalo}')

    #posições
    posicao = pontoA
    posicao_final = pontoB

    while x1 != x2 and y1 != y2:
        x1 += cateto1_intervalo
        y1 += cateto2_intervalo
        print('Ponto A:','(',(x1),',',(y1),')')


simular_distancia(10,90, random.randint(-50,50),random.randint(-50,50))




#diagonal(10,10, 30,30, 20,40)
