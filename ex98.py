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
    