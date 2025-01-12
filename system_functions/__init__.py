from datetime import datetime
from time import sleep

from .utilidades import cabecalho, printar_opcoes, data_validacao
from data_manipuling import save_json, load_json

class usuarios:
    """
    Classe que se refere aos usuários
    """

    def cadastrar(self, tipo = "aluno" or "coordenador"):
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

            #Se for aluno ele pega o RA
            if tipo == 'aluno':
                ra = input("RA do aluno: ")

            email = input("E-mail: ")
            telefone = input("Telefone: ").replace('(', '').replace(")", "").replace(' ', '')
            data_nascimento = input("Data de Nascimento: ").strip().replace(' ', '').replace("/", '')

            # verifica se o telefone e data de nascimento do usuário é valido para prosseguir.
            if telefone.isnumeric() and data_nascimento.isnumeric():

                # Registra o coordenador no dict e no arquivo
                if tipo == 'coordenador':
                    self.DATA_USERS[nome] = {"senha":senha, "email":email, "telefone": telefone, "data de nascimento":data_nascimento}
                    save_json(self.FILE_USERS, self.DATA_USERS)
                    print(f"Coordenador {nome.split()[0]} salvo com sucesso!")
                    sleep(2)
                    break

                # Registra o Aluno no dict e no arquivo
                elif tipo == 'aluno':
                    self.DATA_USERS[ra] = {"nome":nome, "senha":senha, "email":email, "telefone": telefone, "data de nascimento":data_nascimento}
                    save_json(self.FILE_USERS, self.DATA_USERS)
                    print(f"Coordenador {nome.split()[0]} salvo com sucesso!")
                    sleep(2)
                    break
            else:
                print("Número de telfone ou data de nascimento invalido!")
                sleep(1)

    def login(self, tipo = 'aluno' or 'coordenador'):
        """
        Classe que faz o login de um 
        :param tipo: str: define o tipo de usuário que fara login 'aluno' ou 'coordenador'
        """
        user = ''
        while user != "sair":
            cabecalho(f"Login do {tipo}")
            print("\n[sair] para sair ou digite os dados solicitados para continuar\n")

            # Se for coordenador define nome
            if tipo == "coordenador":
                user = input("Nome completo: ").strip().lower()

            # Se for aluno define RA
            elif tipo == 'aluno':
                user = input("RA: ").strip()
            if user == 'sair':
                break

            senha = input("Senha: ").strip()

            #faz o login do usuário
            if user in self.DATA_USERS and senha in self.DATA_USERS[user]["senha"]:
                self.USUARIO = {user:self.DATA_USERS[user]}
                self.pagina_inicial()
            else:
                print("Dados inválidos!")
                sleep(2)
    
    def pagina_inicial(self):
        """
        Página inicial do usuário
        """
        user = ''
        while user != 'sair':

            #Mostra o cabeçalho e as funções disponíveis
            cabecalho("Unifecaf Eventos")
            printar_opcoes(self.USER_OPTIONS)

            user = input("oque desenja: ").strip().lower()
            if user == "sair":
                quit()

            # Chama a função que o usuário escolheu
            elif user.isnumeric():
                self.chamar_funcao(int(user)) #Função vinda da classe "aluno ou coordenador"

            else:
                print("Opção invalida!")
                sleep(2)

    def listar_eventos(self):
        eventos = load_json("data/eventos.json")
        for numero, evento in enumerate(list(eventos.keys())):
            print(f"[{numero}] - {evento}")


        
class aluno(usuarios):
    """
    Classe que controla tudo que se refere a um Aluno
    """
    def __init__(self, data_users:dict, file_users: str):
        """
        :param data_user: dict: dicionário com os dados dos usuários cadastrados.
        :param file_users: str: contendo o local do arquivo.
        """
        self.DATA_USERS = data_users
        self.FILE_USERS = file_users
        self.USER_OPTIONS = ("Inscrever em Eventos", "Visualizar eventos disponíveis", "Visualizar Inscrições")
        self.USUARIO = {}
    
    def chamar_funcao(self, funcao = int):
        pass

class Coordenador(usuarios):
    """
    Classe que controla tudo que se refere a um Coordenador
    """
    def __init__(self, data_users:dict, file_users: str):
        """
        :param data_user: dict: dicionário com os dados dos usuários cadastrados.
        :param file_users: str: contendo o local do arquivo.
        """
        self.DATA_USERS = data_users
        self.FILE_USERS = file_users
        self.USER_OPTIONS = ("Cadastrar Evento", "Atualizar Evento", "Visualizar Eventos", "Excluir Eventos")

        self.USUARIO = {}

    def chamar_funcao(self, funcao = int):
        if funcao == 0:
            self.cadastrar_evento()
        elif funcao == 1:
            self.atualizar_evento()
        elif funcao == 2:
            self.listar_eventos()

    def cadastrar_evento(self):
        """
        Função para criar um evento
        """
        user = ''
        while user != "sair":

            # Mostra o cabeçalho
            cabecalho("Criar Eventos")
            print("[sair] para voltar\n")

            #coleta os dados
            nome = input("Nome do Evento: ").strip().capitalize()
            if nome == 'Sair':
                break
            data = data_validacao()
            max_pessoas = input("Número maximo de pessoas: ")
            descricao = input("Descrição do Evento: ").strip()

            # Valida os dados
            if max_pessoas.isnumeric() and int(max_pessoas) > 0:
                try:
                    eventos = load_json("data/eventos.json") # importa os eventos
                except:
                    eventos = {}

                #Registra os eventos
                if not nome in eventos.keys():
                    eventos[nome] = {"data": data, "maximo de pessoas": int(max_pessoas), "descricao": descricao, "coordenador": list(self.USUARIO.keys())[0]}
                    save_json("data/eventos.json", eventos)
                    print("Evento cadastrado com sucesso!")
                    sleep(1)
                else:
                    print("Evento já existe!")
                    sleep(1)
            else:
                print("número de pessoas deve ser númerico e maior que 0!")
                sleep(1)
    
    def atualizar_evento(self):
        sair = ""
        while user != 'sair':
            cabecalho("Eventos")
            self.listar_eventos()
            print("\n[sair] para sair \n")
            user = input("selecione um evento: ")

            if user == 'sair':
                break
            
