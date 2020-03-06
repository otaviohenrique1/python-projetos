from tkinter import*# importa todos os modulos do pacote

#Interface da calculadora
janela = Tk()#Cria a janela
janela.title("Calculadora de sub redes")#Titulo da janela
janela .geometry("500x600")#Dimensões da janela
#Botoes
botao1 = Button(janela, text='Botão 1',command=janela.quit)
botao1.pack(side=RIGHT)
botao2 = Button(janela, text='Botão 2',command=janela.quit)
botao2.pack(side=LEFT)
botao3 = Button(janela, text='Botão 3',command=janela.quit)
botao3.pack(side=TOP)
botao4 = Button(janela, text='Botão 4',command=janela.quit)
botao4.pack(side=BOTTOM)

janela.mainloop()#Inicia a janela