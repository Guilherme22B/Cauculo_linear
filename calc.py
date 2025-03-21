class calc():

  '''essa função cria uma regra para os valors que serao recolidos para o menu'''
  @staticmethod
  def config_menu():
    valor = int(input("Digite um número: "))
    if(valor <= 4 and valor >=0):
      return valor
    else: 
      print(f"{valor} é um valor incorreto ")
      calc.config_menu()




  '''Esta função cria e inicializa uma matriz 
  bidimensional com dimensões definidas pelo 
  usuário (largura e altura), preenchendo-a 
  com valores padrão iguais a zero.'''
  @staticmethod 
  def criar_matriz_zerada(largura, altura): 
    matriz = [[0 for _ in range(largura)] for _ in range(altura)]
    return matriz


  '''essa função preenche a matriz com valores
     instipulados pelo usuario'''
  @staticmethod
  def implementa_matriz(matriz, largura, altura):
    for i in range(altura):
      for j in range(largura): 
        matriz[i][j] = 10
    return matriz


  @staticmethod
  def formatar_matriz(matriz):
    print("aqui deve conter a formatação da matriz ")



  
    
    

    