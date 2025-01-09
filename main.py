import os

from data_manipuling import load_json, save_json

from system_interface import interfaces

# Criando o diretório data caso ele não exista
os.makedirs('data', exist_ok=True)

# Constants
FILE_USERS = 'data/users.json'

# Coleta os dados do arquivo dos usuários
DATA_USERS = load_json(FILE_USERS)

# Verifica se o arquivo está vazio, caso esteja ele faz o usuário passar pelo processo de cadastro no primeiro uso.
if len(DATA_USERS) == 0:
    interfaces().register_user(DATA_USERS, frist_acess=True)
    save_json(FILE_USERS, DATA_USERS)
else:
    interfaces().register_user(DATA_USERS)
    save_json(FILE_USERS, DATA_USERS)