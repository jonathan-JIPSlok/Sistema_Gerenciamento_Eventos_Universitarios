import os

from time import sleep

from data_manipuling import load_json, save_json

# Criando o diretório data caso ele não exista
os.makedirs('data', exist_ok=True)

# Constants
FILE_USERS = 'data/users.json'

# Coleta os dados do arquivo dos usuários
DATA_USERS = load_json(FILE_USERS)

# Verifica se o arquivo está vazio, caso esteja ele faz o usuário passar pelo processo de cadastro no primeiro uso.
if len(DATA_USERS) == 0: 
    pass

# Caso já tenha algo cadastrado, vamos para tela inícial em que o usuário decide se faz login ou sai
else:
    pass