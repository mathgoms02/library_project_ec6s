import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import *
from tkinter import Tk
from tkinter import messagebox
from bd_project import tela_livros

def tela_login():

    # cores -----------------------------
    co0 = "#f0f3f5"  # Preta / black
    co1 = "#feffff"  # branca / white
    co2 = "#3fb5a3"  # verde / green
    co3 = "#38576b"  # valor / value
    co4 = "#403d3d"   # letra / letters

    # cirando janela ----------------------------------------------------------------
    tela_login = Tk()
    tela_login.title('Login')
    tela_login.geometry('310x300')
    tela_login.configure(background=co1)
    tela_login.resizable(width=FALSE, height=FALSE)

    #Dividindo a Janela cadastro -------------------------------------------------------------
    frame_cima = Frame(tela_login, width=310, height=50, bg=co1, relief='flat')
    frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

    frame_baixo = Frame(tela_login, width=310, height=250, bg=co1, relief='flat')
    frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    #Configurando o frame cima da tela login ------------------------------------------------------
    l_nome = Label(frame_cima, text='LOGIN', anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
    l_nome.place(x=5, y=5)

    l_linha = Label(frame_cima, text='', width=275, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
    l_linha.place(x=10, y=45)


    def abrir_tela_cadastro():
        tela_login.withdraw()  # Esconder a tela de login
        tela_cadastro = tk.Toplevel()  # Criar uma nova janela para o cadastro
        tela_cadastro.title('')
        tela_cadastro.geometry('310x300')
        tela_cadastro.configure(background=co1)
        tela_cadastro.resizable(width=FALSE, height=FALSE)
        tela_cadastro.title('Cadastro')
        
        def cadastrar():
            # Obter os dados do formulário
            novo_username = e_nome.get()
            nova_password = e_senha.get()
            
            # Limpar os campos de entrada
            e_nome.delete(0, tk.END)
            e_senha.delete(0, tk.END)
            
            # Conectar ao banco de dados
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='microondas123@',
                database='biblioteca'
            )
            cursor = conn.cursor()
            
            # Verificar se o nome de usuário já existe
            query = "SELECT * FROM usuarios WHERE nomeUsuario=%s"
            cursor.execute(query, (novo_username,))
            resultado = cursor.fetchone()
            
            # Validação de dados
            if resultado:
                messagebox.showinfo('Cadastro', 'Usuário já existernte')
            else:
                # Inserir o usuário no banco de dados
                query = "INSERT INTO usuarios (nomeUsuario, senhaUsuario) VALUES (%s, %s)"
                valores = (novo_username, nova_password)
                cursor.execute(query, valores)

                # Efetivar a transação
                conn.commit()
                
                # Fechar a conexão com o banco de dados
                cursor.close()
                conn.close()
                
                # Exibir mensagem se sucesso
                messagebox.showinfo('Cadastro', 'Usuário ' + novo_username + ' cadastrado com sucesso!!!')
        
        # Função para fechar a tela de cadastro e mostrar a tela de login novamente
        def fechar_tela_cadastro():
            tela_cadastro.destroy()
            tela_login.deiconify()  # Mostrar a tela de login novamente
        
        #Dividindo a Janela cadastro -------------------------------------------------------------
        frame_cima2 = Frame(tela_cadastro, width=310, height=50, bg=co1, relief='flat')
        frame_cima2.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

        frame_baixo2 = Frame(tela_cadastro, width=310, height=250, bg=co1, relief='flat')
        frame_baixo2.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)
        
        #Configurando o frame cima da tela cadastro ------------------------------------------------------
        l_nome = Label(frame_cima2, text='CADASTRO', anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
        l_nome.place(x=5, y=5)
        l_linha = Label(frame_cima2, text='', width=275, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
        l_linha.place(x=10, y=45)
        
        #Configurando o frame baixo da tela cadastro ------------------------------------------------------
        l_nome = Label(frame_baixo2, text='Novo Usuário *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
        l_nome.place(x=10, y=20)
        e_nome = Entry(frame_baixo2, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
        e_nome.place(x=14, y=50)
        
        l_senha = Label(frame_baixo2, text='Nova Senha', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
        l_senha.place(x=10, y=95)
        e_senha = Entry(frame_baixo2, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid', show='*')
        e_senha.place(x=14, y=125)
        
        b_cadastrar = Button(frame_baixo2, text='Fechar', width=15, height=2, font=('Ivy 10 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE,command=fechar_tela_cadastro)
        b_cadastrar.place(x=15, y=180)

        b_confirmar = Button(frame_baixo2, text='Cadastrar', width=15, height=2, font=('Ivy 10 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE,command=cadastrar)
        b_confirmar.place(x=165, y=180)
        
    def verifica_senha():
        # Realizar a consulta para verificar se o usuário existe
        username = e_nome.get()
        password = e_senha.get()
        
        # Limpar os campos de entrada
        e_nome.delete(0, tk.END)
        e_senha.delete(0, tk.END)
        
        # Conectar ao banco de dados
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='microondas123@',
            database='biblioteca'
        )
        cursor = conn.cursor()
        
        query = "SELECT * FROM usuarios WHERE nomeUsuario=%s AND senhaUsuario=%s"
        cursor.execute(query, (username, password))
        resultado = cursor.fetchone()
        
        if resultado:
            messagebox.showinfo('Login', 'Seja bem-vindo ' + username + '!!!')
            tela_login.destroy()  # Fechar a janela de login
            tela_livros(username)
        else:
            messagebox.showinfo('Error', 'Login ou senha incorreto. Caso não tenha login realize o cadastro.')
        
        # Efetivar a transação    
        conn.commit()

        # Fechar a conexão com o banco de dados
        cursor.close()
        conn.close()

    
    #Configurando o frame baixo da tela login ------------------------------------------------------
    l_nome = Label(frame_baixo, text='Nome *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nome.place(x=10, y=20)
    e_nome = Entry(frame_baixo, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
    e_nome.place(x=14, y=50)

    l_senha = Label(frame_baixo, text='Senha *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_senha.place(x=10, y=95)
    e_senha = Entry(frame_baixo, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid', show='*')
    e_senha.place(x=14, y=125)

    b_cadastrar = Button(frame_baixo, text='Cadastre-se', width=15, height=2, font=('Ivy 10 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE,command=abrir_tela_cadastro)
    b_cadastrar.place(x=15, y=180)

    b_confirmar = Button(frame_baixo, text='Entrar', width=15, height=2, font=('Ivy 10 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE,command=verifica_senha)
    b_confirmar.place(x=165, y=180)

    tela_login.mainloop()