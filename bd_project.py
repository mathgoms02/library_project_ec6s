import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from deznanota import easteregg
from carrinho import tela_carrinho


password = "microondas123@"

def tela_livros(usuario):
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
    cursor.execute("SELECT * FROM livros_disponiveis")
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

    text_id = Label(root, bg='#FFFACD', text='Livros disponíveis:', fg='#000000', font=('Montserrat', 15, 'bold'))
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

    # Botão Carrinho
    def to_carrinho():
        tela_carrinho(username)

    def id_usuario(username):
        conn4 = create_server_connection("localhost", "root", password, "biblioteca")
        cursor4 = conn4.cursor()

        query4 = "SELECT idUsuario FROM usuarios WHERE nomeUsuario = %s"
        cursor4.execute(query4, (username,))
        resultado = cursor4.fetchone()

        # Verificar se o usuário foi encontrado
        if resultado:
            idUsuario = resultado[0]
        else:
            messagebox.showinfo("Erro", "Usuário não encontrado")
            idUsuario = None

        # Fechar o cursor e a conexão com o banco de dados
        cursor4.close()
        conn4.close()

        return idUsuario
        
    idUser = id_usuario(username)
    

    # Botão Adicionar no Carrinho
    def add_carrinho():
        try:
            item_selecionado = tabela.selection()
            if item_selecionado:
                valores_selecionados = tabela.item(item_selecionado)["values"]
                idLivro_loja = valores_selecionados[0]
                titulo = valores_selecionados[1]
                autor = valores_selecionados[2]
                ano = valores_selecionados[3]
                genero = valores_selecionados[4]

                preco = float(valores_selecionados[5])


                conn3 = create_server_connection("localhost", "root", password, "biblioteca")
                cursor3 = conn3.cursor()

                query = "INSERT INTO carrinho (idCarrinho_Usuario, idLivro_loja, titulo, autor, ano, genero, preco) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                values = (idUser, idLivro_loja, titulo, autor, ano, genero, preco)
                cursor3.execute(query, values)
                conn3.commit()

                messagebox.showinfo("SUCESSO", "Adicionado com sucesso ao carrinho")

        except Error as err:
            messagebox.showinfo("Error", str(err))
        finally:
            if conn3.is_connected():
                cursor3.close()
                conn3.close()


    def restaurar_table():
        tabela.delete(*tabela.get_children())
        conn = create_server_connection("localhost", "root", password, "biblioteca")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM livros_disponiveis")
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

    # Botões
    botaoPesquisar = Button(root, text="Pesquisar", width=15, font=('Montserrat', 12), command=botao_pesquisar)
    botaoPesquisar.configure(bg="#FFDAB9", fg="black", relief="raised", padx=10, pady=5, activebackground="#008B8B")
    botaoPesquisar.pack(pady=10)

    botaoAddCarrinho = Button(root, text="Adicionar ao Carrinho", width=20, font=('Montserrat', 12), command=add_carrinho)
    botaoAddCarrinho.configure(bg="#FFDAB9", fg="black", relief="raised", padx=10, pady=5, activebackground="#008B8B")
    botaoAddCarrinho.pack(pady=10)

    botaoCarrinho = Button(root, text="Carrinho", width=10, font=('Montserrat', 12), command=to_carrinho)
    botaoCarrinho.configure(bg="#FFDAB9", fg="black", relief="raised", padx=10, pady=5, activebackground="#008B8B")
    botaoCarrinho.pack(pady=10)

    def eateregg_1():
        root.state(newstate='iconic')
        easteregg()

    btEaterEggs = Button(root, text="ツ", width=2, font=('Arial', 15), command=eateregg_1)
    btEaterEggs.configure(bg="#C71585", fg="white", relief="raised")
    btEaterEggs.place(x=1,y=750)

    # Mostrando os dados na tabela
    for i, (IdLivro, titulo, autor, ano, genero, preco) in enumerate(rows, start=1):
        tabela.insert("", tk.END, text=str(i), values=(IdLivro, titulo, autor, ano, genero, preco))
        
    # root.protocol("WM_DELETE_WINDOW", abrir)
    
    conn.close()
    root.mainloop()