# Lista de perguntas e respostas do quiz
perguntas = [
  ['Qual o nome do atual presidente do Brasil?' , 'Lula'] ,
  ['Qual o ano da proxima copa do mundo?' , '2026'] ,
  ['Qual a montanha mais alta do mundo?' , 'monte everest'] , 
  ['Qual país tem o formato de uma bota?' , 'Italia'] ,
]
# Contador de respostas corretas
acertos = 0

# Início do quiz
print('Olá! Seja bem-vindo ao Quiz LB')
print('O quiz terá 4 perguntas. Vamos ver quantas você consegue acertar!. \nVamos nessa!')
input('Digite ENTER para começar o quiz')

# Percorre cada pergunta da lista
for pergunta_resposta in perguntas:

  # Separa a pergunta e a resposta correta
  pergunta = pergunta_resposta[0]
  resposta_correta  = pergunta_resposta[1].lower()
  
  # Mostra a pergunta e lê a resposta do usúario
  print(f"\nPergunta: {pergunta}")
  resposta_usuario = input("Sua resposta: ").lower()

  # Verifica se a resposta está correta
  if resposta_usuario == resposta_correta:
    print('Resposta correta! ✅')
    acertos += 1
  else:
    print(f'Resposta errada!❌ A resposta correta era: {resposta_correta}')

print('\nQuiz finalizado!')
print(f'Você acertou {acertos} de {len(perguntas)} perguntas.')
