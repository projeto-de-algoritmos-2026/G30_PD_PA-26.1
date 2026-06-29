from tkinter import ttk

from app.service import rota_service


class AbaTabelaDistancias(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, padding=20, **kwargs)
        self._montar()

    def _montar(self):
        topo = ttk.Frame(self)
        topo.pack(fill="x", pady=(0, 16))

        ttk.Label(topo, text="Origem:", style="Subtitulo.TLabel").pack(side="left", padx=(0, 10))

        regioes = rota_service.regioes_disponiveis()
        self.combo_origem = ttk.Combobox(topo, values=regioes, state="readonly", width=28)
        self.combo_origem.pack(side="left")

        botao = ttk.Button(topo, text="Gerar tabela", style="Primario.TButton", command=self._ao_gerar)
        botao.pack(side="left", padx=16)

        colunas = ("regiao", "custo")
        self.tabela = ttk.Treeview(self, columns=colunas, show="headings", height=16)
        self.tabela.heading("regiao", text="Região Administrativa")
        self.tabela.heading("custo", text="Custo a partir da origem")
        self.tabela.column("regiao", width=320)
        self.tabela.column("custo", width=200, anchor="center")
        self.tabela.pack(fill="both", expand=True)

    def _ao_gerar(self):
        origem = self.combo_origem.get()
        if not origem:
            return

        for linha in self.tabela.get_children():
            self.tabela.delete(linha)

        distancias = rota_service.obter_tabela_de_distancias(origem)

        # Ordena por custo (inalcançáveis — infinito — vão para o final)
        itens_ordenados = sorted(distancias.items(), key=lambda item: item[1])

        for regiao, custo in itens_ordenados:
            texto_custo = "Inalcançável" if custo == float("inf") else str(custo)
            self.tabela.insert("", "end", values=(regiao, texto_custo))