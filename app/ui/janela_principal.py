import tkinter as tk
from tkinter import ttk

from app.ui.estilo import aplicar_estilo
from app.ui.aba_calculadora import AbaCalculadora
from app.ui.aba_grafo_completo import AbaGrafoCompleto
from app.ui.aba_tabela_distancias import AbaTabelaDistancias


class JanelaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RotaDF — Menor Caminho no Distrito Federal")
        self.geometry("900x720")
        self.minsize(820, 640)

        aplicar_estilo(self)
        self._montar_layout()

    def _montar_layout(self):
        ttk.Label(self, text="RotaDF", style="Titulo.TLabel").pack(pady=(24, 4))
        ttk.Label(
            self,
            text="Cálculo de menor rota entre Regiões Administrativas do DF · Bellman-Ford",
            style="Subtitulo.TLabel",
        ).pack(pady=(0, 16))

        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        notebook.add(AbaCalculadora(notebook), text="Calculadora de Rota")
        notebook.add(AbaGrafoCompleto(notebook), text="Grafo Completo")
        notebook.add(AbaTabelaDistancias(notebook), text="Tabela de Distâncias")