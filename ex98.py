def criar_matriz(nome):
    print(f"\n--- Inserindo valores para a Matriz {nome} (4x3) ---")
    matriz = []
    for i in range(4):
        linha = []
        for j in range(3):
            valor = int(input(f"Digite o elemento [{i}][{j}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz


def main():
    matriz1 = criar_matriz("A")
    matriz2 = criar_matriz("B")

    matriz_soma = []
    for i in range(4):
        linha = []
        for j in range(3):
            soma = matriz1[i][j] + matriz2[i][j]
            linha.append(soma)
        matriz_soma.append(linha)

    print("\n========================================")
    print("      RESULTADO DA SOMA (Matriz C)      ")
    print("========================================")

    for linha in matriz_soma:
        linha_formatada = " | ".join(f"{val:5}" for val in linha)
        print(f"[ {linha_formatada} ]")

    print("========================================")


if __name__ == "__main__":
    main()