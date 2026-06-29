"""
Identidade visual da aplicação RotaDF: paleta de cores (tema escuro)
e estilos ttk reutilizáveis pelos widgets e abas.
"""
from tkinter import ttk

# Paleta de cores
COR_FUNDO = "#0f1b2d"
COR_FUNDO_CARD = "#16243b"
COR_FUNDO_CARD_CLARO = "#1d3050"
COR_PRIMARIA = "#2e8bf0"
COR_PRIMARIA_HOVER = "#4fa3ff"
COR_TEXTO = "#eaf1fb"
COR_TEXTO_SECUNDARIO = "#9fb3c8"
COR_DESTAQUE = "#22c98f"
COR_ERRO = "#e35d6a"
COR_BORDA = "#26395c"

FONTE_PADRAO = ("Segoe UI", 10)
FONTE_TITULO = ("Segoe UI", 24, "bold")
FONTE_SUBTITULO = ("Segoe UI", 11)


def aplicar_estilo(root) -> ttk.Style:
    root.configure(bg=COR_FUNDO)

    estilo = ttk.Style(root)
    estilo.theme_use("clam")

    estilo.configure(".", background=COR_FUNDO, foreground=COR_TEXTO, font=FONTE_PADRAO)

    estilo.configure("Titulo.TLabel", background=COR_FUNDO, foreground=COR_TEXTO, font=FONTE_TITULO)
    estilo.configure("Subtitulo.TLabel", background=COR_FUNDO, foreground=COR_TEXTO_SECUNDARIO, font=FONTE_SUBTITULO)

    estilo.configure("Card.TFrame", background=COR_FUNDO_CARD, relief="flat")
    estilo.configure("Card.TLabel", background=COR_FUNDO_CARD, foreground=COR_TEXTO, font=("Segoe UI", 10, "bold"))
    estilo.configure("CardTexto.TLabel", background=COR_FUNDO_CARD, foreground=COR_TEXTO_SECUNDARIO)

    estilo.configure("TCombobox", padding=8)
    estilo.configure("Campo.TCombobox", padding=(10, 8), arrowsize=16,
                      fieldbackground=COR_FUNDO_CARD_CLARO, background=COR_FUNDO_CARD_CLARO)
    estilo.map("Campo.TCombobox",
               fieldbackground=[("readonly", COR_FUNDO_CARD_CLARO)],
               background=[("readonly", COR_FUNDO_CARD_CLARO)],
               foreground=[("readonly", COR_TEXTO)])

    estilo.configure("Primario.TButton", font=("Segoe UI", 10, "bold"), padding=10,
                      background=COR_PRIMARIA, foreground="white", borderwidth=0)
    estilo.map("Primario.TButton",
               background=[("active", COR_PRIMARIA_HOVER)],
               foreground=[("active", "white")])

    estilo.configure("Resultado.TLabel", background=COR_FUNDO, foreground=COR_DESTAQUE, font=("Segoe UI", 13, "bold"))
    estilo.configure("Erro.TLabel", background=COR_FUNDO, foreground=COR_ERRO, font=("Segoe UI", 11, "bold"))

    # Abas (Notebook)
    estilo.configure("TNotebook", background=COR_FUNDO, borderwidth=0)
    estilo.configure("TNotebook.Tab", background=COR_FUNDO_CARD, foreground=COR_TEXTO_SECUNDARIO,
                      padding=(18, 10), font=("Segoe UI", 10, "bold"))
    estilo.map("TNotebook.Tab",
               background=[("selected", COR_PRIMARIA)],
               foreground=[("selected", "white")])

    # Tabela (Treeview)
    estilo.configure("Treeview", background=COR_FUNDO_CARD, fieldbackground=COR_FUNDO_CARD,
                      foreground=COR_TEXTO, rowheight=28, borderwidth=0)
    estilo.configure("Treeview.Heading", background=COR_FUNDO_CARD_CLARO, foreground=COR_TEXTO,
                      font=("Segoe UI", 10, "bold"))
    estilo.map("Treeview", background=[("selected", COR_PRIMARIA)])

    return estilo