def criar_matriz(nome):
  print(f"\n--- Inserindo valores para a Matriz {nome} (4x3) ---")
  matriz = []
  for i in range(4):
    linha = []
    for j in range(3):
      # Lê cada elemento da matriz (usando int, mas pode ser float se preferir)
      valor = int(input(f"Digite o elemento [{i}][{j}]: "))
      linha.append(valor)
    matriz.append(linha)
  return matriz