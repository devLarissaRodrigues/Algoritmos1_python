#Escreva um programa em Python capaz de receber a idade de uma pessoa e exibir o valor equivalente em segundos. Teste o programa usando valores de idades como 18, 56 ou 94 anos;

idade = int(input('Digite sua idade: '))

#1 ano - 365 dias
#1 dia - 24 h
#1 hora - 60 min
#1 min - 60 s
#Logo, 1 ano tem (365*24*60*60)s = 31536000s

idade_segundos = idade * (365*24*60*60)

print(f'Sua idade em segundos é {idade_segundos}')