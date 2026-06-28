from dataclasses import dataclass
from typing import List, Dict

from app.data.grafo_df import GRAFO_DF, listar_regioes
from app.domain.bellman_ford import bellman_ford, reconstruir_caminho


@dataclass
class ResultadoRota:
    """Representa o resultado de uma consulta de rota, já pronto para exibição."""
    origem: str
    destino: str
    alcancavel: bool
    custo_total: float = 0
    caminho: List[str] = None
    erro: str = ""

    def __post_init__(self):
        if self.caminho is None:
            self.caminho = []


def regioes_disponiveis() -> List[str]:
    return listar_regioes()


def calcular_rota(origem: str, destino: str) -> ResultadoRota:
    """
    Calcula a menor rota entre duas RAs do DF.
    Trata os casos de erro (seleção inválida, ciclo negativo,
    destino inalcançável) e devolve sempre um ResultadoRota coerente.
    """
    if origem not in GRAFO_DF or destino not in GRAFO_DF:
        return ResultadoRota(origem, destino, alcancavel=False, erro="Região desconhecida.")

    if origem == destino:
        return ResultadoRota(origem, destino, alcancavel=False, erro="Origem e destino são iguais.")

    resultado = bellman_ford(GRAFO_DF, origem)

    if resultado.tem_ciclo_negativo:
        return ResultadoRota(origem, destino, alcancavel=False, erro="Ciclo negativo detectado no grafo.")

    custo = resultado.distancias[destino]
    if custo == float("inf"):
        return ResultadoRota(origem, destino, alcancavel=False, erro="Destino inalcançável a partir da origem.")

    caminho = reconstruir_caminho(resultado.predecessores, origem, destino)

    return ResultadoRota(origem, destino, alcancavel=True, custo_total=custo, caminho=caminho)


def obter_tabela_de_distancias(origem: str) -> Dict[str, float]:
    """
    Retorna o custo da origem até TODAS as demais regiões — útil para
    a aba de tabela comparativa. As regiões inalcançáveis vêm com
    valor infinito.
    """
    if origem not in GRAFO_DF:
        return {}

    resultado = bellman_ford(GRAFO_DF, origem)
    return resultado.distancias