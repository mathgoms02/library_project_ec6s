import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox

def easteregg():
    
    root1 = tk.Tk()
    root1.title('10 de média?')
    root1.geometry('600x600')
    root1.configure(background='#66cdaa')

    def move_button_1(e):
        if abs(e.x - button_1.winfo_x()) < 100 and abs(e.y - button_1.winfo_y()) < 150:
            x = random.randint(0, root1.winfo_width() - button_1.winfo_width())
            y = random.randint(0, root1.winfo_height() - button_1.winfo_height())
            button_1.place(x=x, y=y)

    def accepted():
        messagebox. showinfo(
            'DAAALEEE', 'Thanks, tamojunto')
        
    def denied():
        move_button_1.destroy()


    margin = Canvas(root1, width=500, bg='#FFFFFF', height=5,
                    bd=0, highlightthickness=0, relief='ridge')
    margin.pack()
    text_id = Label(root1, bg='#66cdaa', text='Professor vai nos dar 10 de média??',
                    fg='#590d22', font=('Montserrat', 24, 'bold'))
    text_id.pack()
    button_1 = tk.Button(root1, text='Não', bg='#ffb3c1', command=denied,
                            relief=RIDGE, bd=3, font=('Montserrat', 14, 'bold'))
    button_1.pack()


    root1.bind('<Motion>', move_button_1)
    button_2 = tk.Button(root1, text='ÓBVIO', bg='#ffb3c1', relief=RIDGE,
                            bd=3, command=accepted, font=('Montserrat', 14, 'bold'))
    button_2.pack()

    root1.mainloop()