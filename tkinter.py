#Interface gráfica com Tkinter

from tkinter import *
from tkinter import messagebox


janela = Tk()
janela.title ("Minha primeira janela")
janela.geometry("500x500+400+70")
janela.minsize(200,200)
#janela.maxsize(600,600)
#janela.resizable(False, False)
#janela.state("zoomed")
#janela.state("iconic")
janela['bg'] = "light blue"

def mensagem1():
    texto = txtnome.get()
    print(texto)
def mensagem2():
    #messagebox.showinfo("DINHEIRO ROUBADO")
    messagebox.showwarning ("PERDEU TUDO", "VOCE ESTA NO SERASA")

nome = Label (janela, text = "Parabéns você acabou de ganhar \n 1000 reais  \n Digite seu cpf para fazer o resgate", font = "Arial 20")
nome.pack()

txtnome = Entry(janela, font = "Arial 20", bg = "light yellow")
txtnome.pack(pady = 30)

botao1= Button (janela, text ="Clique aqui para resgatar seu dinheiro!", font = "Arial 20", command = mensagem1)
botao1.pack()
botao2 =  Button (janela, text ="Não clique aqui", font = "Arial 14", command = mensagem2)
botao2.pack()
janela.mainloop()
