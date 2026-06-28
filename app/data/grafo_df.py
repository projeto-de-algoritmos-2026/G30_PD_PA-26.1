from typing import Dict, List, Tuple

GrafoTipo = Dict[str, List[Tuple[str, int]]]


GRAFO_DF: GrafoTipo = {
    "Plano Piloto": [
        ("Lago Sul", 8), ("Lago Norte", 9), ("Núcleo Bandeirante", 10),
        ("Cruzeiro", 7), ("Sudoeste/Octogonal", 6), ("Varjão", 12), ("Paranoá", 18),
    ],
    "Cruzeiro": [("Plano Piloto", 7), ("Sudoeste/Octogonal", 4), ("Águas Claras", 9)],
    "Sudoeste/Octogonal": [("Cruzeiro", 4), ("Guará", 5), ("Núcleo Bandeirante", 7)],
    "Guará": [("Sudoeste/Octogonal", 5), ("Núcleo Bandeirante", 4), ("Águas Claras", -2)],
    "Núcleo Bandeirante": [
        ("Plano Piloto", 10), ("Guará", 4), ("Riacho Fundo", 5),
        ("Candangolândia", 3), ("Park Way", 6),
    ],
    "Candangolândia": [("Núcleo Bandeirante", 3), ("Riacho Fundo", 4)],
    "Riacho Fundo": [("Núcleo Bandeirante", 5), ("Riacho Fundo II", 6), ("Recanto das Emas", 8)],
    "Riacho Fundo II": [("Riacho Fundo", 6), ("Recanto das Emas", 5)],
    "Park Way": [("Núcleo Bandeirante", 6), ("Gama", 12), ("São Sebastião", 16)],
    "Águas Claras": [("Guará", -2), ("Taguatinga", -3), ("Vicente Pires", 4)],
    "Vicente Pires": [("Águas Claras", 4), ("Taguatinga", 5)],
    "Taguatinga": [
        ("Águas Claras", -3), ("Vicente Pires", 5), ("Ceilândia", 6),
        ("Samambaia", 11), ("Brazlândia", 19),
    ],
    "Ceilândia": [("Taguatinga", 6), ("Brazlândia", 14), ("Samambaia", 8), ("Sol Nascente/Pôr do Sol", 5)],
    "Sol Nascente/Pôr do Sol": [("Ceilândia", 5), ("Brazlândia", 12)],
    "Brazlândia": [("Ceilândia", 14), ("Taguatinga", 19)],
    "Samambaia": [("Ceilândia", 8), ("Taguatinga", 11), ("Recanto das Emas", 6)],
    "Recanto das Emas": [("Samambaia", 6), ("Riacho Fundo", 8), ("Riacho Fundo II", 5), ("Gama", 9)],
    "Gama": [("Park Way", 12), ("Recanto das Emas", 9), ("Santa Maria", 7)],
    "Santa Maria": [("Gama", 7), ("São Sebastião", 10)],
    "São Sebastião": [("Park Way", 16), ("Santa Maria", 10), ("Jardim Botânico", 11), ("Paranoá", 9)],
    "Jardim Botânico": [("São Sebastião", 11), ("Lago Sul", 13), ("Paranoá", 8)],
    "Paranoá": [("Plano Piloto", 18), ("São Sebastião", 9), ("Jardim Botânico", 8), ("Itapoã", 6)],
    "Itapoã": [("Paranoá", 6), ("Varjão", 7)],
    "Varjão": [("Plano Piloto", 12), ("Itapoã", 7), ("Lago Norte", 6)],
    "Lago Norte": [("Plano Piloto", 9), ("Varjão", 6), ("Sobradinho", 13)],
    "Lago Sul": [("Plano Piloto", 8), ("Jardim Botânico", 13), ("São Sebastião", 15)],
    "Sobradinho": [("Lago Norte", 13), ("Sobradinho II", 4), ("Planaltina", 16), ("Fercal", 10)],
    "Sobradinho II": [("Sobradinho", 4), ("Fercal", 8)],
    "Planaltina": [("Sobradinho", 16)],
    "Fercal": [("Sobradinho", 10), ("Sobradinho II", 8)],
}


def listar_regioes() -> List[str]:
    """Retorna a lista ordenada de Regiões Administrativas do grafo."""
    return sorted(GRAFO_DF.keys())


def total_regioes() -> int:
    return len(GRAFO_DF)