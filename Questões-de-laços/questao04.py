#Escreva um programa que possa ler o nome de um aluno e um conjunto de notas de tamanho desconhecido e possa exibir na tela a maior nota. A leitura do valor -1 (flag) indicará o final da leitura dos dados.

nota = 0
maior = 0

while nota != -1:
  nota = float(input("Digite uma nota ou -1 para sair: "))
  if nota > maior:
    maior = nota
    
print(f"A maior nota digitada é {maior}")


