# Importação das bibliotecas
import sys
import re
import xml.etree.ElementTree as ET
from random import randint
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication
from IPython.display import Image

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


#transforma um ponto
def transformar_ponto(coordenada, window, viewport):
    xwmin, ywmin = window[0].x, window[0].y
    xwmax, ywmax = window[1].x, window[1].y
    xvmin, yvmin = viewport[0].x, viewport[0].y
    xvmax, yvmax = viewport[1].x, viewport[1].y

    xv = xvmin + (coordenada.x - xwmin) * (xvmax - xvmin) / (xwmax - xwmin)
    yv = yvmin + (coordenada.y - ywmin) * (yvmax - yvmin) / (ywmax - ywmin)

    return Ponto(xv, yv)

# Função para transformar as coordenadas dos objetos para o sistema de coordenadas da viewport
# não aplica margem
# não inverte o y
def transformar(window, viewport, pontos, retas, poligono):
    viewport_x = int(viewport[1].x) - int(viewport[0].x)
    viewport_y = int(viewport[1].y) - int(viewport[0].y)

    window_x = int(window[1].x) - int(window[0].x)
    window_y = int(window[1].y) - int(window[0].y)

    largura = viewport_x / window_x
    altura = viewport_y / window_y

    # Aplicando a transformação nos pontos
    for ponto in pontos:
        ponto.x = int(ponto.x) * largura
        ponto.y = int(ponto.y) * altura

    # Aplicando a transformação nas retas
    for reta in retas:
        reta.ponto1.x = int(reta.ponto1.x) * largura
        reta.ponto2.x = int(reta.ponto2.x) * largura
        reta.ponto1.y = int(reta.ponto1.y) * altura
        reta.ponto2.y = int(reta.ponto2.y) * altura

    # Aplicando a transformação no polígono
    for ponto in poligono:
        ponto.x = int(ponto.x) * largura
        ponto.y = int(ponto.y) * altura

    # Atualizando os limites da window para os da viewport
    window[0].x = 0
    window[0].y = 0
    window[1].x = viewport_x
    window[1].y = viewport_y

# Função para adicionar margem à viewport
def adicionar_margem(window, viewport, pontos, retas, poligono):
    margem_y = int(viewport[0].y)
    margem_x = int(viewport[0].x)

    # Adicionando margem acima e abaixo
    window[1].y = window[1].y + margem_y * 2

    for ponto in pontos:
        ponto.y = ponto.y + margem_y

    for reta in retas:
        reta.ponto1.y = reta.ponto1.y + margem_y
        reta.ponto2.y = reta.ponto2.y + margem_y

    for ponto in poligono:
        ponto.y = ponto.y + margem_y

    # Adicionando margem à esquerda e à direita
    window[1].x = window[1].x + margem_x * 2

    for ponto in pontos:
        ponto.x = ponto.x + margem_x

    for reta in retas:
        reta.ponto1.x = reta.ponto1.x + margem_x
        reta.ponto2.x = reta.ponto2.x + margem_x

    for ponto in poligono:
        ponto.x = ponto.x + margem_x

# Função para inverter a coordenada y
def inverter_y(window, pontos, retas, poligono):
    for ponto in pontos:
        ponto.y = window[1].y - ponto.y

    for reta in retas:
        reta.ponto1.y = window[1].y - reta.ponto1.y
        reta.ponto2.y = window[1].y - reta.ponto2.y

    for ponto in poligono:
        ponto.y = window[1].y - ponto.y


#função para transformar os pontos para o sistema de coordenadas da viewport com a margem e o y invertido
def transformar2(pontos,retas,poligono,window,viewport):

    """
    #xvp = ((xw - xwmin)/(xwmax-xwmin)) * (xvpmax - xvpmin)
    #yvp = (1- (yw - ywmin) * (yvpmax - yvpmin)


    #converter para int
    for ponto in pontos:
        ponto.x = int(ponto.x)
        ponto.y = int(ponto.y)

    for reta in retas:
        reta.ponto1.x = int(reta.ponto1.x)
        reta.ponto1.y = int(reta.ponto1.y)
        reta.ponto2.x = int(reta.ponto2.x)
        reta.ponto2.y = int(reta.ponto2.y)

    for ponto in poligono.pontos:
        ponto.x = int(ponto.x)
        ponto.y = int(ponto.y)

    for ponto in viewport:
        ponto.x = int(ponto.x)
        ponto.y = int(ponto.y)

    for ponto in window:
        ponto.x = int(ponto.x)
        ponto.y = int(ponto.y)

    # Aplicando a transformação nos pontos
    for ponto in pontos:
        ponto.x = int((float((ponto.x - window[0].x)/(window[1].x - window[0].x)) * (viewport[1].x - viewport[0].x)))
        ponto.y = int((1.0 - float(float(ponto.y - window[0].y)/float(window[1].y - window[0].y)) * float(viewport[1].y - viewport[0].y)))
        #transformar3(ponto,window,viewport)

    # Aplicando a transformação nas retas
    for reta in retas:
        reta.ponto1.x = ((reta.ponto1.x - window[0].x)/(window[1].x - window[0].x)) * (viewport[1].x - viewport[0].x)
        reta.ponto2.x = ((reta.ponto2.x - window[0].x)/(window[1].x - window[0].x)) * (viewport[1].x - viewport[0].x)

        reta.ponto1.y = (1 - ((reta.ponto1.y - window[0].y)/(window[1].y - window[0].y )) *(viewport[1].y - viewport[0].y))
        reta.ponto2.y = (1 - ((reta.ponto2.y - window[0].y)/(window[1].y - window[0].y )) *(viewport[1].y - viewport[0].y))

    # Aplicando a transformação no polígono
    for ponto in poligono.pontos:
        ponto.x = ((ponto.x - window[0].x)/(window[1].x - window[0].x)) * (viewport[1].x - viewport[0].x)
        ponto.y = (1 - ((ponto.y - window[0].y)/(window[1].y - window[0].y )) *(viewport[1].y - viewport[0].y))

    """
    viewport_x = int(viewport[1].x) - int(viewport[0].x)
    viewport_y = int(viewport[1].y) - int(viewport[0].y)

    window_x = int(window[1].x) - int(window[0].x)
    window_y = int(window[1].y) - int(window[0].y)

    largura = viewport_x / window_x
    altura = viewport_y / window_y

    margem_y = int(viewport[0].y)
    margem_x = int(viewport[0].x)



    # Aplicando a transformação nos pontos
    for ponto in pontos:
        ponto.x = (int(ponto.x) * largura) + margem_x
        ponto.y = int(viewport_y) - ((int(ponto.y) * altura)) + margem_y

    # Aplicando a transformação nas retas
    for reta in retas:
        reta.ponto1.x = (int(reta.ponto1.x) * largura) + margem_x
        reta.ponto2.x = (int(reta.ponto2.x) * largura) + margem_x
        reta.ponto1.y = int(viewport_y) - ((int(reta.ponto1.y) * altura)) + margem_y
        reta.ponto2.y = int(viewport_y) - ((int(reta.ponto2.y) * altura)) + margem_y

    # Aplicando a transformação no polígono
    for ponto in poligono:
        ponto.x = (int(ponto.x) * largura) + margem_x
        ponto.y = int(viewport_y) - ((int(ponto.y) * altura)) + margem_y

    # Atualizando os limites da window para os da viewport
    window[0].x = 0
    window[0].y = 0
    window[1].x = viewport_x + margem_x
    window[1].y = viewport_y + margem_y

############################################
#funções para o segundo trabalho
############################################

#FUNÇÕES PARA DESLOCAR A IMAGEM DE MODO QUE O CENTRO FIQUE NA COORDENADA 0,0 E DEPOIS VOLTAR

def mover_para_origem(window):

    for ponto in pontos:        
        ponto.y = ponto.y+(window.size_y/2)

    for reta in retas:      
        reta.ponto1.y = reta.ponto1.y +(window.size_y/2)
        reta.ponto2.y = reta.ponto2.y +(window.size_y/2)

    for ponto in poligono:    
        ponto.y = ponto.y +(window.size_y/2)


    for ponto in pontos:        
        ponto.x= ponto.x-(window.size_x/2)

    for reta in retas:      
        reta.ponto1.x = reta.ponto1.x -(window.size_x/2)
        reta.ponto2.x = reta.ponto2.x -(window.size_x/2)

    for ponto in poligono:    
        ponto.x = ponto.x -(window.size_x/2)    

def mover_de_volta(window):

    for ponto in pontos:        
        ponto.y = ponto.y-(window.size_y/2)

    for reta in retas:      
        reta.ponto1.y = reta.ponto1.y -(window.size_y/2)
        reta.ponto2.y = reta.ponto2.y -(window.size_y/2)

    for ponto in poligono:    
        ponto.y = ponto.y -(window.size_y/2)


    for ponto in pontos:        
        ponto.x= ponto.x +(window.size_x/2)

    for reta in retas:      
        reta.ponto1.x = reta.ponto1.x +(window.size_x/2)
        reta.ponto2.x = reta.ponto2.x +(window.size_x/2)

    for ponto in poligono:    
        ponto.x = ponto.x +(window.size_x/2)  
   

#FUNÇÕES PARA MOVER A IMAGEM

def mover_para_cima(window):

    for ponto in pontos:        
        ponto.y = ponto.y-1

    for reta in retas:      
        reta.ponto1.y = reta.ponto1.y -1
        reta.ponto2.y = reta.ponto2.y-1

    for ponto in poligono:    
        ponto.y = ponto.y-1
 

def mover_para_baixo(window):
 
    for ponto in window.pontos:        
        ponto.y = ponto.y+1

    for reta in window.retas:      
        reta.ponto1.y = reta.ponto1.y +1
        reta.ponto2.y = reta.ponto2.y +1

    for ponto in window.poligono:    
        ponto.y = ponto.y+1


def mover_para_direita(window):  

    for ponto in window.pontos:        
        ponto.x = ponto.x+1

    for reta in window.retas:      
        reta.ponto1.x = reta.ponto1.x +1
        reta.ponto2.x = reta.ponto2.x +1

    for ponto in window.poligono:    
        ponto.x = ponto.x+1


def mover_para_esquerda(window):

    for ponto in window.pontos:        
        ponto.x = ponto.x - 1

    for reta in window.retas:      
        reta.ponto1.x = reta.ponto1.x - 1
        reta.ponto2.x = reta.ponto2.x - 1

    for ponto in window.poligono:    
        ponto.x = ponto.x - 1


#FUNÇÕES PARA ROTACIONAR A IMAGEM

#usar matrizes homogêneas
#deslocar a imagem de modo que o centro corresponda ao centro da imagem, e não à coordenada 0,0
#aplicar a transformação e deslocar a imagem de volta


#FUNÇÕES PARA AUMENTAR OU REDUZIR O TAMANHO DA IMAGEM

#usar matrizes homogêneas
#deslocar a imagem de modo que o centro corresponda ao centro da imagem, e não à coordenada 0,0
#aplicar a transformação e deslocar a imagem de volta



############################################
#funções para o segundo trabalho fim
############################################


# Classe para a janela principal da aplicação
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, pontos, retas, poligono, window_x, window_y):
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(window_x, window_y)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

        self.pontos = pontos
        self.retas = retas
        self.poligono = poligono

        self.size_x = window_x
        self.size_y = window_y

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
        for ponto in pontos:
            painter.drawPoint(int(ponto.x), int(ponto.y))

        # Desenhando as retas na tela
        for reta in retas:
            painter.drawLine(int(reta.ponto1.x), int(reta.ponto1.y), int(reta.ponto2.x), int(reta.ponto2.y))

        # Desenhando o polígono na tela
        i = 0
        while(i < (len(poligono) - 1)):
            painter.drawLine(int(poligono[i].x), int(poligono[i].y), int(poligono[i + 1].x), int(poligono[i + 1].y))
            i += 1

        painter.drawLine(int(poligono[i].x), int(poligono[i].y), int(poligono[0].x), int(poligono[0].y))

        painter.end()
        self.label.setPixmap(canvas)

# Função para capturar a tela da aplicação e salvar como uma imagem
def salvar_imagem(window, nome_arquivo):
    screenshot = window.grab()  # Captura a tela da janela
    screenshot.save(nome_arquivo)  # Salva a captura como uma imagem

# Parsing do arquivo XML de entrada
tree = ET.parse('entrada.xml')
root = tree.getroot()

e = root[0][1].text

# Imprimindo a tag da raiz
print(root.tag)

# Listas para armazenar os pontos, retas e polígono
pontos = []
retas = []
poligono = []

viewport = []
window = []

# Iterando sobre os elementos do XML
for child in root:
    if (child.tag == 'viewport'):
        for child01 in child:
            if((child01.tag == 'vpmin') or (child01.tag == 'vpmax')):
                resultados = re.findall(r'\d+', str(child01.attrib))
                viewport.append(Ponto(resultados[0], resultados[1]))

    elif(child.tag == 'window'):
        for child02 in child:
            resultados = re.findall(r'\d+', str(child02.attrib))
            window.append(Ponto(resultados[0], resultados[2]))

    elif (child.tag == 'ponto'):
        resultados = re.findall(r'\d+', str(child.attrib))
        pontos.append(Ponto(resultados[0], resultados[1]))

    elif (child.tag == 'reta'):
        pontos_da_reta =[]
        for child2 in child:
            resultados = re.findall(r'\d+', str(child2.attrib))
            pontos_da_reta.append(Ponto(resultados[0], resultados[1]))
        retas.append(Reta(pontos_da_reta[0], pontos_da_reta[1]))

    elif (child.tag == 'poligono'):
        for child3 in child:
            resultados = re.findall(r'\d+', str(child3.attrib))
            poligono.append(Ponto(resultados[0], resultados[2]))

# Imprimindo os pontos, retas, viewport e window antes da transformação
print('pontos: ')
for ponto in pontos:
    print('coordenadas do ponto:')
    print(ponto.x)
    print(ponto.y)

for reta in retas:
    print('pontos da reta:')
    print('ponto 1 da reta: ')
    print(reta.ponto1.x)
    print(reta.ponto1.y)
    print('ponto 2 da reta: ')
    print(reta.ponto2.x)
    print(reta.ponto2.y)
    print('')

print('pontos do polígono: ')
for pontos2 in poligono:
    print('ponto: ')
    print(pontos2.x)
    print(pontos2.y)

print('viewport: ')
print(viewport[0].x)
print(viewport[0].y)
print('')
print(viewport[1].x)
print(viewport[1].y)

print('window: ')
print(window[0].x)
print(window[0].y)
print('')
print(window[1].x)
print(window[1].y)

#classe polígono
poligono2 = Poligono(pontos)

"""
# Transformando os objetos para o sistema de coordenadas da viewport
transformar(window, viewport, pontos, retas, poligono)

# Adicionando margem à viewport
adicionar_margem(window, viewport, pontos, retas, poligono)

# Invertendo a coordenada y
inverter_y(window, pontos, retas, poligono)
"""

transformar2(pontos,retas,poligono,window,viewport)

# Imprimindo os pontos, retas, viewport e window após a transformação
print('pontos após a transformação: ')
print('pontos: ')
for ponto in pontos:
    print('coordenadas do ponto:')
    print(ponto.x)
    print(ponto.y)

for reta in retas:
    print('pontos da reta:')
    print('ponto 1 da reta: ')
    print(reta.ponto1.x)
    print(reta.ponto1.y)
    print('ponto 2 da reta: ')
    print(reta.ponto2.x)
    print(reta.ponto2.y)
    print('')

print('pontos do polígono: ')
for pontos2 in poligono:
    print('ponto: ')
    print(pontos2.x)
    print(pontos2.y)

print('viewport: ')
print(viewport[0].x)
print(viewport[0].y)
print('')
print(viewport[1].x)
print(viewport[1].y)

print('window: ')
print(window[0].x)
print(window[0].y)
print('')
print(window[1].x)
print(window[1].y)

# Escrevendo os dados no arquivo de saída no formato XML
arquivo = open("saida.xml", "w")
arquivo.write("<?xml version=\"1.0\" ?>\n")
arquivo.write("<dados>\n")
margem_x = int(viewport[0].x)
margem_y = int(viewport[0].y)

for ponto in pontos:
    arquivo.write("    <ponto x=\"" + str(ponto.x - margem_x) + "\" y=\"" + str(ponto.y - margem_y) + "\"/>\n")


for reta in retas:
    arquivo.write("\n")
    arquivo.write("    <reta>\n")
    arquivo.write("        <ponto x1=\"" + str(reta.ponto1.x - margem_x) + "\" y1=\"" + str(reta.ponto1.y - margem_y) + "\"/>\n")
    arquivo.write("        <ponto x1=\"" + str(reta.ponto2.x - margem_x) + "\" y1=\"" + str(reta.ponto2.y - margem_y) + "\"/>\n")

    arquivo.write("    </reta>\n")
arquivo.write("\n")

arquivo.write("    <poligono>\n")
for ponto in poligono:
    arquivo.write("        <ponto x=\"" + str(int(ponto.x) - int(margem_x)) + "\" y=\"" + str(int(ponto.y) - int(margem_y)) + "\"/>\n")
arquivo.write("    </poligono>\n")
arquivo.write("</dados>")
arquivo.close()

# Criando e exibindo a janela da aplicação gráfica
app = QtWidgets.QApplication(sys.argv)
#window = MainWindow(pontos, retas, poligono, int(window[1].x) - int(window[0].x), int(window[1].y) - int(window[0].y))
window = MainWindow(pontos, retas, poligono, int(window[1].x) - int(window[0].x), int(window[1].y) - int(window[0].y))

window.show()


###########################
#TRABALHO 2
###########################

#movimentando a tela

entrada = input("mova a tela com as teclas \"a\',\"s\",\"d\",\"w\". digite 0 para parar \n ")

while(entrada != "0"):
   
    window.draw_something()
    window.show()
    entrada = input("mova a tela com as teclas \"a\',\"s\",\"d\",\"w\". digite 0 para parar \n ")
    if(entrada == "w"):
        mover_para_cima(window)
    elif(entrada == "a"):
        mover_para_esquerda(window)
    elif(entrada == "d"):
        mover_para_direita(window)
    elif(entrada == "s"):
        mover_para_baixo(window)

    elif(entrada == "o"):
        mover_para_origem(window)
    elif(entrada == "e"):
        mover_de_volta(window)    

#movimentando a tela fim



###########################
#TRABALHO 2 FIM
###########################

#window.show()
app.exec()

# Salvando a imagem resultante
nome_arquivo_imagem = "imagem_resultado.png"
salvar_imagem(window, nome_arquivo_imagem)
print("Imagem salva como:", nome_arquivo_imagem)

# Caminho da imagem salva
caminho_imagem = "imagem_resultado.png"

# Exibindo a imagem no notebook
Image(filename=caminho_imagem)