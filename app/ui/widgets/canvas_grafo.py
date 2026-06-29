import tkinter as tk
from typing import List

from app.ui.estilo import COR_FUNDO_CARD, COR_PRIMARIA, COR_DESTAQUE, COR_TEXTO


class CanvasCaminho(tk.Canvas):
    def __init__(self, parent, largura: int = 780, altura: int = 260, **kwargs):
        super().__init__(parent, width=largura, height=altura, bg=COR_FUNDO_CARD, highlightthickness=0, **kwargs)
        self._largura = largura
        self._altura = altura

    def desenhar(self, caminho: List[str]):
        self.delete("all")

        n = len(caminho)
        if n == 0:
            return

        raio = 26
        margem = 60
        espacamento = (self._largura - 2 * margem) / max(n - 1, 1)
        y = self._altura // 2

        coordenadas = [(margem + i * espacamento, y) for i in range(n)]

        for i in range(n - 1):
            x1, y1 = coordenadas[i]
            x2, y2 = coordenadas[i + 1]
            self.create_line(
                x1 + raio, y1, x2 - raio, y2,
                fill=COR_PRIMARIA, width=3, arrow=tk.LAST, arrowshape=(12, 14, 6),
            )

        for i, (x, y) in enumerate(coordenadas):
            cor_no = COR_DESTAQUE if i in (0, n - 1) else COR_PRIMARIA
            self.create_oval(x - raio, y - raio, x + raio, y + raio, fill=cor_no, outline="")
            self.create_text(x, y, text=str(i + 1), fill="white", font=("Segoe UI", 11, "bold"))
            self.create_text(
                x, y + raio + 18, text=caminho[i], fill=COR_TEXTO,
                font=("Segoe UI", 9), width=max(int(espacamento), 90),
            )

    def limpar(self):
        self.delete("all")