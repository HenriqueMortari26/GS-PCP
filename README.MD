#  Orientador de Carreiras do Futuro

##  Propósito do Projeto

O **Orientador de Carreiras do Futuro** é um sistema desenvolvido em Python com foco em Programação Orientada a Objetos (POO). Sua missão é simular uma ferramenta inteligente de orientação de carreiras, analisando perfis profissionais com base em competências técnicas e comportamentais (soft & hard skills) relevantes para o mercado de trabalho emergente.

Este projeto conecta a lógica de programação e a automação ao desenvolvimento humano e profissional, estimulando a criação de soluções que preparam pessoas para os desafios e oportunidades do futuro.

##  Funcionalidades

* **Criação de Perfil:** O usuário pode criar um perfil pessoal avaliando seu nível (1-5) em diversas competências-chave, como "Lógica", "Criatividade", "Colaboração", "IA/ML", etc.
* **Banco de Carreiras:** O sistema possui um "banco de dados" simulado com profissões do futuro (ex: "Engenheiro de IA Ética", "Designer de Realidade Mista").
* **Motor de Recomendação:** O sistema compara o perfil do usuário com os requisitos de cada carreira, gerando um "percentual de match".
* **Trilhas de Aprimoramento:** Para cada carreira recomendada, o sistema informa quais competências o usuário precisa desenvolver (gaps) para atingir o nível mínimo exigido, sugerindo uma trilha de aprendizado.
* **Interface de Console (CLI):** Interação com o usuário feita de forma textual, simples e intuitiva.

## 🛠️ Requisitos Técnicos Atendidos

* **Linguagem:** Python 3.x
* **Paradigma:** Programação Orientada a Objetos (POO)
* **Estrutura de Dados:**
    * **Listas:** Usadas para armazenar o banco de carreiras (`CARREIRAS_DB`) e os resultados da análise.
    * **Tuplas:** Usadas para armazenar a lista imutável de competências-base (`COMPETENCIAS_BASE`).
    * **Dicionários:** Usados extensivamente para armazenar as competências e seus respectivos níveis dentro dos objetos `Perfil` e `Carreira`.
* **Modularidade:** O código é organizado em pacotes e módulos (`models`, `core`, `database`).

##  Estrutura de Arquivos e Classes

O projeto está organizado da seguinte forma:

```
orientador_carreiras/
│
├── models/             # Contém as classes do modelo de dados
│   ├── carreira.py     # Define a classe Carreira
│   └── perfil.py       # Define a classe Perfil
│
├── core/               # Contém a lógica de negócio (o "cérebro")
│   └── analisador.py   # Define a classe AnalisadorCarreira
│
├── database/           # Simula o armazenamento de dados
│   └── db.py           # Contém as listas e tuplas de carreiras e competências
│
├── main.py             # Ponto de entrada (Interface CLI)
└── README.md           # Esta documentação
```

### Principais Classes

* **`models.perfil.Perfil`**:
    * **Atributos:** `nome` (str), `competencias` (dict)
    * **Métodos:** `adicionar_competencia(comp, nivel)`
* **`models.carreira.Carreira`**:
    * **Atributos:** `nome` (str), `descricao` (str), `competencias_requeridas` (dict)
* **`core.analisador.AnalisadorCarreira`**:
    * **Atributos:** `lista_carreiras` (list)
    * **Métodos:** `calcular_compatibilidade(perfil)` (função principal que processa e gera as recomendações).

##  Como Executar o Projeto

1.  **Clone o Repositório:**
    ```bash
    git clone [URL-DO-SEU-REPOSITORIO-AQUI]
    cd orientador_carreiras
    ```

2.  **Pré-requisitos:**
    * Certifique-se de ter o Python 3 (versão 3.7 ou superior) instalado.

3.  **Execute a Aplicação:**
    Não são necessárias bibliotecas externas. Basta executar o arquivo `main.py`:

    ```bash
    python main.py
    ```

4.  **Interaja com o Menu:**
    * **Opção 1:** Crie seu perfil informando seus níveis de competência (1-5).
    * **Opção 2:** Veja as recomendações de carreira e suas trilhas de aprimoramento.

## 📸 Demonstração (Exemplo de Saída)

*(Aqui você pode adicionar screenshots da sua aplicação em execução)*

**Menu Principal:**
```
====================================================
  🤖 Orientador de Carreiras do Futuro 🤖
====================================================
Conectando automação ao desenvolvimento humano.

Selecione uma opção:
1. Criar / Atualizar meu Perfil de Competências
2. Ver Recomendações de Carreira
0. Sair
====================================================
Opção: 1
```

**Análise e Recomendações:**
```
--- 2. Análise e Recomendações para [Seu Nome] ---
Analisando seu perfil contra as carreiras do futuro...

----------------------------------------------------
 Carreira: Gestor(a) de Colaboração Humano-Máquina (Match: 75.0%)
   Descrição: Otimiza a interação e colaboração entre equipes humanas e 'colegas' de IA.
    Trilhas de Aprimoramento (1):
      - Colaboracao (Necessário: 5 / Atual: 4)

----------------------------------------------------
 Carreira: Engenheiro(a) de IA Ética (Match: 50.0%)
   Descrição: Projeta sistemas de IA que são justos, transparentes e responsáveis.
    Trilhas de Aprimoramento (2):
      - Logica (Necessário: 5 / Atual: 4)
      - Pensamento_critico (Necessário: 5 / Atual: 3)
```
