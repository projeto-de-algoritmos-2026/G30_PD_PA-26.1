import math
import tkinter as tk
from tkinter import ttk

from app.data.grafo_df import GRAFO_DF, listar_regioes
from app.ui.estilo import COR_FUNDO_CARD, COR_PRIMARIA, COR_TEXTO, COR_DESTAQUE


class AbaGrafoCompleto(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, padding=20, **kwargs)
        self._montar()

    def _montar(self):
        ttk.Label(
            self, text="Malha completa de Regiões Administrativas do DF", style="Subtitulo.TLabel"
        ).pack(pady=(0, 12))

        self.canvas = tk.Canvas(self, width=820, height=560, bg=COR_FUNDO_CARD, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.after(50, self._desenhar_grafo)  # garante que o canvas já tenha tamanho real

    def _desenhar_grafo(self):
        regioes = listar_regioes()
        n = len(regioes)

        largura = self.canvas.winfo_width() or 820
        altura = self.canvas.winfo_height() or 560
        centro_x, centro_y = largura / 2, altura / 2
        raio_layout = min(largura, altura) / 2 - 70
        raio_no = 6

        posicoes = {}
        for i, regiao in enumerate(regioes):
            angulo = 2 * math.pi * i / n
            x = centro_x + raio_layout * math.cos(angulo)
            y = centro_y + raio_layout * math.sin(angulo)
            posicoes[regiao] = (x, y)

        # Arestas primeiro (para ficarem atrás dos nós)
        for origem, conexoes in GRAFO_DF.items():
            x1, y1 = posicoes[origem]
            for destino, peso in conexoes:
                x2, y2 = posicoes[destino]
                cor = COR_DESTAQUE if peso < 0 else COR_PRIMARIA
                self.canvas.create_line(x1, y1, x2, y2, fill=cor, width=1)

        # Nós e rótulos
        for regiao, (x, y) in posicoes.items():
            self.canvas.create_oval(
                x - raio_no, y - raio_no, x + raio_no, y + raio_no, fill=COR_PRIMARIA, outline=""
            )
            self.canvas.create_text(
                x, y - 14, text=regiao, fill=COR_TEXTO, font=("Segoe UI", 7), width=100
            )