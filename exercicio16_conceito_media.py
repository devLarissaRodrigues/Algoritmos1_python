#Escreva um programa que receba 3 números inteiros como entrada e possa informar qual é o MAIOR

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 > num2 and num1 > num3:
  print(f"O número {num1} é o maior")
elif num2 > num1 and num2 > num3:
  print(f"O número {num2} é o maior")
elif num3 > num1 and num3 > num2:
  print(f"O número {num3} é o maior")