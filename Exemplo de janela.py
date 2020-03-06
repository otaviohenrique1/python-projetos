from tkinter import*# importa todos os modulos do pacote
#Interface da calculadora
janela = Tk()#Cria a janela
janela.title("Janela")#Titulo da janela
janela.geometry("680x400")#Dimensões da janela
janela.resizable(width=FALSE, height=FALSE)#Janela não pode ser maximindada, janela de tamanho pequeno
#-------------------------------------------------------------------------------------------------------------------
#Parte do label titulo-------------------------------------------------------------------------------------------------
#Frame do label titulo
labelframe = Frame(janela)#Nome do frame e local onde ele esta na janela
labelframe.config(bd=2, relief=SUNKEN, bg='blue')#Configurações do frame, borda(bd = tamanho), estilo da borda e cor de fundo(bg = 'cor')
labelframe.pack(side=TOP, pady=5, padx=5)#local onde o frame esta na janela
#Label
titulofont = ('times', 20, 'bold', 'italic')#Variavel para colocar a fonte do label(fonte do texto,tamanho da fonte,texto em negrito e italico)
titulo = Label(labelframe, text='Janela',height=1, width=20,font=titulofont).pack(side=TOP)
#Lugar onde o label esta e text é o titulo do label, dimensões e fonte do label, lugar onde label esta no layout do frame(layout é o pack(side=DIREÇÃO(escrito em letras maiusculas)))
BarraScroll = Scrollbar(labelframe).pack(side=RIGHT, fill = Y)
janela.mainloop()