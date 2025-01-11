from datetime import datetime

def cabecalho(titulo = str) -> None:
    print('-'*50)
    print(f'\t {titulo} \t {datetime.today().date()}')
    print('-'*50)

def printar_opcoes(opcoes: tuple):
    for numero, item in enumerate(opcoes):
        print(f'[{numero}] - {item}')
    print('[sair] - para sair')