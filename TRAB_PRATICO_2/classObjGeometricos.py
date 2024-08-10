import sys
import re
import xml.etree.ElementTree as ET
from random import randint
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication
from IPython.display import Image

import classObjGeometricos as obj
import funcTransformacao as ft
# import classMainWindow as w

# TODO: DESMEMBRAR EM ARQUIVOS
import funcoesSegundoTrabalho as fs

# Definindo as classes para representar os objetos geométricos
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Reta:
    def __init__(self, Ponto1, Ponto2):
        self.ponto1 = Ponto1
        self.ponto2 = Ponto2

class Poligono:

    def __init__(self,pontos):
        self.pontos = []
        tamanho = len(pontos)
        i = 0
        while(i<tamanho):
            self.pontos.append(pontos[i])
            i+=1