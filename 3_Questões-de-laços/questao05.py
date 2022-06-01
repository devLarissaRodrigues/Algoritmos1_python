#(Para profissionais!) Foi feita uma pesquisa de audiência de canais de TV em várias casas de uma certa cidade. Para cada casa visitada, foi perguntado sobre qual o canal (5, 7, 10 ou 12) e ainda o número de pessoas que o estavam assistindo naquela casa. Fazer um algoritmo que: a)leia um número desconhecido de casas que participaram da pesquisa; a leitura do valor -1 (flag) indicará o final da leitura dos dados; b)calcule e escreva o canal vencedor e a porcentagem de audiência de cada canal.

casas = 0
canal = 0
total_pessoas = 0

soma_5 = 0
soma_7 = 0
soma_10 = 0
soma_12 = 0

while canal != -1:
  canal = int(input("Digite o canal assistido (5, 7, 10 ou 12) ou digite -1 para sair: "))
  if canal == -1: 
    break
  else:
    pessoas = int(input(f"Digite a quantidade de pessoas que assistem ao canal {canal} em sua casa: "))
    casas += 1    

    if canal == 5:
      soma_5 += pessoas
    elif canal == 7:
      soma_7 += pessoas
    elif canal == 10:
      soma_10 += pessoas
    elif canal == 12:
      soma_12 += pessoas

    print("*" * 35)
    total_pessoas += pessoas

lista = [soma_5, soma_7, soma_10, soma_12]
for vencedor in lista:
  if max(lista) == soma_5:
    canal_vencedor = "Canal 5"
  elif max(lista) == soma_7:
    canal_vencedor = "Canal 7"
  elif max(lista) == soma_10:
    canal_vencedor = "Canal 10"
  elif max(lista) == soma_12:
    canal_vencedor = "Canal 12"


print(f"O canal vencedor é o {canal_vencedor}")

print(f"A porcentagem de pessoas que assiste ao canal 5 é {((soma_5/total_pessoas)*100):.2f}%")
print(f"A porcentagem de pessoas que assiste ao canal 7 é {((soma_7/total_pessoas)*100):.2f}%")
print(f"A porcentagem de pessoas que assiste ao canal 10 é {((soma_10/total_pessoas)*100):.2f}%")
print(f"A porcentagem de pessoas que assiste ao canal 12 é {((soma_12/total_pessoas)*100):.2f}%")

