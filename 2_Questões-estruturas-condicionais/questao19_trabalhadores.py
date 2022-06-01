#Numa fábrica, os trabalhadores são divididos em 3 classes:
#Os que fazem até 30 peças por mês (Classe C)
#Os que fazem de 31 a 44 peças por mês (Classe B)
#Os que fazem mais de 44 peças por mês (Classe A)
#A classe C recebe salário-mínimo (SM).  A classe B recebe SM mais 5% do SM por peça.  A classe A recebe SM mais 10% do SM por cada peça fabricada.
#Faça um algoritmo que:
#  Leia Salário mínimo, Nome do funcionário e o nº de peças confeccionadas por mês;
# Calcule o salário do funcionário e determine a classe que o funcionário pertence;

nome = input("Digite seu nome: ")
pecas = int(input("Digite a quantidade de peças confeccionadas por mês: "))

salario_minimo = 1212

if pecas <= 30:
  classe = "C"
  salario_final = salario_minimo
elif pecas >= 31 and pecas <= 44:
  classe = "B"
  salario_final = salario_minimo + (salario_minimo * 0.05)
else:
  classe = "A"
  salario_final = salario_minimo + (salario_minimo * 0.1)

print(f"Funcionário: {nome}")
print(f"Salário mínimo: R$ {salario_minimo:.2f}")
print(f"Número de peças fabricadas: {pecas}")           
print(f"Classe: {classe}")
print(f"Salário final calculado: R$ {salario_final:.2f}")