#Escreva um programa para uma clínica médica que determine o grau de obesidade de uma pessoa. Devem ser fornecidos como entrada o peso (em kilogramas) e a altura (em metros) da pessoa. O grau de obesidade é determinado pelo IMC – Índice de Massa Corpórea (IMC = Peso / Altura2). No final, o programa deve emitir as mensagens correspondentes conforme a tabela a seguir:

peso = float(input("Digite seu peso, em quilogramas: "))
altura = float(input("Digite sua altura, em metros: "))

imc = peso/(altura**2)
print(f"Seu IMC é {imc:.2f}")

if imc < 18.5:
  print("Você está abaixo do seu peso ideal")  
elif imc >= 18.5 and imc <= 24.9:
  print("Parabéns! Você está no seu peso ideal!")
elif imc >= 25 and imc <= 29.9:
  print("Você está acima do seu peso (sobrepeso)")
elif imc >= 30 and imc <= 34.9:
  print("Obesidade grau I")
elif imc >= 35 and imc <= 39.9:
  print("Obesidade grau II")
else:
  print("Obsesidade grau III")

