from datetime import datetime
from time import sleep

from .utilidades import cabecalho
from data_manipuling import save_json

class aluno:
    """
    Classe que controla tudo que se refere a um Aluno
    """
    def __init__(self, data_users):
        self.DATA_USERS = data_users


class Coordenador:
    """
    Classe que controla tudo que se refere a um Coordenador.
    """
    def __init__(self, data_users: dict, file_users: str) -> None:
        """
        :param data_user: dict: dicionário com os dados dos usuários cadastrados.
        :param file_users: str: contendo o local do arquivo.
        """
        self.DATA_USERS = data_users
        self.FILE_USERS = file_users
    
    
    def cadastrar(self):
        """
        Cadastra um novo usuário do tipo coordenador.
        """
        user = ''
        while user != "sair":

            # printa o cabeçalho da tela
            cabecalho("Cadastro de Coordenador")

            #Coletando os dados do usuário
            print('[sair] para sair \nou nom completo para prosseguir \n')
            nome = input("Nome completo: ").lower().strip()
            
            #Verifica se o usuário quer sair.
            if nome == "sair":
                return False
            
            senha = input("Defina uma senha: ").strip()
            email = input("E-mail: ")
            telefone = input("Telefone: ").replace('(', '').replace(")", "").replace(' ', '')
            data_nascimento = input("Data de Nascimento: ").strip().replace(' ', '').replace("/", '')

            # verifica se o telefone e data de nascimento do usuário é valido para prosseguir.
            if telefone.isnumeric() and data_nascimento.isnumeric():
                self.DATA_USERS[nome] = {"senha":senha, "email":email, "telefone": telefone, "data de nascimento":data_nascimento}
                save_json(self.FILE_USERS, self.DATA_USERS)
                print(f"Coordenador {nome.split()[0]} salvo com sucesso!")
                sleep(2)
                break
            else:
                print("Número de telfone invalido!")
                sleep(1)