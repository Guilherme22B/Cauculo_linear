import numpy as np

def solicitar_sistema():
    try:
        n = int(input("Digite o tamanho do sistema (máximo 10): "))
        if n > 10 or n < 1:
            raise ValueError("Tamanho inválido. Escolha um valor entre 1 e 10.")
    except ValueError as e:
        print(e)
        return solicitar_sistema()

    A = []
    B = []
    print("Digite os coeficientes da matriz aumentada:")
    for i in range(n):
        try:
            linha = list(map(float, input(f"Equação {i + 1}: ").split()))
            if len(linha) != n + 1:
                raise ValueError("Número incorreto de coeficientes. Tente novamente.")
        except ValueError as e:
            print(e)
            return solicitar_sistema()
        A.append(linha[:-1])
        B.append(linha[-1])

    return np.array(A, dtype=float), np.array(B, dtype=float)

def imprimir_sistema(A, B, mensagem="Sistema:"):
    print(mensagem)
    for i in range(len(B)):
        print(" ".join(f"{A[i, j]:8.3f}" for j in range(len(A[i]))) + f" | {B[i]:8.3f}")

def escalonar(A, B):
    n = len(B)
    for i in range(n):
        # Pivoteamento parcial
        max_index = np.argmax(abs(A[i:, i])) + i
        if A[max_index, i] == 0:
            continue  # Se for zero, passa para a próxima iteração

        A[[i, max_index]] = A[[max_index, i]]
        B[[i, max_index]] = B[[max_index, i]]

        # Transformar em 1 o pivô
        pivô = A[i, i]
        A[i] = A[i] / pivô
        B[i] = B[i] / pivô

        # Zerar elementos abaixo do pivô
        for j in range(i + 1, n):
            fator = A[j, i]
            A[j] -= fator * A[i]
            B[j] -= fator * B[i]

    return A, B

def resolver_sistema(A, B):
    n = len(B)
    X = np.zeros(n)

    for i in range(n - 1, -1, -1):
        if A[i, i] == 0:
            if B[i] == 0:
                return "O sistema tem infinitas soluções (SPI)."
            else:
                return "O sistema é impossível (SI)."

        X[i] = (B[i] - np.dot(A[i, i + 1:], X[i + 1:])) / A[i, i]

    return X

def executar():
    dados = solicitar_sistema()
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
