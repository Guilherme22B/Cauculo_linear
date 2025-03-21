from calc import calc
from layout import layout



largura = 3
altura = 3
layout.bem_vindo() 
layout.info_sistema()
layout.menu()
matriz = calc.criar_matriz_zerada(largura, altura)
calc.implementa_matriz(matriz, largura, altura)
calc.formatar_matriz(matriz)

