import json, os

print("-----------------------------------------------")
print("               SISTEMA DE CADASTRO             ")
print("-----------------------------------------------")

def adicionar_contato():

    nome = input("nome do contato: ")
    telefone = input("numero do telefone: ")
    email = input("endereço de e-mail: ")
    twitter = input("conta do Twitter: ")
    instagram = input("@ do Instagram: ")

    dicionario = {
        "Nome: ": nome,
        "Telefone: ": telefone,
        "Email: ": email,
        "Twitter: ": twitter,
        "Instagram: " : instagram
    }

    if os.path.isfile("agenda.json"):
        with open("agenda.json", "r") as converte_python:
            itensdata = json.load(converte_python) #converter json para python
    else:
        itensdata = {}

    itensdata[nome] = dicionario

    with open("agenda.json", "w") as converte_json:
        json.dump(itensdata, converte_json) #converter python para json
        print("\nDados inseridos com SUCESSO")


def listar_contato():

    with open("agenda.json", "r") as visualizar:
        itensdata = json.load(visualizar)

        for i, m in itensdata.items():
            for x, n in m.items():
                print(x, n)
            print("\n")

def deletar_contato():
    nome = input("nome do contato: ")

    with open("agenda.json", "r") as busca_itens:
        itensdata = json.load(busca_itens)

        if nome in itensdata:
            itensdata.pop(nome)

            with open("agenda.json", "w") as delete:
                itensdata1 = json.dump(itensdata, delete)
                print("\nContato deletado com sucesso")

def atualizar_contato():
    nome = input("nome do contato: ")

    with open("agenda.json", "r") as busca_itens:
        itensdata = json.load(busca_itens)

        if nome in itensdata:
            telefone = input("numero do telefone: ")
            email = input("endereço de e-mail: ")
            twitter = input("conta do Twitter: ")
            instagram = input("@ do Instagram: ")

            dicionario = {
                "Nome: ": nome,
                "Telefone: ": telefone,
                "Email: ": email,
                "Twitter: ": twitter,
                "Instagram: " : instagram
            }

            itensdata[nome] = dicionario
            with open("agenda.json", "w") as insere_contato:
                json.dump(itensdata, insere_contato)
                print("\nContato inserido com sucesso!")

def pesquisar_contato():
    nome = input("nome do contato: ")
    with open("agenda.json", "r") as busca_itens:
        itensdata = json.load(busca_itens)
        if nome in itensdata:
            print(itensdata[nome])
        else:
            print("\nContato não encontrado")
            
def pesquisar_todos_contatos():
    with open("agenda.json", "r") as busca_itens:
        itensdata = json.load(busca_itens)
        print(itensdata)

def gerar_relatorio():
    with open("agenda.json", "r") as relatorio:
        contatos = json.load(relatorio)
        
        if contatos:
            print("=== RELATÓRIO DE CONTATOS ===\n")
            print("{:<15} {:<25} {:<15} {:<15}".format("Nome", "E-mail", "Twitter", "Instagram"))
            print("-" * 70)
            
            for nome, dados in contatos.items():
                nome = dados["Nome: "]
                email = dados["Email: "]
                twitter = dados["Twitter: "]
                instagram = dados["Instagram: "]
                
                print("{:<15} {:<25} {:<15} {:<15}".format(nome, email, twitter, instagram))
            
            print("-" * 70)
        else:
            print("Não há contatos cadastrados.")



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

    selecao = int(input("Escolha a opção: "))

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

menu()