from os import system
from os import name as system_operational

from datetime import datetime
from time import sleep

from system_functions import user_register

class interfaces:
    def __init__(self):
        """
        Contem as interfaces do systema.
        """
        pass

    def cabecalho(self, titulo: str) -> None:
        """
        Printa um titulo na tela.
        :param titulo: str: Deve conter o titulo do que será mostrado.
        """
        system('cls') if system_operational == 'nt' else system('clear')

        print("-" *50)
        print(f'\t {titulo} \t {datetime.today().date()}')
        print("-" *50)

    def register_user(self, data_user: dict, frist_acess = False) -> bool:
        """
        Interface para registrar um usuário!
        :param data_user: dict: Dicionário contendo os dados do usuário.
        :param frist_acess: bool: Indica se é o primeiro acesso do usuário. Default é False.
        :return: bool: Retorna True se o registro for bem-sucedido, caso contrário, False.
        """
        user = ''
        while user != 'sair':
            self.cabecalho('Registro de usuário')
            
            # Se for o primeiro acesso ele cadastra um coordenador
            if frist_acess:
                nome = input('Nome completo: ')
                senha = input('Digite uma senha: ')
                email = input("Digite seu E-mail: ")

                #Cadastra no dicionário
                try:
                    if user_register(data_user, nome, senha, email, 'coordenador'):
                        print("Coordenador cadastrado com sucesso!")
                        sleep(1)
                        break
                    else:
                        print()
                except Exception as erro:
                    print(erro)
                    sleep(1)
            
            # Se não for o primeiro acesso o usuário decide se o cadastro é de coordenador ou aluno
            else:
                print('[1] - Cadastrar Aluno')
                print('[2] - Cadastrar coordenador')
                print('[sair] - Para sair \n')

                user = input("Informe a opção desejada: ")
                if user == 'sair':
                    break
                elif user == '1' or user == '2':
                    nome = input('Nome completo: ')
                    senha = input('Digite uma senha: ')
                    email = input("Digite seu E-mail: ")

                    if user_register(data_user, nome, senha, email, 'aluno' if user == '1' else 'coordenador'):
                        print('Usuário cadastrado com sucesso!')
                        sleep(1)

                else:
                    print("Opção invalida!")
                    sleep(1)
