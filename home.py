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
    
    # def restaurar_table():
    #     tabela.delete(*tabela.get_children())
    #     conn = create_server_connection("localhost", "root", password, "biblioteca")
    #     cursor2 = conn.cursor()
    #     cursor2.execute("SELECT ld.titulo, ld.autor, u.nomeUsuario FROM livros_disponiveis ld JOIN livros_usuarios lu ON ld.idLivro = lu.fk_idLivro JOIN usuarios u ON lu.fk_idUsuario = u.idUsuario WHERE u.nomeUsuario =%s;", (username,))
    #     rows2 = cursor2.fetchall()
    #     for i, (titulo, autor) in enumerate(rows2, start=1):
    #         tabela.insert("", tk.END, text=str(i), values=(titulo, autor))
    #     # conn.close()

    conn = create_server_connection("localhost", "root", password, "biblioteca")
    cursor = conn.cursor()

    # Obtendo dados da tabela
    cursor.execute("SELECT ld.titulo, ld.autor, u.nomeUsuario FROM livros_disponiveis ld JOIN livros_usuarios lu ON ld.idLivro = lu.fk_idLivro JOIN usuarios u ON lu.fk_idUsuario = u.idUsuario WHERE u.nomeUsuario =%s;", (username,))
    rows = cursor.fetchall()


    # Criando a janela principal
    root = tk.Tk()
    root.title('Biblioteca')
    root.state('zoomed')  # Abre maximizado
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
    tabela["columns"] = ("titulo", "autor")

    # Formatando as colunas
    tabela.column("#0", width=0, stretch=tk.NO)  # Coluna vazia (facilitar contagem)
    tabela.column("titulo", width=200, anchor="w")
    tabela.column("autor", width=150, anchor="w")


    # Definindo os cabeçalhos
    tabela.heading("#0", text="", anchor=tk.W)  # Coluna vazia
    tabela.heading("titulo", text="Título", anchor=tk.W)
    tabela.heading("autor", text="Autor", anchor=tk.W)

    # Posicionando a tabela
    tabela.pack(pady=20)

    # # Botão Pesquisar
    # def botao_pesquisar():
    #     conn2 = create_server_connection("localhost", "root", password, "biblioteca")
    #     cursor2 = conn2.cursor()

    #     valor = caixa_texto1.get()
    #     cursor2.execute("SELECT * FROM livros_ WHERE titulo LIKE %s", ('%' + valor + '%',))
    #     resultados = cursor2.fetchall()

    #     tabela.delete(*tabela.get_children())

    #     for livro in resultados:
    #         tabela.insert("", tk.END, values=livro)

    #     conn2.close()

    # Botão Loja
    def to_loja():
        tela_livros(username)
    
    def restaurar_table():
        username = usuario
        tabela.delete(*tabela.get_children())
        conn = create_server_connection("localhost", "root", password, "biblioteca")
        cursor = conn.cursor()
        cursor.execute("SELECT ld.titulo, ld.autor, u.nomeUsuario FROM livros_disponiveis ld JOIN livros_usuarios lu ON ld.idLivro = lu.fk_idLivro JOIN usuarios u ON lu.fk_idUsuario = u.idUsuario WHERE u.nomeUsuario =%s;", (username,)) #################MUDAR QUERY###############
        rows = cursor.fetchall()
        for i, (titulo, autor, username) in enumerate(rows, start=1):
            tabela.insert("", tk.END, text=str(i), values=(titulo, autor, username))
        conn.close()

    # Labels e Entradas de Texto
    # text1 = Label(root, bg='#FFFACD', text='Pesquisar:', fg='#000000', font=('Montserrat', 12, 'bold'))
    # text1.pack(pady=5)
    # caixa_texto1 = tk.Entry(root)
    # caixa_texto1.pack(pady=5)

    botaoClear = Button(root, text="↺", command=restaurar_table)
    botaoClear.pack(pady=10)

    text3 = Label(root, bg='#FFFACD', text='Unidades:', fg='#000000', font=('Montserrat', 12, 'bold'))
    text3.pack(pady=5)
    caixa_texto2 = tk.Entry(root)
    caixa_texto2.pack(pady=5)

    # # Botões
    # botaoPesquisar = Button(root, text="Pesquisar", width=15, font=('Montserrat', 12), command=botao_pesquisar)
    # botaoPesquisar.configure(bg="#FFDAB9", fg="black", relief="raised", padx=10, pady=5, activebackground="#008B8B")
    # botaoPesquisar.pack(pady=10)

    botaoLoja = Button(root, text="Loja", width=10, font=('Montserrat', 12), command=to_loja)
    botaoLoja.configure(bg="#FFDAB9", fg="black", relief="raised", padx=10, pady=5, activebackground="#008B8B")
    botaoLoja.pack(pady=10)

    # Mostrando os dados na tabela
    for i, (titulo, autor, username) in enumerate(rows, start=1):
        tabela.insert("", tk.END, text=str(i), values=(titulo, autor, username))

    conn.close()
    root.mainloop()