import numpy as np

class sistem():
    def config_menu():
        num = int(input("digite um número de 1 a 3: "))
        if num > 3 or num < 1:
            sistem.config_menu()
        else:
            return num
    





















    def solicitar_sistema():
      # Solicita ao usuário o tamanho do sistema e valida a entrada
      try:
          numero = int(input("Digite o tamanho do sistema (máximo 10): "))
          if numero > 10 or numero < 1:
              raise ValueError("Tamanho inválido. Escolha um valor entre 1 e 10.")
      except ValueError as e:
          print(e)
          return sistem.solicitar_sistema()

      # Inicializa as matrizes de coeficientes e termos independentes
      A = []
      B = []
      print("Digite os coeficientes da matriz aumentada:")
      for i in range(numero):
          try:
              linha = list(map(float, input(f"Equação {i + 1}: ").split()))
              if len(linha) != numero + 1:
                  raise ValueError("Número incorreto de coeficientes. Tente novamente.")
          except ValueError as e:
              print(e)
              return sistem.solicitar_sistema()
          A.append(linha[:-1])  # Coeficientes
          B.append(linha[-1])   # Termo independente

      return np.array(A, dtype=float), np.array(B, dtype=float)






def imprimir_sistema(A, B, mensagem="Sistema:"):
    # Exibe a matriz aumentada na tela
    print(mensagem)
    for i in range(len(B)):
        print(" ".join(f"{A[i, j]:8.3f}" for j in range(len(A[i]))) + f" | {B[i]:8.3f}")




def escalonar(A, B):
    n = len(B)
    for i in range(n):
        # Pivoteamento parcial para evitar divisão por zero
        max_index = np.argmax(abs(A[i:, i])) + i
        if A[max_index, i] == 0:
            continue  # Se for zero, passa para a próxima iteração

        # Troca de linhas para trazer o maior valor para a posição de pivô
        A[[i, max_index]] = A[[max_index, i]]
        B[[i, max_index]] = B[[max_index, i]]

        # Normaliza a linha do pivô (transforma o pivô em 1)
        pivô = A[i, i]
        A[i] = A[i] / pivô
        B[i] = B[i] / pivô

        # Zera os elementos abaixo do pivô
        for j in range(i + 1, n):
            fator = A[j, i]
            A[j] -= fator * A[i]
            B[j] -= fator * B[i]
    return A, B





def resolver_sistema(A, B):
    n = len(B)
    X = np.zeros(n)

    # Substituição retroativa para encontrar as variáveis
    for i in range(n - 1, -1, -1):
        if A[i, i] == 0:
            if B[i] == 0:
                return "O sistema tem infinitas soluções (SPI)."
            else:
                return "O sistema é impossível (SI)."

        X[i] = (B[i] - np.dot(A[i, i + 1:], X[i + 1:])) / A[i, i]

    return X





def executar():
    # Executa o programa principal
    dados = sistem.solicitar_sistema()
    if dados is None:
        return

    A, B = dados
    imprimir_sistema(A, B, "Sistema original:")

    A_esc, B_esc = escalonar(A.copy(), B.copy())
    imprimir_sistema(A_esc, B_esc, "Sistema escalonado:")

    resultado = resolver_sistema(A_esc, B_esc)
    if isinstance(resultado, str):
        print(resultado)
    else:
        print("Solução:", resultado)

if __name__ == "__main__":
    executar()
