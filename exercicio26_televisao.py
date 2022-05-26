#(Para profissionais!) Foi feita uma pesquisa de audiência de canais de TV em várias casas de uma certa cidade. Para cada casa visitada, foi perguntado sobre qual o canal (5, 7, 10 ou 12) e ainda o número de pessoas que o estavam assistindo naquela casa. Fazer um algoritmo que: a)leia um número desconhecido de casas que participaram da pesquisa; a leitura do valor -1 (flag) indicará o final da leitura dos dados;b)calcule e escreva o canal vencedor e a porcentagem de audiência de cada canal.

flag = 0
contador_casas = 0
acumulador = 0

while flag != -1:
  canal = int(input("Digite o canal você mais assiste: "))
  pessoas = int("Quantas pessoas assistem a esse canal em sua casa? ")
  contador_casas += 1
  print("-"*30)

  if canal == 5:
    acumulador += 1

  
  
