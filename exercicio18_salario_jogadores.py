#A diretoria de uma Equipe de Futebol deseja aumentar o salário de seus jogadores registrados.  O ajuste salarial deve obedecer algumas regras. Preparar um algoritmo para ler o nome e o salário atual do jogador (em reais) e, no final, possa imprimir seus dados junto com o salário anterior e o novo salário reajustado.

nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário: R$ "))

if salario <= 1000:
  taxa = 0.3
elif salario <= 1500:
  taxa = 0.2
elif salario <= 2000:
  taxa =  0.15
elif salario <= 2500:
  taxa = 0.1
else:
  taxa = 0.05

salario_com_aumento = salario + (taxa * salario)

print(f"Olá, {nome}! Seu salário anterior era R$ {salario:.2f} e seu novo salário reajustado é R$ {salario_com_aumento:.2f}")