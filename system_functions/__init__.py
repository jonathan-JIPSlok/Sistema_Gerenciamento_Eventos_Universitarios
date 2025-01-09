from time import sleep

from data_manipuling import save_json

def user_register(data_user: dict, username: str, password: str, email: str, tipe = 'aluno' or 'coordenador') -> None:
    """
    Registra um novo usuário no sistema
    :param data_user: dict: Dicionário com os dados dos usuários
    :param username: str: Nome de usuário
    :param password: str: Senha
    :param tipe: str: Tipo de usuário se é aluno ou coordenador
    """
    # Verifica se o usuário já está cadastrado.
    if not username in data_user.keys():

        #Cadastra o usuário no dicionario
        data_user[username] = {'senha': password, 'email': email, 'tipo':tipe}
        return True
    else:
        print("Usuário já cadastrado!")
        sleep(1)
        return False