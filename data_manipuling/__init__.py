import json

def load_json(file_path):
    """
    Carrega um arquivo JSON e retorna um dicionário
    :param file_path: str: Caminho do arquivo JSON
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
            return {}

def save_json(file_path, data):
    """
    Salva um dicionário em um arquivo JSON
    :param file_path: str: Caminho do arquivo JSON
    :param data: dict: Dicionário a ser salvo
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)