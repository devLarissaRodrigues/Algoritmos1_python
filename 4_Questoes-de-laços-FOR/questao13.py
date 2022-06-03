linhas = int(input("Digite a quantidade de linhas: ")) 
colunas = int(input("Digite a quantidade de colunas: "))
caractere = input("Digite o caractere desejado: ")


for linha in range(linhas):
  for coluna in range(colunas):
    print(caractere, end=' ')
  print()