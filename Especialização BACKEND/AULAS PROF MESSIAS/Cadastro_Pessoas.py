#While interativo
def lista_cadastros(database):
    if len(database) == 0:
        print("\n\t\033[1;31;40mNão existe nenhum cadastro!\033[m\n")
    else:
        for i in database.keys():
            s = f"Código: {i} |" \
                f"Nome: {database[i]['nome']} | " \
                f"Email: {database[i]['email']} | " \
                f"Data: {database[i]['data']}"
            print(s)

database = {}
print('\033[1;34;40m    CADASTRO DE PESSOAS    \033[m\n')
while True:
    opcao = int(input('\t\033[1;34;40m LISTA DE OPÇÕES \033[m\n'
                      '\033[1;34m[1]\033[m - Cadastrar uma pessoa\n'
                      '\033[1;34m[2]\033[m - Listar os cadastros\n'
                      '\033[1;34m[3]\033[m - Deletar cadastro\n'
                      '\033[1;34m[4]\033[m - Alterar um cadastro\n'
                      '\033[1;34m[0]\033[m - Sair do programa\n'
                      '\033[1;34;40m   Digite a opção desejada: \033[m'))
    if opcao == 1:
        print('\n\033[1;34;107m----Cadastrar uma pessoa-----\033[m\n')
        codigo = int(input('Digite o seu código: '))
        nome = input('Digite o nome: ')
        email = input('Digite seu e-mail: ')
        data = input('Digite o dia/mês do nascimento: ')

        database[codigo] = {'nome': nome, 'email': email, 'data': data}
        print('\033[1;33;107mSalvo com sucesso!\033[m\n')
    elif opcao == 2:
        print('\033[1;34;40m------Listagem de cadastros-------\033[m')
        lista_cadastros(database)
    elif opcao == 3:
        print("\033[1;34;40m------Deletar cadastro------\033[m")
        lista_cadastros(database)
        codigo = int(input("Digite o código a ser deletado: \n"))
        del database[codigo]
        print(f'\033[1;33;40mCódigo {codigo} deletado com sucesso!\033[m\n')
    elif opcao == 4:
        print("\033[1;34;40m------Alterar um cadastro------\033[m")
        print("\033[1;34m---- Selecione o item a ser alterado --- \033[m")
        lista_cadastros(database)
        codigo = int(input('Digite o código a ser alterado: '))
        op = int(input("\033[1;34m[1]\033[m - Nome\n"
                       "\033[1;34m[2]\033[m - Email\n"
                       "\033[1;34m[3]\033[m - Data\n"
                       "O que você deseja alterar: "))
        if op == 1:
            nome = input('Digite o novo nome: ')
            database[codigo]['nome'] = nome
        if op == 2:
            email = input('Digite o novo e-mail: ')
            database[codigo]['email'] = email
        if op == 3:
            data = input('Digite o novo mês/ano nascimento: ')
            database[codigo]['data'] = data
    elif opcao == 0:
        print('\n\t\033[1;7mContinuamos à disposição! Volte sempre!\033[m')
        break
