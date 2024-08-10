import sys
import re
import xml.etree.ElementTree as ET
from random import randint
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication
from IPython.display import Image

# import classObjGeometricos as obj
import funcTransformacao as ft
import classMainWindow as w

# TODO: DESMEMBRAR EM ARQUIVOS
import funcoesSegundoTrabalho as fs

# Classe para a janela principal da aplicação
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, pontos, retas, poligono, window_x, window_y):
        super().__init__()

        self.pontos = pontos
        self.retas = retas
        self.poligono = poligono

        self.size_x = window_x
        self.size_y = window_y

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(window_x, window_y)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

    # Método para desenhar os objetos na tela
    def draw_something(self):
       
        canvas = self.label.pixmap()
        canvas.fill(Qt.GlobalColor.white)
        painter = QtGui.QPainter(canvas)

        pen = QtGui.QPen()
        pen.setColor(QtGui.QColor(50, 50, 50, 60))

        painter.setPen(pen)

        # Desenhando grade de fundo
        for i in range(100):
            painter.drawLine(0, i * 10, 1000, i * 10)

        for i in range(100):
            painter.drawLine(i * 10, 0, i * 10, 1000)

        pen.setColor(QtGui.QColor('black'))
        painter.setPen(pen)

        # Desenhando os pontos na tela
        for ponto in self.pontos:
            painter.drawPoint(int(ponto.x), int(ponto.y))

        # Desenhando as retas na tela
        for reta in self.retas:
            painter.drawLine(int(reta.ponto1.x), int(reta.ponto1.y), int(reta.ponto2.x), int(reta.ponto2.y))

        # Desenhando o polígono na tela
        i = 0
        while(i < (len(self.poligono) - 1)):
            painter.drawLine(int(self.poligono[i].x), int(self.poligono[i].y), int(self.poligono[i + 1].x), int(self.poligono[i + 1].y))
            i += 1

        painter.drawLine(int(self.poligono[i].x), int(self.poligono[i].y), int(self.poligono[0].x), int(self.poligono[0].y))

        painter.end()
        self.label.setPixmap(canvas)