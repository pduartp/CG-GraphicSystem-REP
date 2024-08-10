# Importação das bibliotecas
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
import funcoesSegundoTrabalho as fs

"""
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
"""

# Função para capturar a tela da aplicação e salvar como uma imagem
def salvar_imagem(window, nome_arquivo):
    screenshot = window.grab()  # Captura a tela da janela
    screenshot.save(nome_arquivo)  # Salva a captura como uma imagem


### MAIN ###
if __name__ == '__main__':

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
                poligono.append(obj.Ponto(resultados[0], resultados[2]))

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
    poligono2 = obj.Poligono(pontos)

    ft.transformar2(pontos,retas,poligono,window,viewport)

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
    window = w.MainWindow(pontos, retas, poligono, int(window[1].x) - int(window[0].x), int(window[1].y) - int(window[0].y))

    window.show()

    ###########################
    #TRABALHO 2
    ###########################

    # TODO: IMPLEMENTAR BOTÕES PRESSIONÁVEIS
    #movimentando a tela
    entrada = input("mova a tela com as teclas \"a\',\"s\",\"d\",\"w\". digite 0 para parar \n ")

    while(entrada != 0):
    
        window.draw_something()
        window.show()
        entrada = input("mova a tela com as teclas \"a\',\"s\",\"d\",\"w\". digite 0 para parar \n ")
        if(entrada == "w"):
            fs.mover_para_cima(window)
        elif(entrada == "a"):
            fs.mover_para_esquerda(window)
        elif(entrada == "d"):
            fs.mover_para_direita(window)
        elif(entrada == "s"):
            fs.mover_para_baixo(window)

        elif(entrada == "o"):
            fs.mover_para_origem(window)
        elif(entrada == "e"):
            fs.mover_de_volta(window)    

    #movimentando a tela fim

    ###########################
    #TRABALHO 2 FIM
    ###########################

    #########  EXIBINDO IMAGEM  #########

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