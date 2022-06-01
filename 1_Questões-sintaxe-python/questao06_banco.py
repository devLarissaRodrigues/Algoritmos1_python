#(Para profissionais!) Um cliente resolveu poupar e efetuou um depósito (em R$) num Banco em uma conta poupança. Neste banco, o valor do rendimento da poupança é fixo de 1% a cada mês decorrido. Com base neste cenário, escreva um programa em Python que leia o montante inicial depositado e o tempo (em meses) que o dinheiro ficará aplicado na conta. O programa deve calcular e exibir na tela o rendimento (i.e., quanto dinheiro esta conta irá acumular) após a passagem destes meses. Assuma que cliente não efetuará nenhuma retirada de dinheiro desta conta poupança até lá.

montante_inicial = float(input('Digite o valor do montante inicial depositado: '))
tempo = int(input('Digite quantos meses o montante ficará aplicado na conta: '))

#Cálculo de juros compostos:
montante_final = montante_inicial * pow(1+0.01, tempo)
rendimento = montante_final - montante_inicial

print(f'Parabéns pelo investimento! Ao final de {tempo} meses, você tem um valor de R$ {rendimento:.2f} de rendimento')