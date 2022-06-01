#Escreva um programa que permita ao usuário inserir os valores do dia, mês e ano de uma data qualquer e verifique se essa data é válida. Informe o dia, mês e ano como três variáveis inteiras.
#Exemplo: um mês pode variar de 1 a 12 (de janeiro a dezembro) e cada mês pode ter 28, 29, 30 ou 31 dias. Logo “05/10/2019” é uma data válida, mas “31/11/2019” é inválida (novembro tem apenas 30 dias), assim como “32/14/2019” (não existe o mês 14 e nenhum mês tem 32 dias). Lembre-se: os meses que possuem 31 dias são janeiro, março, maio, julho, agosto, outubro e dezembro (ou seja, os meses 1, 3, 5, 7, 8, 10 e 12); os que possuem 30 dias são abril, junho, setembro e novembro (meses 4, 6, 9 e 11). Considere que fevereiro (mês 2) como tendo sempre 28 dias

print("PROGRAMA QUE VERIFICA SE UMA DATA DO ANO É VÁLIDA OU NÃO\n")

dia = int(input("Digite o dia a ser verificado: "))
mes = int(input("Digite o mês a ser verificado: "))
ano = int(input("Agora digite o ano: "))


if (dia <= 0 or dia > 31) or (mes <= 0 or mes > 12):
  condicao1 = "Data inválida"
  condicao2 = "Data inválida"
  condicao3 = "Data inválida"
  condicao4 = "Data inválida"
else:
  condicao1 = "Data válida"
  condicao2 = "Data válida"
  condicao3 = "Data válida"
  condicao4 = "Data válida"
  
  #MÊS - FEVEREIRO:
  if mes == 2:
    if dia <= 28:
      condicao2 = "Data válida"
    else:
      condicao2 = "Data inválida"
  
  #MESES COM ATÉ 30 DIAS:
  elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia <= 30:
      condicao3 = "Data válida"
    else:
      condicao3 = "Data inválida"
  
  #MESES COM ATÉ 31 DIAS:
  elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia <= 31:
      condicao4 = "Data válida"
    else: 
      condicao4 = "Data inválida"


if condicao1 == "Data inválida" or condicao2 == "Data inválida" or condicao3 == "Data inválida" or condicao4 == "Data inválida":
  validez_da_data = "Data inválida"
else:
  validez_da_data = "Data válida"

print("\n"+validez_da_data)
print(f"{dia:02.0f}/{mes:02.0f}/{ano:04.0f}")
    