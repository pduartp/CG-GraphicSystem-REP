import math
import classObjGeometricos as obj
import re

############################################
#      funções para o segundo trabalho     #
############################################

################################
#   FUNÇÃO PARA MOVER IMAGEM   #
################################

def mover_para_cima(window):


    for ponto in window.pontos_window:
        ponto.y = ponto.y + 1

    for reta in window.retas_window:
        reta.ponto1.y = reta.ponto1.y + 1
        reta.ponto2.y = reta.ponto2.y + 1

    for poligono in window.poligonos_window:
        for ponto in poligono.pontos:
            ponto.y = ponto.y + 1

    window.atualizar_viewport()

def mover_para_baixo(window):
    for ponto in window.pontos_window:
        ponto.y = ponto.y - 1

    for reta in window.retas_window:
        reta.ponto1.y = reta.ponto1.y - 1
        reta.ponto2.y = reta.ponto2.y - 1

    for poligono in window.poligonos_window:
        for ponto in poligono.pontos:
            ponto.y = ponto.y - 1

    window.atualizar_viewport()

def mover_para_direita(window):
    for ponto in window.pontos_window:
        ponto.x = ponto.x + 1

    for reta in window.retas_window:
        reta.ponto1.x = reta.ponto1.x + 1
        reta.ponto2.x = reta.ponto2.x + 1

    for poligono in window.poligonos_window:
        for ponto in poligono.pontos:
            ponto.x = ponto.x + 1

    window.atualizar_viewport()

def mover_para_esquerda(window):
    for ponto in window.pontos_window:
        ponto.x = ponto.x - 1

    for reta in window.retas_window:
        reta.ponto1.x = reta.ponto1.x - 1
        reta.ponto2.x = reta.ponto2.x - 1

    for poligono in window.poligonos_window:
        for ponto in poligono.pontos:
            ponto.x = ponto.x - 1

    window.atualizar_viewport()

#####################################
#   FUNÇÃO PARA ROTACIONAR IMAGEM   #
#####################################

# usar matrizes homogêneas
# deslocar a imagem de modo que o centro corresponda ao centro da imagem, e não à coordenada 0,0
# aplicar a transformação e deslocar a imagem de volta

# Função para calcular o centro da janela
def calcular_centro(window):
    centro_x = (window.window_2.x-window.window_1.x)/2
    centro_y = (window.window_2.y-window.window_1.y)/2

    return centro_x, centro_y

# Função para aplicar rotação em torno de um ponto específico (cx, cy)
def aplicar_rotacao(ponto, angulo, cx, cy):
    # Converte o ângulo de graus para radianos
    angulo_rad = math.radians(angulo)

    # Translação do ponto para a origem
    x_novo = ponto.x - cx
    y_novo = ponto.y - cy

    # Aplicar a rotação
    x_rotacionado = x_novo * math.cos(angulo_rad) - y_novo * math.sin(angulo_rad)
    y_rotacionado = x_novo * math.sin(angulo_rad) + y_novo * math.cos(angulo_rad)

    # Translação de volta ao local original
    ponto.x = x_rotacionado + cx
    ponto.y = y_rotacionado + cy

# Função para rotacionar para a esquerda em 15°
def rotacionar_para_esquerda(window, angulo=15):
    cx, cy = calcular_centro(window)

    for ponto in window.pontos_window:
        aplicar_rotacao(ponto, angulo, cx, cy)

    for reta in window.retas_window:
        aplicar_rotacao(reta.ponto1, angulo, cx, cy)
        aplicar_rotacao(reta.ponto2, angulo, cx, cy)

    pontos_poligonos = []
    for i, poligono in enumerate(window.poligonos_window):
        for i2, ponto in enumerate(window.poligonos_window[i].pontos):
            pontos_poligonos.append(window.poligonos_window[i].pontos[i2])

    for ponto in pontos_poligonos:
        aplicar_rotacao(ponto, angulo, cx, cy)

    window.atualizar_viewport()

# Função para rotacionar para a direita em 15°
def rotacionar_para_direita(window, angulo=15):
    # Rotacionar à direita é o mesmo que rotacionar à esquerda com ângulo negativo
    rotacionar_para_esquerda(window, -angulo)

############################################################
#   FUNÇÕES PARA AUMENTAR OU REDUZIR O TAMANHO DA IMAGEM   #
############################################################

# usar matrizes homogêneas
# deslocar a imagem de modo que o centro corresponda ao centro da imagem, e não à coordenada 0,0
# aplicar a transformação e deslocar a imagem de volta

# Função para aplicar escala em torno de um ponto específico (cx, cy)
def aplicar_escala(ponto, fator_escala, cx, cy):
    # Translada o ponto para a origem
    x_novo = ponto.x - cx
    y_novo = ponto.y - cy

    # Aplica a escala
    x_escalado = x_novo * fator_escala
    y_escalado = y_novo * fator_escala

    # Translada o ponto de volta ao local original
    ponto.x = x_escalado + cx
    ponto.y = y_escalado + cy

# Função para ampliar a imagem em 10%
def escala_ampliar(window, fator_escala=1.1):
    # 10% de aumento
    cx, cy = calcular_centro(window)

    for ponto in window.pontos_window:
        aplicar_escala(ponto, fator_escala, cx, cy)

    for reta in window.retas_window:
        aplicar_escala(reta.ponto1, fator_escala, cx, cy)
        aplicar_escala(reta.ponto2, fator_escala, cx, cy)

    pontos_poligonos = []
    for i, poligono in enumerate(window.poligonos_window):

        for i2, ponto in enumerate(window.poligonos_window[i].pontos):
            pontos_poligonos.append(window.poligonos_window[i].pontos[i2])

    for ponto in pontos_poligonos:
        aplicar_escala(ponto, fator_escala, cx, cy)

    window.atualizar_viewport()

# Função para reduzir a imagem em 10%
def escala_diminuir(window, fator_escala=0.9):
    # Redução é uma ampliação com fator < 1
    escala_ampliar(window, fator_escala)

##################################################################
#   FUNÇÕES PARA ADICIONAR OBJETOS: PONTOS, LINHAS E POLIGONOS   #
##################################################################

# TODO: IMPLEMENTAR

def adicionar_ponto(window,coordenadas):


    resultados = re.findall(r'\d+', coordenadas)


    ponto = obj.Ponto(float(resultados[0]),float(resultados[1]))
    window.pontos_window.append(ponto)
    window.pontos.append(ponto)

    window.atualizar_viewport()


def adicionar_linha(window,coordenadas):


    resultados = re.findall(r'\d+', coordenadas)

    ponto = obj.Ponto(float(resultados[0]),float(resultados[1]))

    ponto2 = obj.Ponto(float(resultados[2]),float(resultados[3]))

    reta = obj.Reta(ponto,ponto2)
    window.retas_window.append(reta)
    window.retas.append(reta)

    window.atualizar_viewport()

def adicionar_poligono(window,coordenadas):


    resultados = re.findall(r'\d+', coordenadas)


    pontos = []

    for i, number in enumerate(resultados):
        if i>0:
            pontos.append(obj.Ponto(float(resultados[i-1]),float(resultados[i])))


    poligono = obj.Poligono(pontos)


    window.poligonos_window.append(poligono)
    window.poligonos.append(poligono)

    window.atualizar_viewport()



##################################
#   FUNÇÃO PARA RESETAR A WINDOW #
##################################

# TODO: IMPLEMENTAR

def resetar_window(window):


    for i, ponto in enumerate(window.pontos_window):

        if i < len(window.pontos_window_iniciais):
            window.pontos_window[i] = window.pontos_window_iniciais[i].copy()
        else:
            while (len(window.pontos_window) > len(window.pontos_window_iniciais)):
                window.pontos_window.pop(i)
                window.pontos.pop(i)

    for i, reta in enumerate(window.retas_window):

        if i < len(window.retas_window_iniciais):
            window.retas_window[i] = window.retas_window_iniciais[i].copy()
        else:
            while (len(window.retas_window) > len(window.retas_window_iniciais)):
                window.retas_window.pop(i)
                window.retas.pop(i)

    for i, poligono in enumerate(window.poligonos_window):

        if i < len(window.poligonos_window_iniciais):
            for i2, ponto in enumerate(window.poligonos_window[i].pontos):
                window.poligonos_window[i].pontos[i2] = window.poligonos_window_iniciais[i].pontos[i2].copy()
        else:
            while(len(window.poligonos_window) > len(window.poligonos_window_iniciais)):
                window.poligonos_window.pop(i)
                window.poligonos.pop(i)

    window.atualizar_viewport()

