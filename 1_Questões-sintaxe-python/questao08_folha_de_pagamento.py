"""(Para profissionais!) O programa de uma indústria realiza a folha mensal de pagamentos de seus empregados baseando-se nas seguintes regras:

Deve-se, primeiro, ler os dados de cada funcionário (matrícula, nome e salário bruto);
Depois, o programa irá deve processar o salário e exibir na tela o seu contracheque, cujo formato é dado a seguir (próxima página):

Matrícula: 
Nome completo:
Salário Bruto:
Dedução INSS:
Salário Líquido:
"""

nome = input("Olá! Por favor, digite seu nome completo: ")
matricula = input("Agora digite sua matrícula: ")
salario_bruto = float(input('Digite seu salário bruto: R$ '))
deducao_inss = salario_bruto * 0.15
salario_liquido = salario_bruto - deducao_inss

print('-----------------------------------------------------')

print(f'Matrícula: {matricula}')
print(f'Nome completo: {nome}')
print(f'Salário bruto: R$ {salario_bruto}')
print(f'Dedução INSS: {deducao_inss}')
print(f'Salário Líquido: {salario_liquido}')

