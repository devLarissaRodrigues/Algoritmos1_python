#Escreva um programa de “Reajustar Salário”, capaz de receber o nome completo e o salário inicial de um empregado e possa imprimir, no final, o nome e este salário reajustado em 20%.

nome = input('Digite seu nome completo: ')
salario = float(input('Digite seu salário: '))

salario_reajustado = salario - (0.2 * salario)
print(f'Olá, {nome}! Seu salário reajustado é {salario_reajustado:.2f}')
