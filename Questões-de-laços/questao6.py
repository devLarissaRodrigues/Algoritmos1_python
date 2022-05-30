#Faça um programa que, para um número desconhecido de pessoas: a)leia a idade de cada pessoa, sendo que a leitura da idade -1 (flag) indica o final da leitura dos dados e não deve ser considerada; b)ao final, calcule e escreva a quantidade de pessoas; c)calcule e escreva a idade média do grupo; d)calcule e escreva a menor e a maior idade;

maior = 0
menor = 1000
idade = 0
pessoas = 0
soma_idades = 0

while idade != -1:
  idade = int(input("Digite uma idade ou -1 para sair: "))
  
  if idade == -1:
    break
  pessoas += 1
  soma_idades += idade
  media = soma_idades/pessoas

  if idade > maior:
    maior = idade

  if idade < menor:
    menor = idade
  

print(f"A quantidade de pessoas é {pessoas}")
print(f"A média das idades é {media}")
print(f"A menor idade digitada foi {menor}")
print(f"A maior idade digitada foi {maior}")
    
  


