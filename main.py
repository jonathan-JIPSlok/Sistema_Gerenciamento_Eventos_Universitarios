import os

from time import sleep

from data_manipuling import load_json
from system_functions import Coordenador
from system_functions.utilidades import cabecalho, printar_opcoes

# Criando o diretório data caso ele não exista
os.makedirs('data', exist_ok=True)

# Constants
FILE_USERS = 'data/users.json'

# Coleta os dados do arquivo dos usuários
DATA_USERS = load_json(FILE_USERS)

# Verifica se o arquivo está vazio, caso esteja ele faz o usuário passar pelo processo de cadastro no primeiro uso.
if len(DATA_USERS) == 0:
    Coordenador().cadastrar(tipo="coordenador")

# Caso já tenha algo cadastrado, vamos para tela inícial em que o usuário decide se faz login ou sai
else:
    # Primeira tela
    user = ''
    while user != "sair":
        cabecalho("Unifecaf Eventos")
        printar_opcoes(("Sou Aluno", "Sou Coordenador"))
        user = input("O que deseja: ")
        if user == 'sair':
            break
        elif user == '0':
            Coordenador(DATA_USERS, FILE_USERS).login(tipo="aluno")
        elif user == '1':
            Coordenador(DATA_USERS, FILE_USERS).login(tipo="coordenador")
