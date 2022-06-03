#Faça um algoritmo que pergunte ao usuário quantas palavras ele deseja inserir. Em seguida, leia as palavras informando qual é a maior palavra (em quantidade de caracteres). Use a função len(string) de Python para contar os caracteres das palavras. Veja um exemplo abaixo: O tamanho da palavra abaixo será 6


quantidade = int(input("Informe quantas palavras você deseja digitar: "))

for indice in range(quantidade):
  palavra = input(f"Digite a {indice}º palavra: ")
  palavra1.append(palavra)