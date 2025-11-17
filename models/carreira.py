# models/carreira.py

class Carreira:
    """
    Representa uma carreira profissional com suas competências-chave.
    
    Atributos:
        nome (str): O nome da carreira.
        descricao (str): Uma breve descrição da carreira.
        competencias_requeridas (dict): Um dicionário onde a chave é o nome
                                        da competência (str) e o valor é o
                                        nível mínimo (int 1-5) exigido.
    """
    def __init__(self, nome: str, descricao: str, competencias_requeridas: dict):
        self.nome = nome
        self.descricao = descricao
        # Ex: {"logica": 5, "criatividade": 3}
        self.competencias_requeridas = competencias_requeridas

    def __str__(self):
        return f"Carreira: {self.nome}"