resposta = input('Olá, vamos fazer uma brincadeira bem legal? (responda sim ou não): ')

if resposta.upper() == 'SIM':
    print('Ótimo! Preparando a mágica... ✨') 
    print()
    print('Vamos lá! Pense em uma das 5 cores a seguir...')
    print('\n1-laranja\n2- vermelho\n3- rosa\n4- Azul\n5- verde')

    input('\nPressione ENTER quando tiver escolhido a cor.')
    resposta_cor = input('\nJá sei...Existe um boto com essa cor?(responda com sim ou não): ')
    if resposta_cor.upper() == 'SIM':
      print('já sei....')
      print()
      print('É ROSA!!!')
    elif resposta_cor.upper() == 'NÃO':
      print('Poxa,errei!')
      cor_pensada = input('Qual cor que você pensou?')
      print(f'Poxa!voce pensou na cor {cor_pensada}.Espero acerta da proxima!')

elif resposta.upper() == 'NÃO' or resposta.upper() == 'NAO':
        print('Entendido. Fico por aqui, até mais! 👋')
          
else:
        print('Desculpe, só consigo entender "Sim" ou "Não". Tente rodar o programa novamente.')
        