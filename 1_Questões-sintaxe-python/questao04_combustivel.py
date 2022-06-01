#(Para profissionais!) Escreva um programa em Python que seja capaz de calcular o número de litros no abastecimento em um posto de combustíveis. O programa deverá receber a quantia em reais (e.g., 335.90), o preço do combustível (e.g., 7.27) e seja capaz de exibir, com duas casas decimais, quantos litros de combustível serão colocados no tanque.


reais = float(input('Digite a quantia, em reais, que você deseja abastecer seu carro: R$ '))
preco_combustivel = float(input('Digite o preço do combustível: R$ '))

litros = reais/preco_combustivel

print(f'Com {reais} reais de combustível você conseguiu abastecer {litros:.2f} litros em seu automóvel')

