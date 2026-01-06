perguntas = [
  ['Qual o nome do atual presidente do Brasil?,' 'Lula'] ,
  ['Qual o ano da proxima copa do mundo?,' '2026'] ,
  ['Qual a montanha mais alta do mundo?,' 'monte everest'] , 
  ['Qual país tem o formato de uma bota?,' 'Itália'] ,

]

print('Olá! Seja bem vindo ao quiz LB')
print('O quiz terá o total de 5 perguntas e cada pergunta irá valer 2 pontos. Vamos ver quantos pontos você vai conseguir fazer. \nVamos nessa!')
input('digite ENTER para começar o quis')

for pergunta_resposta in perguntas:
  pergunta = pergunta_resposta[0]
  #resposta_correta  = pergunta_resposta[1] # Você usará isso para verificar a resposta depois

  print(f"\nPergunta: {pergunta}")
  resposta_usuario = input("Sua resposta: ")


