#Algoritmo: cálculo de média de um aluno mediante o nome do aluno e duas notas

#Entrada:
nome = input('Qual é o seu nome: ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

#Processamento:
media = (n1+n2)/2

#Saída:
print('\n')
print('---AGORA VOU TE MOSTRAR SUA MÉDIA---\n')
#print('Olá, ' + str(nome) + ". Sua média foi " + str(media))
#print('-----------------------------------')
#print('Ola, {}. Sua média é {:.2f}'.format(nome, media))
#print('-----------------------------------')
print(f'Olá, {nome}. Sua média é {media:.2f}')
