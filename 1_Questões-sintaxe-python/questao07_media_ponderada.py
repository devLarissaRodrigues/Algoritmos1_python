#A partir de três notas de um estudante, prepare um algoritmo para “Calcular Média com Pesos”, capaz de calcular a média final com pesos de notas 20%, 30% e 50%, respectivamente. Ao final, o programa deve imprimir o nome do aluno, suas notas parciais e sua média final.

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota3 = float(input('Agora digite sua terceira nota: '))

media_ponderada = (nota1*0.2 + nota2*0.3 + nota3*0.5)/(0.2+0.3+0.5)
print(f'Sua média final é {media_ponderada}')