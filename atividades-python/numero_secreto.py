print('Olá! Vamos fazer uma brincadeira bem divertida?\nO jogo se chama NÚMERO SECRETO!')
input('Aperte ENTER para começar!')

numero_secreto = 25
tentativas = 0
acertou = False

while not acertou: 
  chute = int(input('Tente adivinhar o número (de 1 a 30): '))
  tentativas += 1

  if chute == numero_secreto:
   acertou = True
   print(f'PARABENS!! Você acertou o número em {tentativas} tentativas!')

  elif chute > numero_secreto:
   print('Errou!! O numero secreto é menor do que esse ')
  
  else:
   print('Errou!! O número secreto é maior do que esse')
  




