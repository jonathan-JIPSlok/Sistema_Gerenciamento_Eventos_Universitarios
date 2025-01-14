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

def printar_opcoes(opcoes: tuple) -> None:
    """
    Mostra todas as opções do usuário, inclusive a de sair.
    :param opcoes: tuple: Deve conter todas as opções do usuário
    """
    for numero, item in enumerate(opcoes):
        print(f'[{numero}] - {item}')
    print('[sair] - para sair')

def printar_eventos(evento: dict):
    cont = 0
    for chave in evento.keys():
        print(f"Nome: {chave} \t [{cont}]")
        print(f"Data: {evento[chave]["data"]}")
        print(f"Máximo de pessoas: {str(evento[chave]["maximo de pessoas"])}")
        print(f"Descrição: {evento[chave]["descricao"]}")
        print("-" *50)
        cont += 1
        
def data_validacao(maior = False)-> str:
    """
    Função para coletar e validar uma data
    :param maior: bool: True para verificar se a data é maior que a data atual, por padrão vem False 
    """
    while True:
        dia = input("Dia do Evento: ").strip()
        mes = input("Mes do Evento: ").strip()
        ano = input("Ano do Evento: ").strip()
        data = dia + mes + ano

        if data.isnumeric() and len(ano) == 4:
            
            #Se a data não precisar ser maior que a atual
            if maior == "False":
                return f"{dia}/{mes}/{ano}"

            # Se a dat aprecisar ser meior que a atual
            elif datetime(int(ano), int(mes), int(dia)) > datetime.now():
                return f"{dia}/{mes}/{ano}"
        
        #Caso a data esteja inválida
        print("Data inválida!")
        sleep(1)
