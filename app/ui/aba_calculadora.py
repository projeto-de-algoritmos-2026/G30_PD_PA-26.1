from tkinter import ttk

from app.services import rota_service
from app.ui.widgets.card_formulario import CardFormulario
from app.ui.widgets.painel_resultado import PainelResultado
from app.ui.widgets.canvas_grafo import CanvasCaminho


class AbaCalculadora(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, padding=20, **kwargs)
        self._montar()

    def _montar(self):
        regioes = rota_service.regioes_disponiveis()

        self.formulario = CardFormulario(self, regioes, on_calcular=self._ao_calcular)
        self.formulario.pack(pady=10, fill="x")

        self.painel_resultado = PainelResultado(self)
        self.painel_resultado.pack(pady=(20, 4))

        self.canvas_caminho = CanvasCaminho(self)
        self.canvas_caminho.pack(pady=16, fill="x")

    def _ao_calcular(self):
        origem = self.formulario.obter_origem()
        destino = self.formulario.obter_destino()

        if not origem or not destino:
            self.painel_resultado.exibir_erro("Selecione origem e destino.")
            return

        resultado = rota_service.calcular_rota(origem, destino)

        if not resultado.alcancavel:
            self.painel_resultado.exibir_erro(resultado.erro)
            self.canvas_caminho.limpar()
            return

        self.painel_resultado.exibir_sucesso(resultado.custo_total, len(resultado.caminho) - 1)
        self.canvas_caminho.desenhar(resultado.caminho)