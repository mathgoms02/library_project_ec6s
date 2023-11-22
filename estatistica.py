import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

password = "microondas123@"

def tela_estatistica(usuario):
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
    # cursorAVG = conn.cursor()

    # SOMA
    cursorSUM = conn.cursor()
    cursorSUM.execute("SELECT SUM(preco) AS total FROM livros_disponiveis ld JOIN livros_usuarios lu ON ld.idLivro = lu.fk_idLivro JOIN usuarios u ON lu.fk_idUsuario = u.idUsuario WHERE preco IS NOT NULL AND u.nomeUsuario = %s;", (username,))
    resultSUM = cursorSUM.fetchone()
    total_gastado = resultSUM[0] if resultSUM else 0

    # MÉDIA
    cursorAVG = conn.cursor()
    cursorAVG.execute("SELECT AVG(preco) AS media FROM livros_disponiveis ld JOIN livros_usuarios lu ON ld.idLivro = lu.fk_idLivro JOIN usuarios u ON lu.fk_idUsuario = u.idUsuario WHERE preco IS NOT NULL AND u.nomeUsuario = %s;", (username,))
    resultAVG = cursorAVG.fetchone()
    media_gasto = resultAVG[0] if resultAVG else 0

    # MODA
    cursorMOD = conn.cursor()
    cursorMOD.execute("SELECT(SELECT preco FROM livros_disponiveis ld JOIN livros_usuarios lu ON ld.idLivro = lu.fk_idLivro JOIN usuarios u ON lu.fk_idUsuario = u.idUsuario WHERE preco IS NOT NULL AND u.nomeUsuario = %s GROUP BY preco ORDER BY COUNT(*) DESC, preco LIMIT 1) AS moda;", (username,))
    resultMOD = cursorMOD.fetchone()
    moda_gasto = resultMOD[0] if resultMOD else 0

    # MEDIANA
    cursorMED = conn.cursor()
    cursorMED.execute("SELECT AVG(preco) AS mediana FROM (SELECT preco FROM (SELECT preco, ROW_NUMBER() OVER (ORDER BY preco) AS row_num, COUNT(*) OVER () AS total_rows FROM livros_disponiveis ld JOIN livros_usuarios lu ON ld.idLivro = lu.fk_idLivro JOIN usuarios u ON lu.fk_idUsuario = u.idUsuario WHERE preco IS NOT NULL AND u.nomeUsuario = %s) AS ranked WHERE row_num BETWEEN total_rows / 2 AND total_rows / 2 + 1) AS subquery;", (username,))
    resultMED = cursorMED.fetchone()
    mediana_gasto = resultMED[0] if resultMED else 0

    # DESVIO PADRAO
    cursorDESVPAD = conn.cursor()
    cursorDESVPAD.execute("SELECT STDDEV(preco) AS desvio_padrao FROM livros_disponiveis ld JOIN livros_usuarios lu ON ld.idLivro = lu.fk_idLivro JOIN usuarios u ON lu.fk_idUsuario = u.idUsuario WHERE preco IS NOT NULL AND u.nomeUsuario = %s;", (username,))
    resultDESVPAD = cursorDESVPAD.fetchone()
    desvpad_gasto = resultDESVPAD[0] if resultDESVPAD else 0



    # Criando a janela principal
    root = tk.Tk()
    root.title('Estatística do Usuário')
    root.state('zoomed')  # Abre maximizado
    root.configure(background='#FFFACD')

    marginSup = Canvas(root, width=1920, bg='#A52A2A', height=15, bd=0, highlightthickness=0, relief='ridge')
    marginSup.pack()

    header_label = Label(root, bg='#FFFACD', text='LITERAPICE', fg='#000000', font=('Montserrat', 15, 'bold'))
    header_label.pack()

    text_id = Label(root, bg='#FFFACD', text='Estatística - ' + username, fg='#000000', font=('Montserrat', 15, 'bold'))
    text_id.pack()




    #Exibindo valores estatístico
    total_gastado_label = Label(root, bg='#FFFACD', text="Total gastado: {:.2f}".format(total_gastado), fg='#000000', font=('Montserrat', 15, 'bold'))
    total_gastado_label.pack()

    media_gastado_label = Label(root, bg='#FFFACD', text="Média de Gastos: {:.2f}".format(media_gasto), fg='#000000', font=('Montserrat', 15, 'bold'))
    media_gastado_label.pack()

    moda_gastado_label = Label(root, bg='#FFFACD', text="Moda dos Gastos: {:.2f}".format(moda_gasto), fg='#000000', font=('Montserrat', 15, 'bold'))
    moda_gastado_label.pack()

    mediana_gastado_label = Label(root, bg='#FFFACD', text="Mediana dos Gastos: {:.2f}".format(mediana_gasto), fg='#000000', font=('Montserrat', 15, 'bold'))
    mediana_gastado_label.pack()

    desvpad_gastado_label = Label(root, bg='#FFFACD', text="Desvio Padrão dos Gastos: {:.2f}".format(desvpad_gasto), fg='#000000', font=('Montserrat', 15, 'bold'))
    desvpad_gastado_label.pack()

    conn.close()
    root.mainloop()
