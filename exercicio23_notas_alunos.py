#Escreva um programa capaz de ler as notas de 5 alunos onde cada aluno possui 2 notas. Utilize estruturas de repetição para ler os dados de cada aluno e suas 2 notas. O programa deve imprimir o nome de cada aluno e sua média final.

quantidade_alunos = 1
while quantidade_alunos <= 5:
  aluno = input("Digite seu nome: ")
  nota1 = float(input("Digite sua primeira nota: "))
  nota2 = float(input("Digite sua segunda nota: "))
  media = (nota1 + nota2)/2
  print(f"\nNome do(a) aluno(a): {aluno}.\nMédia final: {media:.2f}\n")
  quantidade_alunos = quantidade_alunos + 1

