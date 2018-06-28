def definir_sprite(direction,sequence):
    direction = 3-1
    sequence = 4-1

    largura = 128
    altura = 192

    dividir_direcao = largura // 4 ** direction
    dividir_sequencia = altura // 4 ** sequence

    direcao = direction * dividir_sequencia
    sequencia = sequence * dividir_direcao
    print(direcao)
    print(sequencia)

    print('largura de um sprite:',dividir_direcao)
    print('altura de um sprite:',dividir_sequencia)


'''
 abcd efgh ijkl mnop
8    |    |    |    
7____|____|____|____
6    |    |    |        
5____|____|____|____
4    |    |    |    
3____|____|____|____
2    |    |    |    
1    |    |    |    
'''

definir_sprite(0,0)