# core/analisador.py
from models.perfil import Perfil
from models.carreira import Carreira
from typing import List, Tuple

class AnalisadorCarreira:
    """
    Classe responsável por processar o perfil do usuário
    e compará-lo com a base de carreiras.
    """
    def __init__(self, lista_carreiras: List[Carreira]):
        self.lista_carreiras = lista_carreiras

    def calcular_compatibilidade(self, perfil: Perfil) -> List[Tuple[Carreira, float, List[str]]]:
        """
        Calcula a compatibilidade do perfil com cada carreira.
        
        A lógica de "match" é um percentual simples de quantos requisitos
        de competência (com nível mínimo) o perfil atende.

        Retorna:
            Uma lista de tuplas, ordenada da maior compatibilidade para a menor.
            Cada tupla contém: (objeto Carreira, pontuacao_match (0-100), lista_de_gaps)
        """
        resultados = []

        for carreira in self.lista_carreiras:
            pontos_fortes = 0
            total_requisitos = len(carreira.competencias_requeridas)
            areas_para_melhorar = [] # Lista de gaps (trilhas de aprimoramento)

            # Itera sobre as competências exigidas pela carreira
            for comp_req, nivel_req in carreira.competencias_requeridas.items():
                
                # Pega o nível do usuário para essa competência.
                # Usa .get() para retornar 0 se o usuário não tiver a competência cadastrada.
                nivel_perfil = perfil.competencias.get(comp_req, 0)
                
                # Aplicação da lógica condicional
                if nivel_perfil >= nivel_req:
                    pontos_fortes += 1
                else:
                    # Adiciona à lista de aprimoramento
                    gap = f"{comp_req.capitalize()} (Necessário: {nivel_req} / Atual: {nivel_perfil})"
                    areas_para_melhorar.append(gap)
            
            # Calcula a pontuação de match (0 a 100)
            if total_requisitos > 0:
                pontuacao_match = (pontos_fortes / total_requisitos) * 100
            else:
                pontuacao_match = 100.0 # Se a carreira não exige nada, é 100%

            resultados.append((carreira, pontuacao_match, areas_para_melhorar))

        # Ordena a lista de resultados pela pontuação (índice 1 da tupla), do maior para o menor
        resultados.sort(key=lambda x: x[1], reverse=True)
        
        return resultados
        