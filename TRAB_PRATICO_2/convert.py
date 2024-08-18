# Importação das bibliotecas
import sys
import re
import xml.etree.ElementTree as ET
from PyQt6 import QtWidgets

import classObjGeometricos as obj
import funcTransformacao as ft
import classMainWindow as w
import os
import shutil

#converte os valores lidos do arquivo para tipo inteiro

def to_int(pontos,retas,poligonos,window,viewport):
    window[0].x = int(window[0].x)
    window[0].y = int(window[0].y)
    window[1].x = int(window[1].x)
    window[1].y = int(window[1].y)

    viewport[0].x = int(viewport[0].x)
    viewport[0].y = int(viewport[0].y)
    viewport[1].x = int(viewport[1].x)
    viewport[1].y = int(viewport[1].y)

    for ponto in pontos:
        ponto.x = int(ponto.x)
        ponto.y = int(ponto.y)

    for reta in retas:
        reta.ponto1.x = int(reta.ponto1.x)
        reta.ponto2.x = int(reta.ponto2.x)
        reta.ponto1.y = int(reta.ponto1.y)
        reta.ponto2.y = int(reta.ponto2.y)

    for poligono in poligonos:
        for ponto in poligono.pontos:
            ponto.x = int(ponto.x)
            ponto.y = int(ponto.y)

def to_float(pontos,retas,poligonos,window,viewport):
    window[0].x = float(window[0].x)
    window[0].y = float(window[0].y)
    window[1].x = float(window[1].x)
    window[1].y = float(window[1].y)

    viewport[0].x = float(viewport[0].x)
    viewport[0].y = float(viewport[0].y)
    viewport[1].x = float(viewport[1].x)
    viewport[1].y = float(viewport[1].y)



    for ponto in pontos:
        ponto.x = float(ponto.x)
        ponto.y = float(ponto.y)

    for reta in retas:
        reta.ponto1.x = float(reta.ponto1.x)
        reta.ponto2.x = float(reta.ponto2.x)
        reta.ponto1.y = float(reta.ponto1.y)
        reta.ponto2.y = float(reta.ponto2.y)

    for poligono in poligonos:
        for ponto in poligono.pontos:
            ponto.x = float(ponto.x)
            ponto.y = float(ponto.y)

