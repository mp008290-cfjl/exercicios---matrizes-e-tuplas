def main():
  print("--- Verificação de Matriz Identidade (3x3) ---")
  matriz = []

  
  for i in range(3):
    linha = []
    for j in range(3):
      valor = float(input(f"Digite o elemento [{i}][{j}]: "))
      linha.append(valor)
    matriz.append(linha)
# 2. Analisa se a matriz é identidade
  eh_identidade = True
  for i in range(3):
    for j in range(3):
      if i == j:
        # Na diagonal principal, o elemento deve ser 1
        if matriz[i][j] != 1:
          eh_identidade = False
      else:
        # Fora da diagonal principal, o elemento deve ser 0
        if matriz[i][j] != 0:
          eh_identidade = False
