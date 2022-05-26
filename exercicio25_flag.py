#Escreva um programa que possa ler o nome de um aluno e um conjunto de notas de tamanho desconhecido e possa exibir na tela a maior nota. A leitura do valor -1 (flag) indicará o final da leitura dos dados.

nome = input("Olá! Digite seu nome: ")
nota = 0
maior_nota = 0

while nota != -1:
  nota = float(input("Digite uma nota: "))
  if nota > maior_nota:
    maior_nota = nota


print(maior_nota)
  
  