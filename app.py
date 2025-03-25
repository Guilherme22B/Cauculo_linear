from calc import calc
from layout import layout


'''
layout.bem_vindo() 
layout.info_sistema()
layout.menu()
matriz = calc.criar_matriz_zerada(largura, altura)
calc.implementa_matriz(matriz, largura, altura)
calc.formatar_matriz(matriz)
'''

layout.bem_vindo()
layout.menu()
chave = calc.config_menu()
if(chave == 1):
    tamanho = calc.tamanho_matriz()
    matriz = calc.criar_matriz_zerada(tamanho)
    calc.implementa_matriz(tamanho, matriz)

