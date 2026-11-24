def main():
  print("--- Verificação de Matriz Identidade (3x3) ---")
  matriz = []

  
  for i in range(3):
    linha = []
    for j in range(3):
      valor = float(input(f"Digite o elemento [{i}][{j}]: "))
      linha.append(valor)
    matriz.append(linha)
