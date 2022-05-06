#Faça um programa em Python capaz de ler uma temperatura em graus Celsius e convertê-la em Fahrenheit. A fórmula da conversão é: F = 32 –9C/5

celsius = float(input('Digite a temperatura, em Celsius, que você deseja converter para Fahrenheit: '))

fahrenheit = 32 + (9 * celsius)/5

print(f'Fiz a conversão de temperaturas para você! {celsius}º Celsius equivale a {fahrenheit}º Fahrenheit')
