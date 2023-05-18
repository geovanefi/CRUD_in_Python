#CRUD Atividade Ativa

import json, os

# Adicona contatos
def add_contatos():

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
        print("Dados inseridos com SUCESSO")


def ver_contatos():

    with open("agenda.json", "r") as visualizar:
        itensdata = json.load(visualizar)

        for i, m in itensdata.items():
            for x, n in m.items():
                print(x, n)
            print("\n")

def delete_contatos():
    nome = input("nome do contato: ")

    with open("agenda.json", "r") as busca_itens:
        itensdata = json.load(busca_itens)

        if nome in itensdata:
            itensdata.pop(nome)

            with open("agenda.json", "w") as delete:
                itensdata1 = json.dump(itensdata, delete)
                print("Contato deletado com sucesso")

ver_contatos()



















# https://www.youtube.com/watch?v=gyqGt20hiI8