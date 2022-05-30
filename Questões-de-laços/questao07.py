#Escreva um programa que possa ler do usuário uma senha e verificar se a senha digitada é igual a "abc123". Neste programa, o usuário tem, no máximo, 3 tentativas de acertar a senha (insira entradas inválidas para verificar se o número de tentativas irá expirar com sucesso). A cada vez que o usuário errar a senha, exiba uma mensagem de erro e quantas tentativas ainda lhe restam.

tentativa = 1
senha_correta = "abc123"
quantidade = 3

while tentativa <= 3:
  senha = input("Digite a senha corretamente: ")
  quantidade -= 1
  if senha != senha_correta:
    print(f"Senha incorreta. Quantidade de tentativas restante: {quantidade}\n")
  else:
    print("\nParabéns! Senha correta.")
    break
  tentativa += 1
  