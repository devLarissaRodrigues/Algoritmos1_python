#Faça um programa para uma escola que, dadas três notas de um aluno e seu nome completo, exiba, no final, o nome do estudante, a média final e o seu conceito, observando que:
#a média final é calculada a partir da média aritmética simples das 3 notas;
#o conceito é determinado a partir da tabela a seguir:


nome = input("Digite seu nome completo: ")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3)/3

if media >= 80:
  conceito = "A"
elif media >= 50 and media < 80:
  conceito = "B"
else:
  conceito = "C"

print(f"{nome} obteve conceito {conceito}")
print(f"As notas fornecidas como entrada foram: {n1:.2f}, {n2:.2f} e {n3:.2f} com média final: {media:.2f}")