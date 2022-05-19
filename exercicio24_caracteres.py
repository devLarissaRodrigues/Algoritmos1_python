#(Para profissionais!) Usando estruturas de repetição, faça um programa em Python que possa receber um caractere (qualquer), um número de linhas e um número de colunas e possa imprimir, ao final, uma seqüência conforme o exemplo abaixo:

caractere = input("Digite o caratere desejado: ")
#linhas = int(input("Digite a quantidade de linhas desejada: "))
colunas = int(input("Digite a quantidade de colunas desejada: "))

contador1 = 0
contador2 = 0

while colunas >= contador1:
  colunas -= 1
  quantidade_colunas = caractere * colunas

print(quantidade_colunas)
 

