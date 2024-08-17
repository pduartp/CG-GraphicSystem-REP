from PyQt6 import QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QLabel
from IPython.display import Image
import os
import funcTransformacao as ft
import classObjGeometricos as obj

# TODO: DESMEMBRAR EM ARQUIVOS
import segundoTrabalho.funcoesSegundoTrabalho as fs

# Classe para a janela principal da aplicação
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, pontos, retas, poligonos, janela_1, janela_2, pontos_window,retas_window,poligonos_window, window_1, window_2, viewport_margem, viewport):
        super().__init__()

        self.pontos = pontos
        self.retas = retas
        self.poligonos = poligonos

        self.size_x = janela_2.x-janela_1.x
        self.size_y = janela_2.y-janela_1.y

        self.pontos_window = pontos_window
        self.retas_window = retas_window
        self.poligonos_window = poligonos_window

        self.window_x = window_2.x-window_1.x
        self.window_y = window_2.y-window_1.y

        #coordenadas na imagem resultante
        self.janela_1 = janela_1
        self.janela_2 = janela_2

        #coordenadas da window
        self.window_1 = window_1
        self.window_2 = window_2

        #coordenadas da viewport
        self.viewport_margem = viewport_margem
        self.viewport = viewport



        # Configuração do layout da janela
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Configuração do rótulo e canvas
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(self.size_x, self.size_y)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.layout.addWidget(self.label)

        # Adicionando botões
        self.button_up = QPushButton('↑', self)
        self.button_up.clicked.connect(self.move_up)
        self.layout.addWidget(self.button_up)

        self.button_left = QPushButton('←', self)
        self.button_left.clicked.connect(self.move_left)
        self.layout.addWidget(self.button_left)

        self.button_right = QPushButton('→', self)
        self.button_right.clicked.connect(self.move_right)
        self.layout.addWidget(self.button_right)

        self.button_down = QPushButton('↓', self)
        self.button_down.clicked.connect(self.move_down)
        self.layout.addWidget(self.button_down)

        self.draw_something()





    def atualizar_viewport(self):
        """
        pontos2 = [ ponto_window.copy() for ponto_window in self.pontos_window]
        retas2 = [reta_window.copy() for reta_window in self.retas_window]
        poligonos2 = [poligono_window.copy() for poligono_window in self.poligonos_window]

        window2 = []

        ponto001 = obj.Ponto(self.window_1.x, self.window_1.y)
        ponto002 = obj.Ponto(self.window_2.x, self.window_2.y)

        window2.append(ponto001)
        window2.append(ponto002)

        ponto003 = obj.Ponto(self.viewport_01.x, self.viewport_01.y)
        ponto004 = obj.Ponto(self.viewport_02.x, self.viewport_02.y)

        viewport2 = []

        viewport2.append(ponto003)
        viewport2.append(ponto004)

        print([ponto3.x for ponto3 in pontos2])

        ft.transformar2(pontos2,retas2,poligonos2,window2, viewport2)

        print([ponto3.x for ponto3 in pontos2])

        self.viewport_1.x = window2[0].x
        self.viewport_1.y = window2[0].y
        self.viewport_2.x = window2[1].x
        self.viewport_2.y = window2[1].y

        i = 0
        for ponto in self.pontos:
            ponto.x = pontos2[i].x
            ponto.y = pontos2[i].y
            i += 1


        i = 0
        for reta in self.retas:

           reta.ponto1.x = retas2[i].ponto1.x
           reta.ponto1.y = retas2[i].ponto1.y
           reta.ponto2.x = retas2[i].ponto2.x
           reta.ponto2.y = retas2[i].ponto2.y

           i += 1

        i = 0
        for poligono in self.poligonos:
            i2 = 0
            for ponto in poligono.pontos:
                ponto.x = poligonos2[i].pontos[i2].x
                ponto.y = poligonos2[i].pontos[i2].y

                i2+=1

            i+=1
            """

        i = 0
        print("pontos antes: ")
        for ponto in self.pontos_window:
            print("ponto " + str(i))
            print(ponto.x)
            print(ponto.y)
            i+=1

        window = []
        viewport = []

        ponto001 = obj.Ponto(self.window_1.x,self.window_1.y)
        ponto002 = obj.Ponto(self.window_2.x,self.window_2.y)

        ponto003 = obj.Ponto(self.viewport_margem.x, self.viewport_margem.y)
        ponto004 = obj.Ponto(self.viewport.x, self.viewport.y)

        window.append(ponto001)
        window.append(ponto002)

        viewport.append(ponto003)
        viewport.append(ponto004)


        #ft.transformar2(self.pontos_window, self.retas_window,self.poligonos_window, self.window, self.viewport)

        self.viewport[0].x = 10

        i = 0
        print("pontos depois: ")
        for ponto in self.pontos_window:
            print("ponto " + str(i))
            print(ponto.x)
            print(ponto.y)
            i += 1





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

        # Desenhando os polígonos na tela
        for poligono in self.poligonos:
            i = 0
            while(i < (len(poligono.pontos) - 1)):
                painter.drawLine(int(poligono.pontos[i].x), int(poligono.pontos[i].y), int(poligono.pontos[i + 1].x), int(poligono.pontos[i + 1].y))
                i += 1

            painter.drawLine(int(poligono.pontos[i].x), int(poligono.pontos[i].y), int(poligono.pontos[0].x), int(poligono.pontos[0].y))

        painter.end()
        self.label.setPixmap(canvas)
        self.create_tempWidget()

    # CRIA UM WIDGET TEMPORÁRIO PARA SALVAR A IMAGEM SEM OS BOTÕES 
    def create_tempWidget(self):
        # Criar um widget temporário
        temp_widget = QWidget()
        temp_layout = QVBoxLayout(temp_widget)
        temp_label = QLabel()
        temp_label.setPixmap(self.label.pixmap())
        temp_layout.addWidget(temp_label)

        # Redimensionar o widget temporário
        temp_widget.setFixedSize(temp_label.width(), temp_label.height())

        ##############################
        #     SALVANDO  A IMAGEM     #
        ##############################

        # Construir o caminho completo do arquivo de imagem
        filename = "imagem_resultado.png"
        filepath = os.path.join("output", filename)

        # Capturar a imagem do widget temporário
        screenshot = temp_widget.grab()
        screenshot.save(filepath)

        # Exibindo a imagem no notebook
        # Image(filename=screenshot)

