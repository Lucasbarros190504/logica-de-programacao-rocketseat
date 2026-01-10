print('🔮 Bem-vindo ao Oráculo da sabedoria python🔮')


while True:
  tema = input ("\nDigite um assunto de programação (ex:python, java, sql) ou 'sair' para encerrar: ").lower()

  if tema == "sair":
    print("Até a próxima! ")
    break

  match tema:
   case 'python': 
    print('Python é uma linguagem de programação focada em ligibilidade. Ela possui 3 pilares: 1- Fácil de ler.\n2- Multiúso\n3- Pronta para uso ')
    
   case 'java':
    print('Java é uma linguagem de programação robusta, orientada a objetos e famosa pela sua portabilidade: "escreva uma vez, execute em qualquer lugar" ')

   case 'sql':
    print('sql (Structured Query Language) não é uma linguagem de programação comum, mas sim uma linguagem de consulta usada exclusivamente para interagir com bancos de dados.')

   case 'html':
    print('HTML (HyperText Markup Language) não é uma linguagem de programação, mas sim uma linguagem de marcação usada para estruturar e dar corpo às páginas da web.')  

   case _:
    print('Ainda estou aprendendo sobre esse assunto!')  
  