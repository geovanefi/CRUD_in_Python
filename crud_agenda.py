import json, os

print("-----------------------------------------------")
print("               SISTEMA DE CADASTRO             ")
print("-----------------------------------------------")

# Função para adicionar um novo contato ao sistema
def adicionar_contato():
    # Solicita informações do contato ao usuário
    nome = input("nome do contato: ")
    telefone = input("numero do telefone: ")
    email = input("endereço de e-mail: ")
    twitter = input("conta do Twitter: ")
    instagram = input("@ do Instagram: ")

    # Cria um dicionário com os dados do contato
    dicionario = {
        "Nome: ": nome,
        "Telefone: ": telefone,
        "Email: ": email,
        "Twitter: ": twitter,
        "Instagram: " : instagram
    }

    # Verifica se o arquivo de armazenamento existe
    if os.path.isfile("agenda.json"):
        # Carrega os contatos existentes do arquivo JSON para um dicionário
        with open("agenda.json", "r") as converte_python:
            itensdata = json.load(converte_python) # converter JSON para Python
    else:
        # Se o arquivo não existe, cria um novo dicionário vazio
        itensdata = {}

    # Adiciona o novo contato ao dicionário
    itensdata[nome] = dicionario

    # Salva o dicionário atualizado no arquivo JSON
    with open("agenda.json", "w") as converte_json:
        json.dump(itensdata, converte_json) # converter Python para JSON
        print("\nDados inseridos com SUCESSO")


# Função para listar todos os contatos cadastrados
def listar_contato():
    # Carrega os contatos do arquivo JSON para um dicionário
    with open("agenda.json", "r") as visualizar:
        itensdata = json.load(visualizar)

        # Itera sobre os contatos e exibe suas informações
        for i, m in itensdata.items():
            for x, n in m.items():
                print(x, n)
            print("\n")


# Função para excluir um contato existente
def deletar_contato():
    # Solicita o nome do contato a ser excluído
    nome = input("nome do contato: ")

    # Carrega os contatos do arquivo JSON para um dicionário
    with open("agenda.json", "r") as busca_itens:
        itensdata = json.load(busca_itens)

        # Verifica se o contato existe e remove-o do dicionário
        if nome in itensdata:
            itensdata.pop(nome)

            # Salva o dicionário atualizado no arquivo JSON
            with open("agenda.json", "w") as delete:
                itensdata1 = json.dump(itensdata, delete)
                print("\nContato deletado com sucesso")


# Função para atualizar as informações de um contato existente
def atualizar_contato():
    # Solicita o nome do contato a ser atualizado
    nome = input("nome do contato: ")

    # Carrega os contatos do arquivo JSON para um dicionário
    with open("agenda.json", "r") as busca_itens:
        itensdata = json.load(busca_itens)

        # Verifica se o contato existe
        if nome in itensdata:
            # Solicita as novas informações do contato
            telefone = input("numero do telefone: ")
            email = input("endereço de e-mail: ")
            twitter = input("conta do Twitter: ")
            instagram = input("@ do Instagram: ")

            # Cria um dicionário com as novas informações do contato
            dicionario = {
                "Nome: ": nome,
                "Telefone: ": telefone,
                "Email: ": email,
                "Twitter: ": twitter,
                "Instagram: " : instagram
            }

            # Atualiza as informações do contato no dicionário
            itensdata[nome] = dicionario

            # Salva o dicionário atualizado no arquivo JSON
            with open("agenda.json", "w") as insere_contato:
                json.dump(itensdata, insere_contato)
                print("\nContato inserido com sucesso!")


# Função para pesquisar um contato específico pelo nome
def pesquisar_contato():
    # Solicita o nome do contato a ser pesquisado
    nome = input("nome do contato: ")

    # Carrega os contatos do arquivo JSON para um dicionário
    with open("agenda.json", "r") as busca_itens:
        itensdata = json.load(busca_itens)

        # Verifica se o contato existe e exibe suas informações
        if nome in itensdata:
            print(itensdata[nome])
        else:
            print("\nContato não encontrado")


# Função para exibir todos os contatos cadastrados
def pesquisar_todos_contatos():
    # Carrega os contatos do arquivo JSON para um dicionário
    with open("agenda.json", "r") as busca_itens:
        itensdata = json.load(busca_itens)
        print(itensdata)


# Função para gerar um relatório com os dados de todos os contatos cadastrados
def gerar_relatorio():
    # Carrega os contatos do arquivo JSON para um dicionário
    with open("agenda.json", "r") as relatorio:
        contatos = json.load(relatorio)
        
        if contatos:
            print("=== RELATÓRIO DE CONTATOS ===\n")
            print("{:<15} {:<25} {:<15} {:<15}".format("Nome", "E-mail", "Twitter", "Instagram"))
            print("-" * 70)
            
            # Itera sobre os contatos e exibe seus dados no relatório
            for nome, dados in contatos.items():
                nome = dados["Nome: "]
                email = dados["Email: "]
                twitter = dados["Twitter: "]
                instagram = dados["Instagram: "]
                
                print("{:<15} {:<25} {:<15} {:<15}".format(nome, email, twitter, instagram))
            
            print("-" * 70)
        else:
            print("Não há contatos cadastrados.")


# Função principal que exibe o menu inicial e permite interagir com o sistema
def menu():
    print("\n ====> MENU INICIAR <=====")
    print("\n 1 = Adicionar Contato")
    print("\n 2 = Listar Contatos")
    print("\n 3 = Excluir Contato")
    print("\n 4 = Atualizar Contato")
    print("\n 5 = Pesquisar Contato")
    print("\n 6 = Pesquisar Todos Contatos")
    print("\n 7 = Gerar Relatório")
    print("\n 8 = Sair")
    print("\n====> digite o numero correspondente. <=====\n")

    # Solicita a seleção da opção desejada
    selecao = int(input("Escolha a opção: "))

    # Executa a função correspondente à opção selecionada
    if selecao == 1:
        adicionar_contato()
        menu()
    elif selecao == 2:
        listar_contato()
        menu()
    elif selecao == 3:
        deletar_contato()
        menu()
    elif selecao == 4:
        atualizar_contato()
        menu()
    elif selecao == 5:
        pesquisar_contato()
        menu()
    elif selecao == 6:
        pesquisar_todos_contatos()
        menu()
    elif selecao == 7:
        gerar_relatorio()
        menu()
    else:
        print("Saindo do programa... OBRIGADO!")

# Executa a função menu para iniciar o sistema
menu()
