#(Para profissionais!) O custo final de um carro novo para seu consumidor é dado pela soma entre o  custo de fábrica, a percentagem do distribuidor (obtida do custo de fábrica) e ainda os impostos (obtidos do custo de fábrica). Supondo que a percentagem do distribuidor seja 10% e os impostos 45%, escreva um programa em Python capaz de processar e calcular o custo final de um carro. Este programa deve ler o custo de fábrica inicial do carro e exibir o custo final calculado para seu comprador.

custo_fabrica = float(input("Digite o valor do custo de fábrica inicial do carro: R$ "))

porcentagem_distribuidor = custo_fabrica * 0.1
impostos = custo_fabrica * 0.45

custo_final = custo_fabrica + porcentagem_distribuidor + impostos

print(f'O custo final é de R$ {custo_final:.2f}')