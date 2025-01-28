import tkinter as tk
from PIL import ImageTk, Image

def criar_janela():
    janela = tk.Tk()
    janela.title("Cadastro")

    # Carregar o ícone
    icon = Image.open("img.png")
    photo = ImageTk.PhotoImage(icon)
    janela.iconphoto(False, photo)

    # Definir tamanho fixo e desabilitar redimensionamento
    largura, altura = 400, 250
    janela.geometry(f"{largura}x{altura}")
    janela.resizable(False, False)

    # Criar o título no topo com fundo verde e letra branca
    titulo = tk.Label(janela, text="CADASTRO", font=("Arial", 24), bg="green", fg="white", pady=10)
    titulo.pack(fill="x", side="top")

    # Criar o frame principal para centralizar os campos
    frame_conteudo = tk.Frame(janela)
    frame_conteudo.pack(expand=True)

    # Criar os elementos da interface com layout ajustado e centralizado
    frame_nome = tk.Frame(frame_conteudo)
    label_nome = tk.Label(frame_nome, text="Nome:", anchor="w", width=15)
    entry_nome = tk.Entry(frame_nome)
    label_nome.grid(row=0, column=0, padx=10, sticky="w")
    entry_nome.grid(row=0, column=1, padx=10)
    frame_nome.pack(fill="x", pady=5)

    frame_email = tk.Frame(frame_conteudo)
    label_email = tk.Label(frame_email, text="E-mail:", anchor="w", width=15)
    entry_email = tk.Entry(frame_email)
    label_email.grid(row=0, column=0, padx=10, sticky="w")
    entry_email.grid(row=0, column=1, padx=10)
    frame_email.pack(fill="x", pady=5)

    frame_senha = tk.Frame(frame_conteudo)
    label_senha = tk.Label(frame_senha, text="Senha:", anchor="w", width=15)
    entry_senha = tk.Entry(frame_senha, show="*")
    label_senha.grid(row=0, column=0, padx=10, sticky="w")
    entry_senha.grid(row=0, column=1, padx=10)
    frame_senha.pack(fill="x", pady=5)

    frame_confirmar_senha = tk.Frame(frame_conteudo)
    label_confirmar_senha = tk.Label(frame_confirmar_senha, text="Confirmar Senha:", anchor="w", width=15)
    entry_confirmar_senha = tk.Entry(frame_confirmar_senha, show="*")
    label_confirmar_senha.grid(row=0, column=0, padx=10, sticky="w")
    entry_confirmar_senha.grid(row=0, column=1, padx=10)
    frame_confirmar_senha.pack(fill="x", pady=5)

    # Botão cadastrar com fundo verde e letra branca
    botao_cadastrar = tk.Button(janela, text="Cadastrar", bg="green", fg="white", font=("Arial", 12))
    botao_cadastrar.pack(pady=20)

    janela.mainloop()


criar_janela()
