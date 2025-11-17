# main.py
import os
import time
from models.perfil import Perfil
from database.db import COMPETENCIAS_BASE, CARREIRAS_DB
from core.analisador import AnalisadorCarreira

def limpar_tela():
    """Função simples para limpar o console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_cabecalho():
    """Exibe o título da aplicação."""
    limpar_tela()
    print("====================================================")
    print("  🤖 Orientador de Carreiras do Futuro 🤖")
    print("====================================================")
    print("Conectando automação ao desenvolvimento humano.\n")

def coletar_perfil() -> Perfil:
    """
    Função para criar ou atualizar o perfil do usuário.
    Interage com o usuário para obter nome e níveis de competência.
    """
    exibir_cabecalho()
    print("--- 1. Criação de Perfil ---")
    nome = input("Digite seu nome: ")
    perfil = Perfil(nome)
    
    print("\nPor favor, avalie suas competências de 1 (Iniciante) a 5 (Especialista):")
    print("(Se não souber, pode digitar 1)\n")

    # Itera sobre a TUPLA de competências base
    for competencia in COMPETENCIAS_BASE:
        while True:
            try:
                # Pergunta o nível para cada competência
                nivel_input = input(f"  - {competencia.capitalize()}: ")
                nivel = int(nivel_input)
                
                if 1 <= nivel <= 5:
                    perfil.adicionar_competencia(competencia, nivel)
                    break
                else:
                    print("Por favor, insira um valor entre 1 e 5.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro.")
    
    print("\nPerfil criado com sucesso!")
    time.sleep(2)
    return perfil

def exibir_recomendacoes(perfil: Perfil, analisador: AnalisadorCarreira):
    """
    Função para processar e exibir as recomendações para o perfil.
    """
    exibir_cabecalho()
    print(f"--- 2. Análise e Recomendações para {perfil.nome} ---")
    
    # Chama o método do analisador para obter os resultados
    resultados = analisador.calcular_compatibilidade(perfil)
    
    if not resultados:
        print("Nenhuma carreira encontrada em nosso banco de dados para analisar.")
        input("\nPressione Enter para voltar ao menu...")
        return

    print("Analisando seu perfil contra as carreiras do futuro...\n")
    time.sleep(1)

    # Itera sobre a LISTA de resultados (já ordenada)
    for carreira, match, areas_melhorar in resultados:
        print("\n----------------------------------------------------")
        print(f"🌟 Carreira: {carreira.nome} (Match: {match:.1f}%)")
        print(f"   Descrição: {carreira.descricao}")
        
        # Condicional para exibir trilhas de aprendizado ou parabenizar
        if not areas_melhorar:
            print("   ✅ Parabéns! Você atende a todos os requisitos desta carreira.")
        else:
            print(f"   🌱 Trilhas de Aprimoramento ({len(areas_melhorar)}):")
            for area in areas_melhorar:
                print(f"      - {area}")
    
    print("\n----------------------------------------------------")
    input("\nPressione Enter para voltar ao menu...")

def menu_principal():
    """Função principal que controla o loop da aplicação CLI."""
    perfil_usuario = None
    # Instancia o analisador com o "banco de dados" de carreiras
    analisador = AnalisadorCarreira(CARREIRAS_DB)

    while True:
        exibir_cabecalho()
        print("Selecione uma opção:")
        print("1. Criar / Atualizar meu Perfil de Competências")
        print("2. Ver Recomendações de Carreira")
        print("0. Sair")
        print("====================================================")

        opcao = input("Opção: ")

        if opcao == '1':
            perfil_usuario = coletar_perfil()
        elif opcao == '2':
            if perfil_usuario:
                exibir_recomendacoes(perfil_usuario, analisador)
            else:
                print("\nVocê precisa criar um perfil primeiro (Opção 1).")
                time.sleep(2)
        elif opcao == '0':
            print("\nObrigado por usar o Orientador de Carreiras. O futuro espera por você!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")
            time.sleep(1)

# Ponto de entrada do script
if __name__ == "__main__":
    menu_principal()