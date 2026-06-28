"""
Widget reutilizável: card com seletores de origem/destino e botão de ação.
Não conhece o algoritmo — apenas expõe os valores selecionados e aceita
um callback a ser executado quando o botão é clicado.
"""
from tkinter import ttk
from typing import Callable, List


class CardFormulario(ttk.Frame):
    def __init__(self, parent, regioes: List[str], on_calcular: Callable[[], None], **kwargs):
        super().__init__(parent, style="Card.TFrame", padding=24, **kwargs)
        self._montar(regioes, on_calcular)

    def _montar(self, regioes: List[str], on_calcular: Callable[[], None]):
        ttk.Label(self, text="Origem", style="Card.TLabel").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.combo_origem = ttk.Combobox(self, values=regioes, state="readonly", width=24)
        self.combo_origem.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(self, text="Destino", style="Card.TLabel").grid(row=0, column=2, padx=10, pady=10, sticky="w")
        self.combo_destino = ttk.Combobox(self, values=regioes, state="readonly", width=24)
        self.combo_destino.grid(row=0, column=3, padx=10, pady=10)

        self.botao_calcular = ttk.Button(self, text="Calcular rota", style="Primario.TButton", command=on_calcular)
        self.botao_calcular.grid(row=0, column=4, padx=(20, 10))

    def obter_origem(self) -> str:
        return self.combo_origem.get()

    def obter_destino(self) -> str:
        return self.combo_destino.get()