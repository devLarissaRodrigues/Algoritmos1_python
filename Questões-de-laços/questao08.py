#Escreva um algoritmo capaz de simular (uma parte) do uso de um menu de operações simples para um sistema de caixa automático bancário. O programa deve iniciar exibindo o menu abaixo. O usuário, então, pode escolher uma opção de uso—que apenas deverá ser impressa na tela (e.g., "Você escolheu a opção 1, sacar!")—e o programa deve retornar ao menu principal. Se teclar 0 (zero), o programa deve sair do menu e encerrar o atendimento do usuário. A fim de tentar reduzir longas filas de espera, neste programa bancário, o usuário pode realizar, no máximo, três operações em sequência. Caso tente executar mais, o programa deve alertar que o número máximo de operações foi utrapassado, sair do menu e encerrar o atendimento.

print("* * * * * * * * * * * *\nTerminal de atendimento\nBanco do Nordeste - BNE\n* * * * * * * * * * * *\n1- Saque\n2- Extrato\n3- Depósito\n4- Transferência\n* * * * * * * * * * * *\n0- Encerrar atendimento")

tentativas = 1
while tentativas <= 3:
  opcao = int(input("\nDigite o número correspondente à operação que deseja: "))
  if opcao == 0:
    print("Atendimento encerrado!")
    break
  elif opcao == 1:
    print("Você escolheu a opção 1: Sacar!")
  elif opcao == 2:
    print("Você escolheu a opção 2: Extrato!")
  elif opcao == 3:
    print("Você escolheu a opção 3: Depósito!")
  elif opcao == 4:
    print("Você escolheu a opção 4: Transferência!")
  tentativas += 1
  