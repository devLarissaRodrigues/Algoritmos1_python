#Faça um algoritmo que pergunte ao usuário quantas palavras ele deseja inserir. Em seguida, leia as palavras informando qual é a maior palavra (em quantidade de caracteres). Use a função len(string) de Python para contar os caracteres das palavras.

quantidade_palavras = int(input("Digite a quantidade de palavras que deseja inserir: "))

contador = 1
lista = []
maior = ''

while contador <= quantidade_palavras:
  palavra = input(f"Digite a {contador}º palavra: ")
  contador += 1
  lista.append(palavra)

for palavra1 in lista:
  if len(palavra1) > len(maior):
    maior = palavra1

print(f"A maior palavra é {maior}")
  

  
  
