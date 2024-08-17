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

import convert

if __name__ == '__main__':

    # Parsing do arquivo XML de entrada
    tree = ET.parse('entrada.xml')
    root = tree.getroot()
    e = root[0][1].text

    # Listas para armazenar os pontos, retas e polígono
    pontos = []
    retas = []
    poligonos = []
    viewport = []
    window = []

    pontos3 = []
    poligono = obj.Poligono(pontos3)

    # Iterando sobre os elementos do XML
    for child in root:
        if (child.tag == 'viewport'):
            for child01 in child:
                if((child01.tag == 'vpmin') or (child01.tag == 'vpmax')):
                    resultados = re.findall(r'\d+', str(child01.attrib))
                    viewport.append(obj.Ponto(resultados[0], resultados[1]))

        elif(child.tag == 'window'):
            for child02 in child:
                resultados = re.findall(r'\d+', str(child02.attrib))
                window.append(obj.Ponto(resultados[0], resultados[2]))

        elif (child.tag == 'ponto'):
            resultados = re.findall(r'\d+', str(child.attrib))
            pontos.append(obj.Ponto(resultados[0], resultados[1]))

        elif (child.tag == 'reta'):
            pontos_da_reta =[]

            for child2 in child:
                resultados = re.findall(r'\d+', str(child2.attrib))
                pontos_da_reta.append(obj.Ponto(resultados[0], resultados[1]))
            
            retas.append(obj.Reta(pontos_da_reta[0], pontos_da_reta[1]))


        elif (child.tag == 'poligono'):
            for child3 in child:
                resultados = re.findall(r'\d+', str(child3.attrib))
                poligono.pontos.append(obj.Ponto(resultados[0], resultados[2]))
            poligonos.append(poligono)

    #classe polígono
    #poligono2 = obj.Poligono(pontos)

    #window antes da transformação
    window1 = []
    window1.append(window[0])
    window1.append(window[1])



    #######################################################
    #   CRIANDO E EXIBINDO A JANELA DA APLICAÇÃO GRÁFICA  #
    #######################################################

    convert.to_int(pontos,retas,poligonos,window,viewport)

    pontos2 = [ponto.copy() for ponto in pontos]
    retas2 =[reta.copy() for reta in retas]
    poligonos2 = [poligono.copy() for poligono in poligonos]



    ft.transformar2(pontos, retas, poligonos, window, viewport)


    # Criando e exibindo a janela da aplicação gráfica
    app = QtWidgets.QApplication(sys.argv)
    window = w.MainWindow(pontos, retas, poligonos, window[0], window[1],    pontos2, retas2, poligonos2, window1[0], window1[1], viewport[0], viewport[1])
    window.show()
    app.exec()

    # ADICIONANDO UM DIRETÓRIO "output" para armazenar os arquivos de saída se não existir
    os.makedirs("output", exist_ok=True)
    
    ##############################
    #   SALVANDO ARQUIVO   XML   #
    ##############################

    # Escrevendo os dados no arquivo de saída no formato XMLs
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
    for ponto in poligono.pontos:
        arquivo.write("        <ponto x=\"" + str(int(ponto.x) - int(margem_x)) + "\" y=\"" + str(int(ponto.y) - int(margem_y)) + "\"/>\n")
    arquivo.write("    </poligono>\n")
    arquivo.write("</dados>")
    arquivo.close()
    
    # Mover o arquivo para a pasta output
    destination = os.path.join("output", "saida.xml")
    shutil.move("saida.xml", destination)
