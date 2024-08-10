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
import classMainWindow as w

# TODO: DESMEMBRAR EM ARQUIVOS
# import funcoesSegundoTrabalho as fs

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

    for ponto in window.pontos:        
        ponto.y = ponto.y-1

    for reta in window.retas:      
        reta.ponto1.y = reta.ponto1.y -1
        reta.ponto2.y = reta.ponto2.y-1

    for ponto in window.poligono:    
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