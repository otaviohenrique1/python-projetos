# -*- coding: UTF-8 -*-
from tkinter import *

class CriaComponentesTela(object):
    @staticmethod
    def criaFrame(local, padx, pady, valorSide):
        frame = Frame(local);
        frame["padx"] = padx;
        frame["pady"] = pady;
        frame.pack(side=valorSide);
        return frame;

    @staticmethod
    def criaBotao(local, texto, fonte, comando, valorSide):
        botao = Button(local);
        botao["text"] = texto;
        botao["font"] = fonte;
        botao["command"] = comando;
        botao.pack(side=valorSide);
        return botao;

    @staticmethod
    def criaLabel(local, padx, pady, bordaLargura, bordaTipo, fonte, texto, valorSide):
        label = Label(local);
        label["padx"] = padx;
        label["pady"] = pady;
        label["font"] = fonte;
        label["bd"] = bordaLargura;
        label["relief"] = bordaTipo;
        label["text"] = texto;
        label.pack(side=valorSide);
        return label;

    @staticmethod
    def criaCampoDeTexto(local, fonte, largura, valorSide):
        campoDeTexto = Entry(local);
        campoDeTexto["font"] = fonte;
        campoDeTexto["width"] = largura;
        campoDeTexto.pack(side=valorSide);
        return campoDeTexto;
