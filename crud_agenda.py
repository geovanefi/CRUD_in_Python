#CRUD Atividade Ativa

import json, os

def add_contato():

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


add_contato()