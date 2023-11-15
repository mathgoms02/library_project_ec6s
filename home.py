import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from bd_project import tela_livros


password = "microondas123@"

def tela_home(usuario):
    # Conexão com o banco de dados
    username = usuario
    def create_server_connection(host_name, user_name, user_password, database):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=database
            )
            print("MySQL Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")
        return connection

    conn = create_server_connection("localhost", "root", password, "biblioteca")
    cursor = conn.cursor()

    # Obtendo dados da tabela
    cursor.execute("SELECT * FROM livros_usuarios")
    rows = cursor.fetchall()

    # Criando a janela principal
    root = tk.Tk()
    root.title('Biblioteca')
    root.geometry('1920x1080')
    root.configure(background='#FFFACD')

    marginSup = Canvas(root, width=1920, bg='#A52A2A', height=15, bd=0, highlightthickness=0, relief='ridge')
    marginSup.pack()

    library_name = Label(root, bg='#FFFACD', text='LITERAPICE', fg='#000000', font=('Montserrat', 15, 'bold'))
    library_name.pack()

    text_id = Label(root, bg='#FFFACD', text='Bem vindo ' + username, fg='#000000', font=('Montserrat', 15, 'bold'))
    text_id.pack()

    # Criando estilo para a tabela
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview",
                    background="#FFFFFF",
                    foreground="black",
                    fieldbackground="#FFFFFF")
    style.map("Treeview",
              background=[('selected', '#008B8B')])

    # Criando a tabela
    tabela = ttk.Treeview(root)
    tabela["columns"] = ("IdLivro", "titulo", "autor", "ano", "genero", "preco")

    # Formatando as colunas
    tabela.column("#0", width=0, stretch=tk.NO)  # Coluna vazia (facilitar contagem)
    tabela.column("IdLivro", width=80, anchor="center")
    tabela.column("titulo", width=200, anchor="w")
    tabela.column("autor", width=150, anchor="w")
    tabela.column("ano", width=80, anchor="center")
    tabela.column("genero", width=150, anchor="w")
    tabela.column("preco", width=80, anchor="center")

    # Definindo os cabeçalhos
    tabela.heading("#0", text="", anchor=tk.W)  # Coluna vazia
    tabela.heading("IdLivro", text="IdLivro", anchor=tk.W)
    tabela.heading("titulo", text="Título", anchor=tk.W)
    tabela.heading("autor", text="Autor", anchor=tk.W)
    tabela.heading("ano", text="Ano", anchor=tk.W)
    tabela.heading("genero", text="Gênero", anchor=tk.W)
    tabela.heading("preco", text="Preço", anchor=tk.W)

    # Posicionando a tabela
    tabela.pack(pady=20)

    # Botão Pesquisar
    def botao_pesquisar():
        conn2 = create_server_connection("localhost", "root", password, "biblioteca")
        cursor2 = conn2.cursor()

        valor = caixa_texto1.get()
        cursor2.execute("SELECT * FROM livros_disponiveis WHERE titulo LIKE %s", ('%' + valor + '%',))
        resultados = cursor2.fetchall()

        tabela.delete(*tabela.get_children())

        for livro in resultados:
            tabela.insert("", tk.END, values=livro)

        conn2.close()

    # Botão Loja
    def to_loja():
        tela_livros(username)
    
    def restaurar_table():
        tabela.delete(*tabela.get_children())
        conn = create_server_connection("localhost", "root", password, "biblioteca")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM livros_usuarios")
        rows = cursor.fetchall()
        for i, (IdLivro, titulo, autor, ano, genero, preco) in enumerate(rows, start=1):
            tabela.insert("", tk.END, text=str(i), values=(IdLivro, titulo, autor, ano, genero, preco))
        conn.close()

    # Labels e Entradas de Texto
    text1 = Label(root, bg='#FFFACD', text='Pesquisar:', fg='#000000', font=('Montserrat', 12, 'bold'))
    text1.pack(pady=5)
    caixa_texto1 = tk.Entry(root)
    caixa_texto1.pack(pady=5)

    botaoClear = Button(root, text="↺", command=restaurar_table)
    botaoClear.pack(pady=10)

    text3 = Label(root, bg='#FFFACD', text='Unidades:', fg='#000000', font=('Montserrat', 12, 'bold'))
    text3.pack(pady=5)
    caixa_texto2 = tk.Entry(root)
    caixa_texto2.pack(pady=5)

    # Botões
    botaoPesquisar = Button(root, text="Pesquisar", width=15, font=('Montserrat', 12), command=botao_pesquisar)
    botaoPesquisar.configure(bg="#FFDAB9", fg="black", relief="raised", padx=10, pady=5, activebackground="#008B8B")
    botaoPesquisar.pack(pady=10)

    botaoLoja = Button(root, text="Loja", width=10, font=('Montserrat', 12), command=to_loja)
    botaoLoja.configure(bg="#FFDAB9", fg="black", relief="raised", padx=10, pady=5, activebackground="#008B8B")
    botaoLoja.pack(pady=10)

    # Mostrando os dados na tabela
    for i, (IdLivro, titulo, autor, ano, genero, preco) in enumerate(rows, start=1):
        tabela.insert("", tk.END, text=str(i), values=(IdLivro, titulo, autor, ano, genero, preco))

    conn.close()
    root.mainloop()