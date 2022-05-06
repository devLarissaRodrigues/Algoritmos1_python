#Faça um programa que leia o nome do eleitor e sua idade e seja capaz de informar sua classe eleitoral, de acordo com as instruções abaixo:
#Não eleitor (abaixo de 16 anos);
#Eleitor obrigatório (entre 18 e 65 anos) e
#Eleitor facultativo (entre 16 e 18 anos ou acima dos 65 anos).

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade < 16:
  print(f"Olá, {nome}! Você é não eleitor (abaixo de 16 anos)")
elif idade >= 18 and idade <= 65:
  print(f"Olá, {nome}! Você é um eleitor obrigatório (idade entre 18 e 65 anos)")
else:
  print(f"Olá {nome}! Você é um eleitor facultativo (idade entre 18 anos ou acima de 65 anos)")