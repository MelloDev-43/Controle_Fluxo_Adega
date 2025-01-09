import sqlite3
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, ttk


def init_db():
    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS mercadorias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        data_entrada TEXT NOT NULL,
        data_saida TEXT
    )
    ''')

    conn.commit()
    conn.close()


def adicionar_mercadoria(nome, quantidade):
    data_entrada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO mercadorias (nome, quantidade, data_entrada) VALUES (?, ?, ?)",
        (nome, quantidade, data_entrada)
    )

    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso", f"Mercadoria '{nome}' adicionada com sucesso.")


def registrar_saida(id_mercadoria, quantidade):
    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()

    cursor.execute("SELECT quantidade FROM mercadorias WHERE id = ?", (id_mercadoria,))
    resultado = cursor.fetchone()

    if resultado:
        quantidade_atual = resultado[0]
        if quantidade_atual >= quantidade:
            nova_quantidade = quantidade_atual - quantidade
            data_saida = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute(
                "UPDATE mercadorias SET quantidade = ?, data_saida = ? WHERE id = ?",
                (nova_quantidade, data_saida, id_mercadoria)
            )
            conn.commit()
            messagebox.showinfo("Sucesso", f"Saída de {quantidade} unidades registrada com sucesso.")
        else:
            messagebox.showwarning("Erro", "Quantidade insuficiente em estoque.")
    else:
        messagebox.showerror("Erro", "Mercadoria não encontrada.")

    conn.close()


def listar_mercadorias():
    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM mercadorias")
    mercadorias = cursor.fetchall()

    if mercadorias:
        lista.delete(*lista.get_children())
        for mercadoria in mercadorias:
            id_, nome, quantidade, data_entrada, data_saida = mercadoria
            quantidade_tag = "normal"
            if quantidade < 5:
                quantidade_tag = "baixo"
            elif quantidade < 10:
                quantidade_tag = "alerta"
            lista.insert("", "end", values=mercadoria, tags=(quantidade_tag,))
    else:
        messagebox.showinfo("Informação", "Nenhuma mercadoria encontrada.")

    conn.close()


def adicionar_mercadoria_ui():
    nome = entrada_nome.get()
    try:
        quantidade = int(entrada_quantidade.get())
        if nome and quantidade > 0:
            adicionar_mercadoria(nome, quantidade)
            listar_mercadorias()
        else:
            messagebox.showwarning("Erro", "Preencha os campos corretamente.")
    except ValueError:
        messagebox.showerror("Erro", "A quantidade deve ser um número inteiro.")


def registrar_saida_ui():
    try:
        id_mercadoria = int(entrada_id.get())
        quantidade = int(entrada_saida_quantidade.get())
        if id_mercadoria > 0 and quantidade > 0:
            registrar_saida(id_mercadoria, quantidade)
            listar_mercadorias()
        else:
            messagebox.showwarning("Erro", "Preencha os campos corretamente.")
    except ValueError:
        messagebox.showerror("Erro", "Os campos ID e quantidade devem ser números inteiros.")


init_db()
root = tk.Tk()
root.title("Controle de Fluxo de Mercadorias")


frame_adicionar = tk.LabelFrame(root, text="Adicionar Mercadoria")
frame_adicionar.pack(fill="x", padx=10, pady=5)

tk.Label(frame_adicionar, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
entrada_nome = tk.Entry(frame_adicionar)
entrada_nome.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_adicionar, text="Quantidade:").grid(row=1, column=0, padx=5, pady=5)
entrada_quantidade = tk.Entry(frame_adicionar)
entrada_quantidade.grid(row=1, column=1, padx=5, pady=5)

tk.Button(frame_adicionar, text="Adicionar", command=adicionar_mercadoria_ui).grid(row=2, column=0, columnspan=2, pady=5)


frame_saida = tk.LabelFrame(root, text="Registrar Saída")
frame_saida.pack(fill="x", padx=10, pady=5)

tk.Label(frame_saida, text="ID:").grid(row=0, column=0, padx=5, pady=5)
entrada_id = tk.Entry(frame_saida)
entrada_id.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_saida, text="Quantidade:").grid(row=1, column=0, padx=5, pady=5)
entrada_saida_quantidade = tk.Entry(frame_saida)
entrada_saida_quantidade.grid(row=1, column=1, padx=5, pady=5)

tk.Button(frame_saida, text="Registrar Saída", command=registrar_saida_ui).grid(row=2, column=0, columnspan=2, pady=5)


frame_lista = tk.LabelFrame(root, text="Lista de Mercadorias")
frame_lista.pack(fill="both", expand=True, padx=10, pady=5)

colunas = ("ID", "Nome", "Quantidade", "Data Entrada", "Data da ultima Saída")
lista = ttk.Treeview(frame_lista, columns=colunas, show="headings")
for col in colunas:
    lista.heading(col, text=col)
    lista.column(col, width=100)

lista.tag_configure("baixo", background="red", foreground="white")
lista.tag_configure("alerta", background="yellow", foreground="black")
lista.tag_configure("normal", background="white", foreground="black")

lista.pack(fill="both", expand=True)

listar_mercadorias()

root.mainloop()
