import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import cadastro
# from bd_project import id_usuario

def tela_carrinho(usuario):
    nomeUsuario = usuario
    password = "microondas123@"
    
    def create_server_connection2(host_name, user_name, user_password,database):
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
    
    def voltar_lista():
        car.destroy()  # Esconder a tela
        

    def tirar_carrinho():
        conn3 = create_server_connection2("localhost", "root", password, "biblioteca")
        cursor3 = conn3.cursor()
        try:
            item_selecionado1 = tabela_carrinho.selection()
            if item_selecionado1:
                valores_selecionados = tabela_carrinho.item(item_selecionado1)["values"]
                IdLivro = valores_selecionados[0]

                query = "DELETE FROM carrinho WHERE IdLivro = %s"
                cursor3.execute(query, (IdLivro,))
                conn3.commit()
                messagebox.showinfo("SUCESSO", "Item removido com sucesso do carrinho.")

                # Remover o item da tabela
                tabela_carrinho.delete(item_selecionado1)
                car.destroy()
                tela_carrinho()

        except Error as err:
            messagebox.showinfo("Error", str(err))
        finally:
            if conn3.is_connected():
                cursor3.close()
                conn3.close()

    def obter_id_usuario(username):
        # Abrir a conexão com o banco de dados
        conn4 = create_server_connection2("localhost", "root", password, "biblioteca")
        cursor4 = conn4.cursor()

        # Consulta SQL para obter o ID do usuário com base no nome
        query = "SELECT idUsuario FROM usuarios WHERE nomeUsuario = %s"
        cursor4.execute(query, (username,))
        resultado = cursor4.fetchone()

        # Verificar se o usuário foi encontrado
        if resultado:
            id_usuario = resultado[0]
        else:
            messagebox.showinfo("Erro", "Usuário não encontrado")
            id_usuario = None

        # Fechar o cursor e a conexão com o banco de dados
        cursor4.close()
        conn4.close()

        return id_usuario
    
    usuarioF = obter_id_usuario(nomeUsuario)

    def obter_id_livros(id_usuario):
        # Abrir a conexão com o banco de dados
        # password = "microondas123@"
        conn = create_server_connection2("localhost", "root", password, "biblioteca")
        cursor = conn.cursor()

        # Consulta SQL para obter os idLivros no carrinho para um usuário específico
        query = "SELECT idLivro_loja FROM carrinho WHERE idCarrinho_Usuario = %s"
        cursor.execute(query, (id_usuario,))
        resultados = cursor.fetchall()

        # Verificar se há livros encontrados no carrinho
        if resultados:
            id_livros = [resultado[0] for resultado in resultados]
        else:
            messagebox.showinfo("Erro", "Nenhum livro encontrado no carrinho")
            id_livros = []

        # Fechar o cursor e a conexão com o banco de dados
        cursor.close()
        conn.close()

        return id_livros
    
    def adquirir():

        conn4 = create_server_connection2("localhost", "root", password, "biblioteca")
        cursor4 = conn4.cursor()
        idlivros_loja = obter_id_livros(usuarioF)

        try:
            cursor4.execute("SELECT * FROM carrinho WHERE idCarrinho_Usuario=%s", (usuarioF,))
            carrinho_rows = cursor4.fetchall()
            
            #print(carrinho_rows)
            
            for item in carrinho_rows:
                idlivros_loja = item[2]
                # Inserir o item na tabela de compras
                cursor4.execute("INSERT INTO livros_usuarios (fk_idLivro, fk_idUsuario) VALUES (%s, %s)",
                            (idlivros_loja, usuarioF))

            # Limpar a tabela carrinho
            cursor4.execute("DELETE FROM carrinho WHERE idCarrinho_Usuario=%s", (usuarioF,))
            conn4.commit()

            messagebox.showinfo("SUCESSO", "Itens adquiridos com sucesso!")

            # Recarregar a tela do carrinho
            car.destroy()
            tela_carrinho(nomeUsuario)

        except Error as err:
            messagebox.showinfo("Error", str(err))
        finally:
            if conn4.is_connected():
                cursor4.close()
                conn4.close()

    def obter_id_usuario2(username):
        # Abrir a conexão com o banco de dados
        conn9 = create_server_connection2("localhost", "root", password, "biblioteca")
        cursor9 = conn9.cursor()

        # Consulta SQL para obter o ID do usuário com base no nome
        query9 = "SELECT idUsuario FROM usuarios WHERE nomeUsuario = %s"
        cursor9.execute(query9, (username,))
        resultado9 = cursor9.fetchone()

        # Verificar se o usuário foi encontrado
        if resultado9:
            id_usuario9 = resultado9[0]
        else:
            messagebox.showinfo("Erro", "Usuário não encontrado")
            id_usuario9 = None

        # Fechar o cursor e a conexão com o banco de dados
        cursor9.close()
        conn9.close()

        return id_usuario9
    
    usuarioS = obter_id_usuario2(nomeUsuario)
    print(usuarioS)



    conn = create_server_connection2("localhost", "root", password,"biblioteca")
    cursor = conn.cursor()

    query = "SELECT * FROM carrinho WHERE idCarrinho_Usuario=%s"
    cursor.execute(query, (usuarioS,))
    rows = cursor.fetchall()


    #Criando janela carrinho
    car = tk.Tk()
    car.title('Biblioteca')
    car.state('zoomed')  # Abre maximizado
    car.configure(background='#FFFACD')

    marginSup = Canvas(car, width=1920, bg='#A52A2A', height=15, bd=0, highlightthickness=0, relief='ridge')
    marginSup.pack()

    library_name = Label(car, bg='#FFFACD', text='LITERAPICE:', fg='#000000', font=('Montserrat', 15, 'bold'))
    library_name.pack()

    text_id = Label(car, bg='#FFFACD', text='Carrinho', fg='#000000', font=('Montserrat', 15, 'bold'))
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


    tabela_carrinho = ttk.Treeview(car)
    tabela_carrinho["columns"] = ("IdLivro", "titulo", "autor", "ano", "genero", "total")

    tabela_carrinho.column("#0", width=0, stretch=tk.NO) #coluna vazia (facilitar contagem)
    tabela_carrinho.column("IdLivro", width=80, anchor="center")
    tabela_carrinho.column("titulo", width=200, anchor="w")
    tabela_carrinho.column("autor", width=150, anchor="w")
    tabela_carrinho.column("ano", width=80, anchor="center")
    tabela_carrinho.column("genero", width=100, anchor="w")
    tabela_carrinho.column("total", width=100, anchor="center")

    tabela_carrinho.heading("#0", text="", anchor=tk.W) #coluna vazia
    tabela_carrinho.heading("IdLivro", text="IdLivro", anchor=tk.W)
    tabela_carrinho.heading("titulo", text="Titulo", anchor=tk.W)
    tabela_carrinho.heading("autor", text="Autor", anchor=tk.W)
    tabela_carrinho.heading("ano", text="Ano", anchor=tk.W)
    tabela_carrinho.heading("genero", text="Genero", anchor=tk.W)
    tabela_carrinho.heading("total", text="Total", anchor=tk.W)
    #tabela_carrinho.place(x=10,y=50)

    tabela_carrinho.pack(pady=20)

    botaoBack = Button(car, text="VOLTAR", command=voltar_lista)
    botaoBack.configure(bg="#FFDAB9", fg="black", relief="raised", padx=10, pady=5, activebackground="#008B8B")
    botaoBack.pack(pady=10)

    botaoDel = Button(car, text="X", command=tirar_carrinho)
    botaoDel.configure(bg="#FFDAB9", fg="black", relief="raised", padx=10, pady=5, activebackground="#008B8B")
    botaoDel.place(x=700, y=390)

    botaoAdd = Button(car, text="ADQUIRIR", command=adquirir)
    botaoAdd.configure(bg="#FFDAB9", fg="black", relief="raised", padx=10, pady=5, activebackground="#008B8B")
    botaoAdd.place(x=750, y=390)



    for i, (IdLivro, idCarrinhoUser, idlivros_loja, titulo, autor, ano, genero, preco) in enumerate(rows, start=1):
        total = preco
        tabela_carrinho.insert("", tk.END, text=str(i), values=(IdLivro, titulo, autor, ano, genero, preco, total))

    conn.close()
    car.mainloop()