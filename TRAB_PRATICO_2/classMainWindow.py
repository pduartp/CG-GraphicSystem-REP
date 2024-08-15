from PyQt6 import QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QLabel
from IPython.display import Image
import os

# TODO: DESMEMBRAR EM ARQUIVOS
import segundoTrabalho.funcoesSegundoTrabalho as fs

# Classe para a janela principal da aplicação
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, pontos, retas, poligono, window_x, window_y):
        super().__init__()

        self.pontos = pontos
        self.retas = retas
        self.poligono = poligono

        self.size_x = window_x
        self.size_y = window_y

        # Configuração do layout da janela
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Configuração do rótulo e canvas
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(window_x, window_y)
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

        # Desenhando o polígono na tela
        i = 0
        while(i < (len(self.poligono) - 1)):
            painter.drawLine(int(self.poligono[i].x), int(self.poligono[i].y), int(self.poligono[i + 1].x), int(self.poligono[i + 1].y))
            i += 1

        painter.drawLine(int(self.poligono[i].x), int(self.poligono[i].y), int(self.poligono[0].x), int(self.poligono[0].y))

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

