# database/db.py
from models.carreira import Carreira

# Usamos uma TUPLA para armazenar as competências-base que o sistema conhece.
# Isso garante que elas sejam imutáveis.
COMPETENCIAS_BASE = (
    "logica",
    "criatividade",
    "colaboracao",
    "adaptabilidade",
    "comunicacao",
    "lideranca",
    "pensamento_critico",
    "ia_ml"  # Competência em Inteligência Artificial / Machine Learning
)

# Usamos uma LISTA de objetos Carreira para simular nosso banco de dados.
CARREIRAS_DB = [
    Carreira(
        nome="Engenheiro(a) de IA Ética",
        descricao="Projeta sistemas de IA que são justos, transparentes e responsáveis.",
        # Dicionário de competências requeridas (nível mínimo 1-5)
        competencias_requeridas={"logica": 5, "pensamento_critico": 5, "ia_ml": 4, "adaptabilidade": 3}
    ),
    Carreira(
        nome="Designer de Experiência de Realidade Mista (MR/VR/AR)",
        descricao="Cria experiências imersivas para usuários em ambientes virtuais ou aumentados.",
        competencias_requeridas={"criatividade": 5, "logica": 3, "colaboracao": 4, "adaptabilidade": 4}
    ),
    Carreira(
        nome="Gestor(a) de Colaboração Humano-Máquina",
        descricao="Otimiza a interação e colaboração entre equipes humanas e 'colegas' de IA.",
        competencias_requeridas={"colaboracao": 5, "lideranca": 4, "comunicacao": 5, "ia_ml": 2, "adaptabilidade": 4}
    ),
    Carreira(
        nome="Especialista em Sustentabilidade Digital",
        descricao="Analisa e otimiza o impacto ambiental de tecnologias e infraestruturas digitais.",
        competencias_requeridas={"pensamento_critico": 4, "logica": 4, "adaptabilidade": 3, "colaboracao": 3}
    ),
    Carreira(
        nome="Terapeuta de Detoque Digital",
        descricao="Ajuda indivíduos a criar relações mais saudáveis com a tecnologia.",
        competencias_requeridas={"comunicacao": 5, "pensamento_critico": 4, "lideranca": 3, "adaptabilidade": 5}
    )
]