#Usando estruturas de repetição, faça um programa em Python que possa receber um caractere (qualquer), um número de linhas e um número de colunas e possa imprimir, ao final, uma seqüência conforme o exemplo abaixo:

linha = 0
coluna = 0

caractere = input("Digite um caractere: ")
linhas = int(input("Digite a quantidade de linhas: "))
colunas = int(input("Digite a quantidade de colunas: "))

while linha < linhas:
  print(colunas * caractere)
  linha += 1


  