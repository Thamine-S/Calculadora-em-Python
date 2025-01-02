from tkinter import *
from tkinter import ttk

#cores
cor1 = "#726a73" #cinza
cor2 = "#fad1ff" #rosa claro
cor3 = "#500459" #rosa escuro
cor4 = "#fde8ff" #branco


#estruturas
janela =  Tk()
janela.title("Calculadora")
janela.geometry("235x316")
janela.config(bg=cor2)

frame_tela = Frame(janela, width=235, height=50, bg=cor1)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=366, bg=cor2)
frame_corpo.grid(row=1, column=0)







todos_valores = ''

def entrar_valores(event):
    
    
    global todos_valores
    
    todos_valores = todos_valores + str(event)
    

    valor_texto.set(todos_valores)
    

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))
    
    
def limpar_tela():
    
    global todos_valores
    todos_valores = ""
    valor_texto.set("")



 

#label

valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=15, height=2, padx=7, relief=FLAT, anchor="e", justify= RIGHT, font=('Ivy 18 bold'), bg= cor3, fg= cor4)
app_label.place(x=0, y=0)


#botões

#primeira linha
b_clear = Button(frame_corpo,command=limpar_tela, text="C", width=16, height=3, font=('Ivy 9 bold'), relief=  GROOVE, overrelief=RIDGE)
b_clear.place(x=0, y=0)

b_porcentagem = Button(frame_corpo, command=lambda: entrar_valores("%"), text="%", width=7, height=3, font=('Ivy 9 bold'), relief=  GROOVE, overrelief=RIDGE)
b_porcentagem.place(x=118, y=0)

b_divisao = Button(frame_corpo, command=lambda: entrar_valores("/"), text="/", width=7, height=3, bg=cor2, fg=cor3,  font=('Ivy 9 bold'), relief=  GROOVE, overrelief=RIDGE)
b_divisao.place(x=177, y=0)


# segunda linha

b_7 = Button(frame_corpo, command=lambda: entrar_valores("7"), text="7", width=7, height=3,  font=('Ivy 9 bold'), relief=  GROOVE, overrelief=RIDGE)
b_7.place(x=0, y=52)

b_8 = Button(frame_corpo, command=lambda: entrar_valores("8"), text="8", width=7, height=3,  font=('Ivy 9 bold'), relief=  GROOVE, overrelief=RIDGE)
b_8.place(x=59, y=52)

b_9 = Button(frame_corpo, command=lambda: entrar_valores("9"), text="9", width=7, height=3,  font=('Ivy 9 bold'), relief=  GROOVE, overrelief=RIDGE)
b_9.place(x=118, y=52)

b_multi = Button(frame_corpo, command=lambda: entrar_valores("*"), text="*", width=7, height=3, bg=cor2, fg=cor3, font=('Ivy 9 bold'), relief=  GROOVE, overrelief=RIDGE)
b_multi.place(x=177, y=52)

#terceira linha

b_4 = Button(frame_corpo, command=lambda: entrar_valores("4"), text="4", width=7, height=3, font=('Ivy 9 bold'), relief=  GROOVE, overrelief=RIDGE)
b_4.place(x=0, y=104)

b_5 = Button(frame_corpo, command=lambda: entrar_valores("5"), text="5", width=7, height=3,  font=('Ivy 9 bold'), relief=  GROOVE, overrelief=RIDGE)
b_5.place(x=59, y=104)

b_6 = Button(frame_corpo, command=lambda: entrar_valores("6"), text="6", width=7, height=3,  font=('Ivy 9 bold'), relief=  GROOVE, overrelief=RIDGE)
b_6.place(x=118, y=104)

b_sub = Button(frame_corpo, command=lambda: entrar_valores("-"), text="-", width=7, height=3, bg=cor2, fg=cor3,  font=('Ivy 9 bold'), relief=  GROOVE, overrelief=RIDGE)
b_sub.place(x=177, y=104)

#quarta linha

b_1 = Button(frame_corpo, command=lambda: entrar_valores("1"), text="1", width=7, height=3,  font=('Ivy 9 bold'), relief=  GROOVE, overrelief=RIDGE)
b_1.place(x=0, y=156)

b_2 = Button(frame_corpo, command=lambda: entrar_valores("2"), text="2", width=7, height=3,  font=('Ivy 9 bold'), relief=  GROOVE, overrelief=RIDGE)
b_2.place(x=59, y=156)

b_3 = Button(frame_corpo, command=lambda: entrar_valores("3"), text="3", width=7, height=3,  font=('Ivy 9 bold'), relief=  GROOVE, overrelief=RIDGE)
b_3.place(x=118, y=156)

b_soma = Button(frame_corpo, command=lambda: entrar_valores("+"), text="+", width=7, height=3, bg=cor2, fg=cor3,  font=('Ivy 9 bold'), relief=  GROOVE, overrelief=RIDGE)
b_soma.place(x=177, y=156)

#quinta linha

b_zero = Button(frame_corpo, command=lambda: entrar_valores("0"), text="0", width=16, height=3,  font=('Ivy 9 bold'), relief=  GROOVE, overrelief=RIDGE)
b_zero.place(x=0, y=208)

b_ponto = Button(frame_corpo, command=lambda: entrar_valores("."), text=".", width=7, height=3,  font=('Ivy 9 bold'), relief=  GROOVE, overrelief=RIDGE)
b_ponto.place(x=118, y=208)

b_resultado = Button(frame_corpo,command= calcular, text="=", width=7, height=3, bg=cor2, fg=cor3,  font=('Ivy 9 bold'), relief=  GROOVE, overrelief=RIDGE)
b_resultado.place(x=177, y=208)



janela.mainloop()

