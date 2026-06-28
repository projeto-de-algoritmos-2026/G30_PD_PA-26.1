from typing import Dict, List, Tuple, Optional, NamedTuple

INFINITO = float("inf")


class ResultadoBellmanFord(NamedTuple):
    """Agrupa as três saídas do algoritmo para facilitar o uso pelo chamador."""
    distancias: Dict[str, float]
    predecessores: Dict[str, Optional[str]]
    tem_ciclo_negativo: bool


def bellman_ford(grafo: Dict[str, List[Tuple[str, int]]], origem: str) -> ResultadoBellmanFord:
    """
    Executa Bellman-Ford a partir de `origem`.

    Passo a passo do algoritmo:
      1. Inicializa todas as distâncias como infinito, exceto a origem (0).
      2. Repete o relaxamento de todas as arestas (V - 1) vezes — esse é
         o número máximo de arestas que um menor caminho pode ter sem
         repetir vértices.
      3. Uma rodada extra de verificação detecta se ainda é possível
         relaxar alguma aresta — se sim, há um ciclo negativo alcançável.
    """
    vertices = list(grafo.keys())
    distancias: Dict[str, float] = {v: INFINITO for v in vertices}
    predecessores: Dict[str, Optional[str]] = {v: None for v in vertices}
    distancias[origem] = 0

    for _ in range(len(vertices) - 1):
        houve_atualizacao = False
        for u in grafo:
            if distancias[u] == INFINITO:
                continue
            for v, peso in grafo[u]:
                nova_distancia = distancias[u] + peso
                if nova_distancia < distancias[v]:
                    distancias[v] = nova_distancia
                    predecessores[v] = u
                    houve_atualizacao = True
        if not houve_atualizacao:
            break  # convergência antecipada

    tem_ciclo_negativo = _existe_relaxamento_possivel(grafo, distancias)

    return ResultadoBellmanFord(distancias, predecessores, tem_ciclo_negativo)


def _existe_relaxamento_possivel(
    grafo: Dict[str, List[Tuple[str, int]]],
    distancias: Dict[str, float],
) -> bool:
    """Verifica se ainda existe alguma aresta relaxável (indício de ciclo negativo)."""
    for u in grafo:
        if distancias[u] == INFINITO:
            continue
        for v, peso in grafo[u]:
            if distancias[u] + peso < distancias[v]:
                return True
    return False


def reconstruir_caminho(
    predecessores: Dict[str, Optional[str]], origem: str, destino: str
) -> List[str]:
    """Reconstrói a sequência de vértices da origem até o destino."""
    caminho: List[str] = []
    atual: Optional[str] = destino

    while atual is not None:
        caminho.append(atual)
        if atual == origem:
            break
        atual = predecessores[atual]

    caminho.reverse()

    if not caminho or caminho[0] != origem:
        return []  # destino inalcançável a partir da origem

    return caminho