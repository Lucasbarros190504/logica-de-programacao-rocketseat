resposta = input('Olá, vamos fazer uma brincadeira bem legal? (responda sim ou não): ').strip().upper()

if resposta == 'SIM':
    print('Ótimo! Preparando a mágica... ✨\n') 
    print('Vamos lá! Pense em uma das 5 cores a seguir: ')
    print('1-Laranja\n2- Vermelho\n3- Rosa\n4- Azul\n5- Verde')

    input('Pronto? Aperte ENTER quando tiver escolhido a cor... ')
    resposta_cor = input('Já sei...Existe um boto com essa cor?(responda com sim ou não): ').strip().upper()
    if resposta_cor == 'SIM':
      print('já sei....')
      print()
      print('É rosa!!! 🎨')
    elif resposta_cor == 'NÃO' or resposta_cor == 'NAO' :
      print('Poxa, errei!')
      cor_pensada = input('Qual cor que você pensou?').strip().capitalize()
      print(f'Poxa! Você pensou na cor {cor_pensada}. Espero acertar da próxima!')

elif resposta in ['NÃO' , 'NAO']:
        print('Entendido. Fico por aqui, até mais! 👋')
          
else:
        print('Desculpe, só consigo entender "Sim" ou "Não". Tente rodar o programa novamente.')
        