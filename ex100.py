def main():
  print("--- Verificação de Matriz Identidade (3x3) ---")
  matriz = []

  
  for i in range(3):
    linha = []
    for j in range(3):
      valor = float(input(f"Digite o elemento [{i}][{j}]: "))
      linha.append(valor)
    matriz.append(linha)

  eh_identidade = True
  for i in range(3):
    for j in range(3):
      if i == j:
        
        if matriz[i][j] != 1:
          eh_identidade = False
      else:
        
        if matriz[i][j] != 0:
          eh_identidade = False
# 3. Exibe a matriz digitada na tela
  print("\n================================")
  print("        MATRIZ INFORMADA        ")
  print("================================")
  for linha in matriz:
    linha_formatada = " | ".join(f"{val:4g}" for val in linha)
    print(f"[ {linha_formatada} ]")
  print("================================")