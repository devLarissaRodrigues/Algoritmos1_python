#Escreva um algoritmo que calcule o valor de H, com duas casas decimais, sendo que H é determinado pela série: H = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50

numerador = -1
denominador = 0

for numero in range(50):
  numerador += 2
  denominador += 1
  print(f"{numerador}/{denominador}", end=" + ")
