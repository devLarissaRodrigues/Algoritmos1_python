#Escreva um algoritmo para ler um número inteiro e exiba se ele é maior, igual ou menor que zero

numero = int(input("Digite um número: "))

if numero > 0:
  print(f"O número {numero} é maior que zero")
elif numero == 0:
  print(f"O número {numero} é igual a zero")
else:
  print(f"O número {numero} é menor que zero")        