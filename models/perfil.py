# models/perfil.py

class Perfil:
    """
    Representa o perfil profissional de um usuário.
    
    Atributos:
        nome (str): O nome do usuário.
        competencias (dict): Um dicionário onde a chave é o nome da
                             competência (str) e o valor é o nível (int 1-5)
                             que o usuário possui.
    """
    def __init__(self, nome: str):
        self.nome = nome
        # Ex: {"logica": 4, "criatividade": 5, "colaboracao": 3}
        self.competencias = {}

    def adicionar_competencia(self, competencia: str, nivel: int):
        """
        Adiciona ou atualiza o nível de uma competência no perfil.
        Valida se o nível está entre 1 e 5.
        """
        if 1 <= nivel <= 5:
            self.competencias[competencia] = nivel
            print(f"Competência '{competencia}' atualizada para o nível {nivel}.")
        else:
            print(f"Erro: O nível para '{competencia}' deve estar entre 1 e 5.")

    def __str__(self):
        return f"Perfil de: {self.nome}"