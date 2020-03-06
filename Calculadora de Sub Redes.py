from tkinter import*# importa todos os modulos do pacote
#Interface da calculadora
janela = Tk()#Cria a janela
janela.title("Calculadora de sub redes")#Titulo da janela
janela.geometry("440x350")#Dimensões da janela
janela.config(bg='light gray', pady=5)
janela.resizable(width=FALSE, height=FALSE)#Janela não pode ser maximindada, janela de tamanho pequeno
#-------------------------------------------------------------------------------------------------------------------
#Parte do label titulo-------------------------------------------------------------------------------------------------
#Frame do label titulo
labelframe = Frame(janela, bd=2, relief=SUNKEN, bg='light gray').pack(side=TOP, padx=5, fill=X)#Nome do frame, configurações do frame e local onde ele esta na janela
#Configurações do frame, borda(bd = tamanho), estilo da borda e cor de fundo(bg = 'cor')
#Label
titulofont = ('times', 20, 'bold', 'italic')#Variavel para colocar a fonte do label(fonte do texto,tamanho da fonte,texto em negrito e italico)
titulo = Label(labelframe, text='Calculadora de sub-redes',height=1, width=20,font=titulofont, relief=SUNKEN, bg='light gray').pack(side=TOP, padx=5, fill=X)
#Lugar onde o label esta e text é o titulo do label, dimensões e fonte do label, lugar onde label esta no layout do frame(layout é o pack(side=DIREÇÃO(escrito em letras maiusculas)))
#-------------------------------------------------------------------------------------------------------------------
#Parte dos labels e textfields-------------------------------------------------------------------------------------------------
textframe = Frame(janela, bd=2, relief=SUNKEN, bg='light gray')
textframe.pack(side=TOP, pady=5, padx=5, fill=X)
#Labels
LabeldoIP = Label(textframe, text='IP(Decimal ou Binario):', bg='light gray').grid(row=0, column=0, sticky = W+E)
LabeldaMascara = Label(textframe, text='Mascara:', bg='light gray').grid(row=1, column=0, sticky = W)
LabeldaSubRede = Label(textframe, text='Numero de Sub Redes:', bg='light gray').grid(row=2, column=0, sticky = W+E)
LabeldoHost = Label(textframe, text='Numero de Hosts:', bg='light gray').grid(row=3, column=0, sticky = W)
#Textfields
TextIP1 = Entry(textframe, width=10, bd=2, relief=SUNKEN).grid(row=0, column=1, padx=4)
TextIP2 = Entry(textframe, width=10, bd=2, relief=SUNKEN).grid(row=0, column=2, padx=4)
TextIP3 = Entry(textframe, width=10, bd=2, relief=SUNKEN).grid(row=0, column=3, padx=4)
TextIP4 = Entry(textframe, width=10, bd=2, relief=SUNKEN).grid(row=0, column=4, padx=4)
TextMascara1 = Entry(textframe, width=10, bd=2, relief=SUNKEN).grid(row=1, column=1, padx=4)
TextMascara2 = Entry(textframe, width=10, bd=2, relief=SUNKEN).grid(row=1, column=2, padx=4)
TextMascara3 = Entry(textframe, width=10, bd=2, relief=SUNKEN).grid(row=1, column=3, padx=4)
TextMascara4 = Entry(textframe, width=10, bd=2, relief=SUNKEN).grid(row=1, column=4, padx=4)
TextSubRede = Entry(textframe, width=20, bd=2, relief=SUNKEN).grid(row=2, column=1, columnspan=2,padx=4,sticky = W+E)
TextHost = Entry(textframe, width=20, bd=2, relief=SUNKEN).grid(row=3, column=1, columnspan=2, padx=4,sticky = W+E)
#-------------------------------------------------------------------------------------------------------------------
#Parte do texto
FrameTexto = Frame(janela, bd=2, relief=SUNKEN, bg='light gray')
FrameTexto.pack(side=TOP, pady=5, padx=5, fill = X)
def comentario():    {        x1.set(100),x2.set(100),x3.set(100),x4.set(100)    }#Função que vai no botao Decimal pra Binario
def comentario2():{        x1.set(100),x2.set(100),x3.set(100),x4.set(100)    }#Função que vai no botao Binario para Decimal
def Limpar():{x5.set(000)}#Função que limpa os labels
x1= StringVar()
x2= StringVar()
x3= StringVar()
x4= StringVar()
x5= StringVar()
DecBin = Label(FrameTexto, text="IP convertido de decimal para binario: ", bg='light gray').grid(row=0, column=0)
DecBinIP1 = Label(FrameTexto, text="000", bd=2, relief=SUNKEN, bg='light gray', width=5,textvariable=x2).grid(row=0, column=1, padx=5)
DecBinIP2 = Label(FrameTexto, text="000", bd=2, relief=SUNKEN, bg='light gray', width=5,textvariable=x2).grid(row=0, column=2, padx=5)
DecBinIP3 = Label(FrameTexto, text="000", bd=2, relief=SUNKEN, bg='light gray', width=5,textvariable=x3).grid(row=0, column=3, padx=5)
DecBinIP4 = Label(FrameTexto, text="000", bd=2, relief=SUNKEN, bg='light gray', width=5,textvariable=x4).grid(row=0, column=4, padx=5)
BinDec = Label(FrameTexto, text="IP convertido de binario para decimal: ", bg='light gray').grid(row=1, column=0)
BinDecIP1 = Label(FrameTexto, text="000", bd=2, relief=SUNKEN, bg='light gray', width=5,textvariable=x2).grid(row=1, column=1, padx=5)
BinDecIP2 = Label(FrameTexto, text="000", bd=2, relief=SUNKEN, bg='light gray', width=5,textvariable=x2).grid(row=1, column=2, padx=5)
BinDecIP3 = Label(FrameTexto, text="000", bd=2, relief=SUNKEN, bg='light gray', width=5,textvariable=x2).grid(row=1, column=3, padx=5)
BinDecIP4 = Label(FrameTexto, text="000", bd=2, relief=SUNKEN, bg='light gray', width=5,textvariable=x2).grid(row=1, column=4, padx=5)
Quantidadesubrede = Label(FrameTexto, text="Quantidade de sub redes:", bg='light gray').grid(row=2, column=0, sticky = W)
Nsubrede = Label(FrameTexto, text="100", bd=2, relief=SUNKEN, bg='light gray', width=5,textvariable=x2).grid(row=2, column=1, columnspan=4, padx=5,sticky = W+E)
TipoIP = Label(FrameTexto, text="Tipo de IP: ", bg='light gray').grid(row=3, column=0, sticky = W)
NTipoIP = Label(FrameTexto, text="100", bd=2, relief=SUNKEN, bg='light gray', width=5,textvariable=x2).grid(row=3, column=1, columnspan=4, padx=5,sticky = W+E)
ClasseIP = Label(FrameTexto, text="Classe de IP:", bg='light gray').grid(row=4, column=0, sticky = W)
NClasseIP = Label(FrameTexto, text="100", bd=2, relief=SUNKEN, bg='light gray', width=5,textvariable=x2).grid(row=4, column=1, columnspan=4, padx=5,sticky = W+E)
#-------------------------------------------------------------------------------------------------------------------
#Parte dos botoes-------------------------------------------------------------------------------------------------
framebotoes = Frame(janela,bd=2, relief=SUNKEN, bg='light gray')#Frame dos botoes
framebotoes.pack(side=BOTTOM, padx=5, fill=X)
DecimalparaBinario = Button(framebotoes, text='Decimal para Binario', bg='light gray',command=comentario).grid(row=0, column=0, pady=5, padx=5)
BinarioparaDecimal = Button(framebotoes, text='Binario para Decimal', bg='light gray',command=comentario2).grid(row=0, column=1, pady=5, padx=5)
Limpar = Button(framebotoes, text='Limpar', width=9, bg='light gray',command=Limpar).grid(row=0, column=2, pady=5, padx=5)
Sair = Button(framebotoes, text='Sair', width=9, bg='light gray',command=janela.quit).grid(row=0, column=3, pady=5, padx=5)
#-------------------------------------------------------------------------------------------------------------------
#Inicia a janela
janela.mainloop()
#-------------------------------------------------------------------------------------------------------------------
#Classes e modulos da culadora
class calculadora:
    {

    }