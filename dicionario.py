usuarios = {}

opcao = input("O que deseja realizar?\n" +
             "<I> - Para inserir um usuario\n" +
             "<P> - Para pesquisar um usuario\n"+
             "<E> - Para excluir um usuario\n"+
             "<L> - Para Listar um usuario : \n").upper()

while opcao =="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        chave=input("Digite o login : ").upper()
        nome=input("Digite o nome : ").upper()
        data=input("Digite a ultima data de acesso : ")
        estacao=input("Qual a ultima estação acessada : ").upper()
        usuarios[chave]=[nome, data, estacao]

    opcao = input("O que deseja realizar?\n" +
             "<I> - Para inserir um usuario\n" +
             "<P> - Para pesquisar um usuario\n"+
             "<E> - Para excluir um usuario\n"+
             "<L> - Para Listar um usuario : \n").upper()

                  

