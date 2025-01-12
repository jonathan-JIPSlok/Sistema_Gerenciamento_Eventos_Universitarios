from os import system as prompt_system

from datetime import datetime
from time import sleep

def cabecalho(titulo = str) -> None:
    """
    Mostra um cabeçalho estruturado com data
    :param titulo: str: O titulo do cabeçalho.
    """
    prompt_system("cls")
    print('-'*50)
    print(f'\t {titulo} \t {datetime.today().date()}')
    print('-'*50)

def printar_opcoes(opcoes: tuple):
    """
    Mostra todas as opções do usuário, inclusive a de sair.
    :param opcoes: tuple: Deve conter todas as opções do usuário
    """
    for numero, item in enumerate(opcoes):
        print(f'[{numero}] - {item}')
    print('[sair] - para sair')

def data_validacao()-> str:
    """
    Função para coletar e validar uma data
    """
    while True:
        dia = input("Dia do Evento: ").strip()
        mes = input("Mes do Evento: ").strip()
        ano = input("Ano do Evento: ").strip()
        data = dia + mes + ano

        if data.isnumeric() and len(ano) == 4:
            return f"{dia}/{mes}/{ano}"
        else:
            print("Data inválida!")
            sleep(2)
