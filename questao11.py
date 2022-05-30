#Desenvolva um algoritmo gerador das tabuadas de adição e multiplicação, capaz de gerar a tabuada de qualquer número inteiro entre 1 e 10. O usuário deve informar qual numero ele deseja produzir as tabuadas


numero = int(input("Digite um número inteiro entre 1 e 10: "))

contador = 0
print(f"\nTABUADA DE ADIÇÃO DO NÚMERO {numero}:")
while contador <= 10:
  print(f"{numero} + {contador} = {numero + contador}")
  contador += 1

print(f"\nTABUADA DE MULTIPLICAÇÃO DO NÚMERO {numero}:")
contador = 0
while contador <= 10:
  print(f"{numero} x {contador} = {numero * contador}")
  contador += 1
  
