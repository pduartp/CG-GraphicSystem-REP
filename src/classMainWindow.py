from PyQt6 import QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QPushButton, QVBoxLayout, QWidget, QLabel, QGridLayout, 
                             QTextEdit, QLineEdit, QFormLayout, QDialog, QDialogButtonBox, QSpinBox)
from IPython.display import Image
from random import randint
import os

import funcTransformacao as ft
import classObjGeometricos as obj
import funcoesSegundoTrabalho as fs
import windowDialog

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, pontos, retas, poligonos, janela_1, janela_2,
                 pontos_window, retas_window, poligonos_window, window_1,
                 window_2, viewport_margem, viewport):
        super().__init__()
        
        self.pontos = pontos
        self.retas = retas
        self.poligonos = poligonos

        self.size_x = janela_2.x - janela_1.x
        self.size_y = janela_2.y - janela_1.y

        self.pontos_window = pontos_window
        self.retas_window = retas_window
        self.poligonos_window = poligonos_window

        self.window_x = window_2.x - window_1.x
        self.window_y = window_2.y - window_1.y

        self.janela_1 = janela_1
        self.janela_2 = janela_2

        self.window_1 = window_1
        self.window_2 = window_2

        self.viewport_margem = viewport_margem
        self.viewport = viewport

        self.pontos_window_iniciais = [ponto.copy() for ponto in self.pontos_window]
        self.retas_window_iniciais = [reta.copy() for reta in self.retas_window]
        self.poligonos_window_iniciais = [poligono.copy() for poligono in self.poligonos_window]

        # Configuração do layout da janela
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # Use a VBoxLayout para o layout principal
        self.main_layout = QVBoxLayout(self.central_widget)

        # Layout para os botões de controle
        self.control_layout = QGridLayout()
        
        # Configuração do rótulo e canvas
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(int(self.size_x), int(self.size_y))
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.main_layout.addWidget(self.label)

        # Adicionando botões de controle
        self.create_control_buttons()
        self.main_layout.addLayout(self.control_layout)
        
        self.draw_something()
            
    def create_control_buttons(self):
        buttons = {
            '↺': self.rotate_left,
            '↑': self.move_up,
            '↻': self.rotate_right,
            '←': self.move_left,
            '↓': self.move_down,
            '→': self.move_right,
            '(+) ZOOM IN': self.scale_zoomIn,
            'RESET': self.window_reset,
            '(-) ZOOM OUT': self.scale_zoomOut,
            'ADICIONAR PONTO': self.add_point,
            'ADICIONAR LINHA': self.add_line,
            'ADICIONAR POLÍGONO': self.add_polygon
        }

        for (text, handler), (row, col) in zip(buttons.items(), [(0, 0), (0, 1), (0, 2), 
                                                                 (1, 0), (1, 1), (1, 2), 
                                                                 (2, 0), (2, 1), (2, 2), 
                                                                 (3, 0), (3, 1), (3, 2)]):
            button = QPushButton(text)
            button.clicked.connect(handler)
            self.control_layout.addWidget(button, row, col)

        # Métodos de movimento conectados aos botões
    def move_up(self):
        fs.mover_para_cima(self)
        self.draw_something()

    def move_down(self):
        fs.mover_para_baixo(self)
        self.draw_something()

    def move_left(self):
        fs.mover_para_esquerda(self)
        self.draw_something()

    def move_right(self):
        fs.mover_para_direita(self)
        self.draw_something()

    def rotate_left(self):
        fs.rotacionar_para_esquerda(self)
        self.draw_something()

    def rotate_right(self):
        fs.rotacionar_para_direita(self)
        self.draw_something()

    def scale_zoomIn(self):
        fs.escala_ampliar(self)
        self.draw_something()

    def scale_zoomOut(self):
        fs.escala_diminuir(self)
        self.draw_something()

    def add_point(self):
        dialog = windowDialog.AddPointDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            x, y = dialog.get_coordinates()
            fs.adicionar_ponto(self, f"{x},{y}")
            self.draw_something()

    def add_line(self):
        dialog = windowDialog.AddLineDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            x1, y1, x2, y2 = dialog.get_coordinates()
            fs.adicionar_linha(self, f"{x1},{y1},{x2},{y2}")
            self.draw_something()

    def add_polygon(self):
        dialog = windowDialog.AddPolygonDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            coordinates = dialog.get_coordinates()
            coordenadas_str = ', '.join(f'{x},{y}' for x, y in coordinates)
            fs.adicionar_poligono(self, coordenadas_str)  # Passe a string de coordenadas para a função
            self.draw_something()
            
    def window_reset(self):
        fs.resetar_window(self)
        self.draw_something()
        
    def atualizar_viewport(self):
        ponto001 = obj.Ponto(self.window_1.x, self.window_1.y)
        ponto002 = obj.Ponto(self.window_2.x, self.window_2.y)

        ponto003 = obj.Ponto(self.viewport_margem.x, self.viewport_margem.y)
        ponto004 = obj.Ponto(self.viewport.x, self.viewport.y)

        window2 = [ponto001, ponto002]
        viewport2 = [ponto003, ponto004]
        poligonos_10 = []

        pontos_10 = [
            self.pontos_window[i].copy()
            for i, ponto in enumerate(self.pontos_window)
        ]
        retas_10 = [
            self.retas_window[i].copy() for i, reta in enumerate(self.retas_window)
        ]
        for i, poligono in enumerate(self.poligonos_window):
            poligonos_10.append(self.poligonos_window[i].copy())

            for i2, ponto in enumerate(self.poligonos_window[i].pontos):
                poligonos_10[i].pontos.append(self.poligonos_window[i].pontos[i2])
                poligonos_10[i].pontos[i2].x = self.poligonos_window[i].pontos[i2].x
                poligonos_10[i].pontos[i2].y = self.poligonos_window[i].pontos[i2].y

        # faz a transformação
        ft.transformar2(self.pontos_window, self.retas_window, self.poligonos_window, window2, viewport2)

        for i, ponto in enumerate(self.pontos):
            self.pontos[i] = self.pontos_window[i].copy()

        for i, reta in enumerate(self.retas):
            self.retas[i] = self.retas_window[i].copy()

        for i, poligono in enumerate(self.poligonos):

            self.poligonos[i] = self.poligonos_window[i].copy()

            for i2, ponto in enumerate(self.poligonos[i].pontos):
                self.poligonos[i].pontos[i2] = self.poligonos_window[i].pontos[i2].copy()

        for i, ponto in enumerate(self.pontos_window):
            self.pontos_window[i] = pontos_10[i].copy()

        for i, reta in enumerate(self.retas_window):
            self.retas_window[i] = retas_10[i].copy()

        for i, poligono in enumerate(self.poligonos_window):
            for i2, ponto in enumerate(self.poligonos_window[i].pontos):

                self.poligonos_window[i].pontos[i2].x = poligonos_10[i].pontos[i2].x
                self.poligonos_window[i].pontos[i2].y = poligonos_10[i].pontos[i2].y

    def criar_fractal(self):
        pontos = []

        i = 0
        x = 0
        y = 0
        while i<10:
            ponto = obj.Ponto(x,y)
            x+= randint(1,6)
            y+= randint(1,6)
            pontos.append(ponto.copy())    

            i+=1

        while i<13:
            ponto = obj.Ponto(x,y)
            x+= randint(1,6)
            y-= randint(1,7)
            pontos.append(ponto.copy())    

            i+=1
        while i<16:
            ponto = obj.Ponto(x,y)
            x+= randint(-7,6)
            y+= randint(-5,6)
            pontos.append(ponto.copy())    

            i+=1       

        string1 = ""
        for ponto in pontos:
            string2 = f"{str(ponto.x)},{str(ponto.y)},"
            string1 = string1 + string2
        string1 = f"{string1}1 , 1"

        print(string1)    

        self.space3.setPlainText(string1)

        for _ in range(150):
            self.add_polygon()
            self.scale_zoomOut()
            self.rotate_right()

    from PyQt6 import QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QPushButton, QVBoxLayout, QWidget, QLabel, QGridLayout, 
                             QTextEdit, QLineEdit, QFormLayout, QDialog, QDialogButtonBox, QSpinBox)
from IPython.display import Image
from random import randint
import os

import funcTransformacao as ft
import classObjGeometricos as obj
import funcoesSegundoTrabalho as fs
import windowDialog

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, pontos, retas, poligonos, janela_1, janela_2,
                 pontos_window, retas_window, poligonos_window, window_1,
                 window_2, viewport_margem, viewport):

        super().__init__()
        
        self.pontos = pontos
        self.retas = retas
        self.poligonos = poligonos

        self.size_x = janela_2.x - janela_1.x
        self.size_y = janela_2.y - janela_1.y

        self.pontos_window = pontos_window
        self.retas_window = retas_window
        self.poligonos_window = poligonos_window

        self.window_x = window_2.x - window_1.x
        self.window_y = window_2.y - window_1.y

        self.janela_1 = janela_1
        self.janela_2 = janela_2

        self.window_1 = window_1
        self.window_2 = window_2

        self.viewport_margem = viewport_margem
        self.viewport = viewport

        self.pontos_window_iniciais = [ponto.copy() for ponto in self.pontos_window]
        self.retas_window_iniciais = [reta.copy() for reta in self.retas_window]
        self.poligonos_window_iniciais = [poligono.copy() for poligono in self.poligonos_window]

        # Configuração do layout da janela
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # Use a VBoxLayout para o layout principal
        self.main_layout = QVBoxLayout(self.central_widget)

        # Layout para os botões de controle
        self.control_layout = QGridLayout()
        
        # Configuração do rótulo e canvas
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(int(self.size_x), int(self.size_y))
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.main_layout.addWidget(self.label)

        # Adicionando botões de controle
        self.create_control_buttons()
        self.main_layout.addLayout(self.control_layout)

        self.draw_something()

    def create_control_buttons(self):
        buttons = {
            '↺': self.rotate_left,
            '↑': self.move_up,
            '↻': self.rotate_right,
            '←': self.move_left,
            '↓': self.move_down,
            '→': self.move_right,
            '(+) ZOOM IN': self.scale_zoomIn,
            'RESET': self.window_reset,
            '(-) ZOOM OUT': self.scale_zoomOut,
            'ADICIONAR PONTO': self.add_point,
            'ADICIONAR LINHA': self.add_line,
            'ADICIONAR POLÍGONO': self.add_polygon
        }

        for (text, handler), (row, col) in zip(buttons.items(), [(0, 0), (0, 1), (0, 2), 
                                                                 (1, 0), (1, 1), (1, 2), 
                                                                 (2, 0), (2, 1), (2, 2), 
                                                                 (3, 0), (3, 1), (3, 2)]):
            button = QPushButton(text)
            button.clicked.connect(handler)
            self.control_layout.addWidget(button, row, col)

        # Métodos de movimento conectados aos botões
    def move_up(self):
        fs.mover_para_cima(self)
        self.draw_something()

    def move_down(self):
        fs.mover_para_baixo(self)
        self.draw_something()

    def move_left(self):
        fs.mover_para_esquerda(self)
        self.draw_something()

    def move_right(self):
        fs.mover_para_direita(self)
        self.draw_something()

    def rotate_left(self):
        fs.rotacionar_para_esquerda(self)
        self.draw_something()

    def rotate_right(self):
        fs.rotacionar_para_direita(self)
        self.draw_something()

    def scale_zoomIn(self):
        fs.escala_ampliar(self)
        self.draw_something()

    def scale_zoomOut(self):
        fs.escala_diminuir(self)
        self.draw_something()

    def add_point(self):
        dialog = windowDialog.AddPointDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            x, y = dialog.get_coordinates()
            fs.adicionar_ponto(self, f"{x},{y}")
            self.draw_something()

    def add_line(self):
        dialog = windowDialog.AddLineDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            x1, y1, x2, y2 = dialog.get_coordinates()
            fs.adicionar_linha(self, f"{x1},{y1},{x2},{y2}")
            self.draw_something()

    def add_polygon(self):
        dialog = windowDialog.AddPolygonDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            coordinates = dialog.get_coordinates()
            coordenadas_str = ', '.join(f'{x},{y}' for x, y in coordinates)
            fs.adicionar_poligono(self, coordenadas_str)  # Passe a string de coordenadas para a função
            self.draw_something()
            
    def window_reset(self):
        fs.resetar_window(self)
        self.draw_something()
        
    def atualizar_viewport(self):
        ponto001 = obj.Ponto(self.window_1.x, self.window_1.y)
        ponto002 = obj.Ponto(self.window_2.x, self.window_2.y)

        ponto003 = obj.Ponto(self.viewport_margem.x, self.viewport_margem.y)
        ponto004 = obj.Ponto(self.viewport.x, self.viewport.y)

        window2 = [ponto001, ponto002]
        viewport2 = [ponto003, ponto004]
        poligonos_10 = []

        pontos_10 = [
            self.pontos_window[i].copy()
            for i, ponto in enumerate(self.pontos_window)
        ]
        retas_10 = [
            self.retas_window[i].copy() for i, reta in enumerate(self.retas_window)
        ]
        for i, poligono in enumerate(self.poligonos_window):
            poligonos_10.append(self.poligonos_window[i].copy())

            for i2, ponto in enumerate(self.poligonos_window[i].pontos):
                poligonos_10[i].pontos.append(self.poligonos_window[i].pontos[i2])
                poligonos_10[i].pontos[i2].x = self.poligonos_window[i].pontos[i2].x
                poligonos_10[i].pontos[i2].y = self.poligonos_window[i].pontos[i2].y

        # faz a transformação
        ft.transformar2(self.pontos_window, self.retas_window, self.poligonos_window, window2, viewport2)

        for i, ponto in enumerate(self.pontos):
            self.pontos[i] = self.pontos_window[i].copy()

        for i, reta in enumerate(self.retas):
            self.retas[i] = self.retas_window[i].copy()

        for i, poligono in enumerate(self.poligonos):

            self.poligonos[i] = self.poligonos_window[i].copy()

            for i2, ponto in enumerate(self.poligonos[i].pontos):
                self.poligonos[i].pontos[i2] = self.poligonos_window[i].pontos[i2].copy()

        for i, ponto in enumerate(self.pontos_window):
            self.pontos_window[i] = pontos_10[i].copy()

        for i, reta in enumerate(self.retas_window):
            self.retas_window[i] = retas_10[i].copy()

        for i, poligono in enumerate(self.poligonos_window):
            for i2, ponto in enumerate(self.poligonos_window[i].pontos):

                self.poligonos_window[i].pontos[i2].x = poligonos_10[i].pontos[i2].x
                self.poligonos_window[i].pontos[i2].y = poligonos_10[i].pontos[i2].y

    def criar_fractal(self):
        pontos = []

        i = 0
        x = 0
        y = 0
        while i<10:
            ponto = obj.Ponto(x,y)
            x+= randint(1,6)
            y+= randint(1,6)
            pontos.append(ponto.copy())    

            i+=1

        while i<13:
            ponto = obj.Ponto(x,y)
            x+= randint(1,6)
            y-= randint(1,7)
            pontos.append(ponto.copy())    

            i+=1
        while i<16:
            ponto = obj.Ponto(x,y)
            x+= randint(-7,6)
            y+= randint(-5,6)
            pontos.append(ponto.copy())    

            i+=1       

        string1 = ""
        for ponto in pontos:
            string2 = f"{str(ponto.x)},{str(ponto.y)},"
            string1 = string1 + string2
        string1 = f"{string1}1 , 1"

        print(string1)    

        self.space3.setPlainText(string1)

        for _ in range(150):
            self.add_polygon()
            self.scale_zoomOut()
            self.rotate_right()

    def draw_something(self):
        canvas = self.label.pixmap()
        canvas.fill(Qt.GlobalColor.white)
        painter = QtGui.QPainter(canvas)

        # Desenhando a grade de fundo
        pen = QtGui.QPen()
        pen.setColor(QtGui.QColor(240, 240, 240, 240))
        painter.setPen(pen)

        for i in range(100):
            painter.drawLine(0, i * 10, 1000, i * 10)
        for i in range(100):
            painter.drawLine(i * 10, 0, i * 10, 1000)

        pen.setColor(QtGui.QColor('blue'))
        painter.setPen(pen)

        # Desenhando os pontos na tela
        for ponto in self.pontos:
            painter.drawPoint(int(ponto.x), int(ponto.y))

        # Desenhando as retas na tela
        for reta in self.retas:
            painter.drawLine(int(reta.ponto1.x), int(reta.ponto1.y), int(reta.ponto2.x), int(reta.ponto2.y))

        # Desenhando os polígonos na tela
        for poligono in self.poligonos:
            i = 0
            while (i < (len(poligono.pontos) - 1)):
                painter.drawLine(int(poligono.pontos[i].x), int(poligono.pontos[i].y), int(poligono.pontos[i + 1].x), int(poligono.pontos[i + 1].y))
                i += 1
            painter.drawLine(int(poligono.pontos[i].x), int(poligono.pontos[i].y), int(poligono.pontos[0].x), int(poligono.pontos[0].y))

        painter.end()

        self.label.setPixmap(canvas)
        self.create_tempWidget()

    def create_tempWidget(self):
        temp_widget = QWidget()
        temp_layout = QVBoxLayout(temp_widget)
        temp_label = QLabel()
        temp_label.setPixmap(self.label.pixmap())
        temp_layout.addWidget(temp_label)
        temp_widget.setFixedSize(temp_label.width(), temp_label.height())

        filename = "imagem_resultado.png"
        filepath = os.path.join("output", filename)
        screenshot = temp_widget.grab()
        screenshot.save(filepath)