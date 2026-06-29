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

        # Frame para conter o canvas e as barras de rolagem
        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)

        # Adiciona barras de rolagem
        self.hbar = ttk.Scrollbar(container, orient="horizontal")
        self.vbar = ttk.Scrollbar(container, orient="vertical")
        self.hbar.pack(side="bottom", fill="x")
        self.vbar.pack(side="right", fill="y")

        # Canvas com scrollregion grande para permitir navegação
        self.canvas = tk.Canvas(
            container, 
            bg=COR_FUNDO_CARD, 
            highlightthickness=0,
            xscrollcommand=self.hbar.set,
            yscrollcommand=self.vbar.set,
            scrollregion=(0, 0, 1200, 1000)
        )
        self.canvas.pack(side="left", fill="both", expand=True)
        
        self.hbar.config(command=self.canvas.xview)
        self.vbar.config(command=self.canvas.yview)

        # Eventos para interatividade
        self.canvas.bind("<ButtonPress-1>", self._scroll_start)
        self.canvas.bind("<B1-Motion>", self._scroll_move)
        
        # Zoom com a roda do mouse (Windows/Linux e macOS)
        self.canvas.bind("<MouseWheel>", self._zoom)
        self.canvas.bind("<Button-4>", self._zoom)
        self.canvas.bind("<Button-5>", self._zoom)

        self._zoom_level = 1.0
        self.after(100, self._desenhar_grafo)

    def _scroll_start(self, event):
        self.canvas.scan_mark(event.x, event.y)

    def _scroll_move(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)

    def _zoom(self, event):
        # Define fator de zoom baseado no evento
        if event.num == 4 or event.delta > 0:
            fator = 1.1
        elif event.num == 5 or event.delta < 0:
            fator = 0.9
        else:
            return

        # Limita zoom
        novo_zoom = self._zoom_level * fator
        if 0.5 <= novo_zoom <= 3.0:
            self._zoom_level = novo_zoom
            self.canvas.scale("all", event.x, event.y, fator, fator)
            # Atualiza a região de rolagem após o zoom
            self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def _desenhar_grafo(self):
        self.canvas.delete("all")
        regioes = listar_regioes()
        n = len(regioes)

        # Define o centro do desenho baseado na scrollregion inicial
        centro_x, centro_y = 600, 500
        raio_layout = 350
        raio_no = 6

        posicoes = {}
        for i, regiao in enumerate(regioes):
            angulo = 2 * math.pi * i / n
            x = centro_x + raio_layout * math.cos(angulo)
            y = centro_y + raio_layout * math.sin(angulo)
            posicoes[regiao] = (x, y)

        # Arestas
        for origem, conexoes in GRAFO_DF.items():
            if origem not in posicoes: continue
            x1, y1 = posicoes[origem]
            for destino, peso in conexoes:
                if destino not in posicoes: continue
                x2, y2 = posicoes[destino]
                cor = COR_DESTAQUE if peso < 0 else COR_PRIMARIA
                largura = 2 if peso < 0 else 1
                dash = (4, 4) if peso < 0 else ()
                
                self.canvas.create_line(
                    x1, y1, x2, y2, fill=cor, width=largura, dash=dash, tags="graph_element"
                )

        # Nós e rótulos
        for regiao, (x, y) in posicoes.items():
            # Nó
            self.canvas.create_oval(
                x - raio_no, y - raio_no, x + raio_no, y + raio_no, 
                fill=COR_PRIMARIA, outline=COR_TEXTO, width=1, tags="graph_element"
            )
            
            # Rótulo com deslocamento radial
            dist = math.sqrt((x - centro_x)**2 + (y - centro_y)**2)
            dx = (x - centro_x) / dist * 35 if dist > 0 else 0
            dy = (y - centro_y) / dist * 35 if dist > 0 else 0
            
            self.canvas.create_text(
                x + dx, y + dy, text=regiao, fill=COR_TEXTO, font=("Segoe UI", 9, "bold"), 
                width=100, anchor="center", justify="center", tags="graph_element"
            )

        # Centraliza a visualização inicial
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        self.canvas.xview_moveto(0.2)
        self.canvas.yview_moveto(0.2)
