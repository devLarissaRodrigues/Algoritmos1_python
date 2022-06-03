#Desenvolva um algoritmo gerador das tabuadas de adição e multiplicação, capaz de gerar a tabuada de qualquer número inteiro entre 1 e 10. O usuário deve informar qual numero ele deseja produzir as tabuadas.

numero = int(input("Digite um número inteiro entre 1 e 10: "))

print(f"\nTABUADA DE ADIÇÃO DO NÚMERO {numero}")
for num1 in range(11):
  print(f"{numero} + {num1} = {numero+num1}")


print(f"\nTABUADA DE MULTIPLICAÇÃO DO NÚMERO {numero}")
for num2 in range(11):
  print(f"{numero} x {num2} = {numero*num2}")