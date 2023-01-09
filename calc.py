from tkinter import *

#cores
preto = '#000000'
azul = '#227A9C'
branco = '#FEFBF5'

janela = Tk()
janela.geometry('310x295')
janela.iconphoto(False, PhotoImage(file='logo.png'))
janela.title(' Calculadora')

#display e corpo
frame_tela = Frame(janela, width=310, height=80, bg = preto)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=310, height=320)
frame_corpo.grid(row=1, column=0)

todos_valores = ''

def coleta_valores(event):

    global todos_valores
    todos_valores = todos_valores + str(event)
    
    
    valor_texto.set(todos_valores)

def faz_calculos():
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))

def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')



#label
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=20, height=3, padx=7, relief='flat', anchor='e', justify='right', font='Arial 19 bold', bg=azul, fg=branco)
app_label.place(x=0, y=0)

#teclas
b1 = Button(frame_corpo, command= limpar_tela, text='C', width=18, height=2, fg=preto, bg=branco, font='Arial 10 bold', relief='groove')
b1.place(x=0,y=0)
b2 = Button(frame_corpo, command= lambda: coleta_valores('7'), text='7', width=9, height=2, fg=preto, bg=branco, font='Arial 10 bold', relief='groove')
b2.place(x=0,y=43)
b3 = Button(frame_corpo, command= lambda: coleta_valores('4'), text='4', width=9, height=2, fg=preto, bg=branco, font='Arial 10 bold', relief='groove')
b3.place(x=0,y=86)
b4 = Button(frame_corpo, command= lambda: coleta_valores('1'), text='1', width=9, height=2, fg=preto, bg=branco, font='Arial 10 bold', relief='groove')
b4.place(x=0,y=129)
b5 = Button(frame_corpo, command= lambda: coleta_valores('0'), text='0', width=18, height=2, fg=preto, bg=branco, font='Arial 10 bold', relief='groove')
b5.place(x=0,y=172)

b6 = Button(frame_corpo, command= lambda: coleta_valores('8'), text='8', width=8, height=2, fg=preto, bg=branco, font='Arial 10 bold', relief='groove')
b6.place(x=80,y=43)
b7 = Button(frame_corpo, command= lambda: coleta_valores('5'), text='5', width=8, height=2, fg=preto, bg=branco, font='Arial 10 bold', relief='groove')
b7.place(x=80,y=86)
b8 = Button(frame_corpo, command= lambda: coleta_valores('2'), text='2', width=8, height=2, fg=preto, bg=branco, font='Arial 10 bold', relief='groove')
b8.place(x=80,y=129)

b9 = Button(frame_corpo, command= lambda: coleta_valores('%'), text='%', width=10, height=2, fg=preto, bg=branco, font='Arial 10 bold', relief='groove')
b9.place(x=153,y=0)
b10 = Button(frame_corpo, command= lambda: coleta_valores('9'), text='9', width=10, height=2, fg=preto, bg=branco, font='Arial 10 bold', relief='groove')
b10.place(x=153,y=43)
b11 = Button(frame_corpo, command= lambda: coleta_valores('6'), text='6', width=10, height=2, fg=preto, bg=branco, font='Arial 10 bold', relief='groove')
b11.place(x=153,y=86)
b12 = Button(frame_corpo, command= lambda: coleta_valores('3'), text='3', width=10, height=2, fg=preto, bg=branco, font='Arial 10 bold', relief='groove')
b12.place(x=153,y=129)
b13 = Button(frame_corpo, command= lambda: coleta_valores('.'), text='.', width=10, height=2, fg=preto, bg=branco, font='Arial 10 bold', relief='groove')
b13.place(x=153,y=172)

b14 = Button(frame_corpo, command= lambda: coleta_valores('/'), text='/', width=8, height=2, fg=preto, bg=branco, font='Arial 10 bold', relief='groove')
b14.place(x=240,y=0)
b15 = Button(frame_corpo, command= lambda: coleta_valores('*'), text='*', width=8, height=2, fg=preto, bg=branco, font='Arial 10 bold', relief='groove')
b15.place(x=240,y=43)
b16 = Button(frame_corpo, command= lambda: coleta_valores('-'), text='-', width=8, height=2, fg=preto, bg=branco, font='Arial 10 bold', relief='groove')
b16.place(x=240,y=86)
b17 = Button(frame_corpo, command= lambda: coleta_valores('+'), text='+', width=8, height=2, fg=preto, bg=branco, font='Arial 10 bold', relief='groove')
b17.place(x=240,y=129)
b18 = Button(frame_corpo, command= faz_calculos, text='=', width=8, height=2, fg=preto, bg=branco, font='Arial 10 bold', relief='groove')
b18.place(x=240,y=172)



janela.mainloop()