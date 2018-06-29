def definir_sprite(direction,sequence):
    direction = direction
    sequence = sequence

    largura = 128
    altura = 192

    dividir_direcao = largura // 4
    dividir_sequencia = altura // 4


    direcao1 = dividir_direcao * (sequence-1)
    sequencia1 = dividir_sequencia * (direction-1)
    print(f'P1 = ({direcao1},{sequencia1})')

    direcao2 = sequence * dividir_direcao
    sequencia2 = direction * dividir_sequencia
    print(f'P2 = ({direcao2},{sequencia2})')

    print('largura de um sprite:',dividir_direcao)
    print('altura de um sprite:',dividir_sequencia)


'''
 abcd efgh ijkl mnop
8    |    |    |    
7____|____|____|____
6    |    |    |        
5____|____|____|____
4    |    |    |xxxx    
3____|____|____|____
2    |    |    |    
1    |    |    |    
'''

definir_sprite(2,4)