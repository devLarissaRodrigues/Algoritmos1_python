#Construir um algoritmo que calcule o imposto de renda (IR) de acordo com as informações abaixo.  As informações de Salário Bruto, INSS e Número de dependentes serão lidos pelo teclado.

#Desconto = R$ 90,00 por cada dependente
#Base de Cálculo = Salário Bruto – ( Desconto * Nº de dependentes) – Desconto INSS
#IR = (Base de cálculo) * Alíquota – Parcela a deduzir

salario_bruto = float(input("Digite o seu salário bruto: R$ "))
inss = float(input("Digite o INSS: "))
dependentes = int(input("Quantos dependentes há em sua casa? "))

desconto = dependentes * 90
base_calculo = salario_bruto - desconto - inss

if base_calculo <= 900.80:
  aliquota = 0
  parcela_deduzir = 0
elif base_calculo <= 1800.50:
  aliquota = 0.15
  parcela_deduzir = 135
else:
  aliquota = 0.275
  parcela_deduzir = 315

imposto_renda = (base_calculo * aliquota) - parcela_deduzir

print(f"O valor do imposto de renda é de R$ {imposto_renda:.2f}")

