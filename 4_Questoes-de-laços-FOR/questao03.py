#Escreva um programa capaz de ler as notas de 5 alunos onde cada aluno possui 2 notas. Utilize estruturas de repetição para ler os dados de cada aluno e suas notas. O programa deve imprimir o nome de cada aluno e sua média final com duas casas decimais.

for aluno in range(5):
  nome = input("Digite seu nome: ")
  n1 = float(input("Digite sua primeira nota: "))
  n2 = float(input("Digite sua segunda nota: "))
  media = (n1+n2)/2
  print(f"Olá, {nome}! Sua média é {media:.2f}")
  print("*" * 30)
  