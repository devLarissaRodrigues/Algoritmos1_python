#O preço do Kw/h varia com a quantidade de energia elétrica consumida, conforme pode-se ver na tabela abaixo:
#Faça um programa para calcular o total a pagar no mês. A saída do sistema deve ter o seguinte formato:
#Consumidor: <FULANO>
#Consumo mensal: <X>
#Preço do kw/h em R$: <P>           Total a pagar R$: <Y>

nome = input("Digite seu nome: ")
consumo = float(input("Digite a quantidade de energia elétrica consumida: "))



if consumo >= 300:
  preco = 100.00
elif consumo >= 200 and consumo < 300:
  preco = 80.00
else:
  preco = 20.00
  
print(f"Consumidor: {nome.upper()}")
print(f"Consumo mensal: {consumo}")
print(f"Preço do kw/h em R$: {preco}")