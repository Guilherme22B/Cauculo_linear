from sistem import sistem
from layout import layout
import sys


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
num = sistem.config_menu()
if(num == 1):
    sistem.solicitar_sistema()
if (num == 2):
    layout.info_sistema()
if (num == 3):
    sys.exit()



