#(Para profissionais!) Foi feita uma pesquisa de audiência de canais de TV em várias casas de uma certa cidade. Para cada casa visitada, foi perguntado sobre qual o canal (5, 7, 10 ou 12) e ainda o número de pessoas que o estavam assistindo naquela casa. Fazer um algoritmo que: a)leia um número desconhecido de casas que participaram da pesquisa; a leitura do valor -1 (flag) indicará o final da leitura dos dados;b)calcule e escreva o canal vencedor e a porcentagem de audiência de cada canal.

contador_casas = 0
canal = 0
total_pessoas = 0

soma_pessoas_5 = 0
soma_pessoas_7 = 0
soma_pessoas_10 = 0
soma_pessoas_12 = 0

porcentagem_5 = 0
porcentagem_7 = 0
porcentagem_10 = 0
porcentagem_12 = 0


while canal != -1:
  canal = int(input("Digite o canal você mais assiste ou digite -1 para sair: "))
  if canal == -1: 
    break
  pessoas = int(input("Quantas pessoas assistem a esse canal em sua casa? "))
  contador_casas += 1
  print("-"*60)
  total_pessoas += pessoas

  if canal == 5:
    soma_pessoas_5 += pessoas
    porcentagem_5 = (soma_pessoas_5/total_pessoas)*100
  elif canal == 7:
    soma_pessoas_7 += pessoas
    porcentagem_7 = (soma_pessoas_7/total_pessoas)*100
  elif canal == 10:
    soma_pessoas_10 += pessoas
    porcentagem_10 = (soma_pessoas_10/total_pessoas)*100
  elif canal == 12:
    soma_pessoas_12 += pessoas
    porcentagem_12 = (soma_pessoas_12/total_pessoas)*100


 
print(f"Casas que participaram da pesquisa: {contador_casas-1}")
print(f"Porcentagem do canal 5: {porcentagem_5:.2f}%\nPorcentagem do canal 7: {porcentagem_7:.2f}%\nPorcentagem do canal 10: {porcentagem_10:.2f}%\nPorcentagem do canal 12: {porcentagem_12:.2f}%")

  
  
