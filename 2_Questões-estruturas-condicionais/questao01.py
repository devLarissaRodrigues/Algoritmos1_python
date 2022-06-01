#Em um sistema de supermercado, as maçãs custam R$ 1,50 cada, se forem compradas menos de uma dúzia; e custam R$ 1,10 cada, se o cliente comprar a partir de 12 maçãs. Escreva um algoritmo que leia a quantidade de maçãs compradas pelo cliente, calcule e escreva o custo total da compra.

macas = int(input("Quantas maçãs você comprou? "))

if macas < 12:
  preco = macas * 1.5
else:
  preco = macas * 1.1
  
print(f"O custo total da sua compra é de R$ {preco:.2f}")