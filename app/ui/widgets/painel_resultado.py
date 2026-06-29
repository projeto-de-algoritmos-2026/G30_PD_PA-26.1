from tkinter import ttk


class PainelResultado(ttk.Label):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, text="", style="Subtitulo.TLabel", **kwargs)

    def exibir_sucesso(self, custo_total: float, quantidade_trechos: int):
        self.configure(
            text=f"Custo total: {custo_total}  ·  {quantidade_trechos} trecho(s)",
            style="Resultado.TLabel",
        )

    def exibir_erro(self, mensagem: str):
        self.configure(text=mensagem, style="Erro.TLabel")

    def limpar(self):
        self.configure(text="", style="Subtitulo.TLabel")