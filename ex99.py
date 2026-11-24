def main():
  pessoas = []

  print("--- Cadastro de 10 Pessoas ---")
  for i in range(1, 11):
    print(f"\n--- Pessoa {i} de 10 ---")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    pessoa_tupla = (nome, idade)
    pessoas.append(pessoa_tupla)

  menores_de_18 = []
  maiores_de_18 = []

  for nome, idade in pessoas:
    if idade < 18:
      menores_de_18.append((nome, idade))
    else:
      maiores_de_18.append((nome, idade))

  print("\n" + "=" * 40)
  print("         GRUPO 1: MENORES DE 18 ANOS")
  print("=" * 40)
  if menores_de_18:
    for nome, idade in menores_de_18:
      print(f"• {nome} — {idade} anos")
  else:
    print("Nenhuma pessoa com menos de 18 anos cadastrada.")