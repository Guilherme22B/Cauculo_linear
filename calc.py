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
  def criar_matriz_zerada(tamanho): 
    matriz = [[0 for _ in range(tamanho[1])] for _ in range(tamanho[0])]
    return matriz


  '''essa função preenche a matriz com valores
     instipulados pelo usuario'''
  @staticmethod
  def implementa_matriz(tamanho, matriz):
    for i in range(tamanho[0]):
      for j in range(tamanho[1]): 
        matriz[i][j] = 10
    return matriz


  @staticmethod
  def formatar_matriz(matriz):
    print("aqui deve conter a formatação da matriz ")

  #essa matriz pede que o usuario insira o tamnaho e a largura
  @staticmethod
  def tamanho_matriz():
    print("qual o tamnaho da matriz desejada? ")
    altura = int(input("altura: "))
    largura = int(input("largura: "))
    tamanho = [altura, largura]
    return tamanho



  
    
    

    