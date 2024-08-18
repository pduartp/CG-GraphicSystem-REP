
import math

############################################
#      funções para o segundo trabalho     #
############################################

################################
#   FUNÇÃO PARA MOVER IMAGEM   #
################################


"""
def mover_para_cima(window):

    for ponto in window.pontos:        
        ponto.y = ponto.y-1

    for reta in window.retas:      
        reta.ponto1.y = reta.ponto1.y -1
        reta.ponto2.y = reta.ponto2.y-1

    for poligono in window.poligonos:
        for ponto in poligono:
            ponto.y = ponto.y - 1
 

def mover_para_baixo(window):
 
    for ponto in window.pontos:        
        ponto.y = ponto.y+1

    for reta in window.retas:      
        reta.ponto1.y = reta.ponto1.y +1
        reta.ponto2.y = reta.ponto2.y +1

    for poligono in window.poligonos:
        for ponto in poligono:
            ponto.y = ponto.y + 1


def mover_para_direita(window):  

    for ponto in window.pontos:        
        ponto.x = ponto.x+1

    for reta in window.retas:      
        reta.ponto1.x = reta.ponto1.x +1
        reta.ponto2.x = reta.ponto2.x +1

    for poligono in window.poligonos:
        for ponto in poligono:
            ponto.x = ponto.x + 1


def mover_para_esquerda(window):

    for ponto in window.pontos:        
        ponto.x = ponto.x - 1

    for reta in window.retas:      
        reta.ponto1.x = reta.ponto1.x - 1
        reta.ponto2.x = reta.ponto2.x - 1

    for poligono in window.poligonos:
        for ponto in poligono:
            ponto.x = ponto.x - 1

"""



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

    #para guardar os pontos dos polígonos
    pontos_poligonos = []
    for i, poligono in enumerate(window.poligonos_window):

        for i2, ponto in enumerate(window.poligonos_window[i].pontos):

            pontos_poligonos.append(window.poligonos_window[i].pontos[i2])


    # Supondo que `window.pontos`, `window.retas` e `window.poligono` são listas de pontos (x, y)
    todos_pontos = window.pontos_window + [reta.ponto1 for reta in window.retas_window] + [reta.ponto2 for reta in
                                                                                 window.retas_window] + pontos_poligonos
    soma_x = sum(ponto.x for ponto in todos_pontos)
    soma_y = sum(ponto.y for ponto in todos_pontos)
    centro_x = soma_x / len(todos_pontos)
    centro_y = soma_y / len(todos_pontos)
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

    #####################
    pontos_poligonos = []
    for i, poligono in enumerate(window.poligonos_window):

        for i2, ponto in enumerate(window.poligonos_window[i].pontos):
            pontos_poligonos.append(window.poligonos_window[i].pontos[i2])

    #####################

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

    for ponto in window.pontos:
        aplicar_escala(ponto, fator_escala, cx, cy)

    for reta in window.retas:
        aplicar_escala(reta.ponto1, fator_escala, cx, cy)
        aplicar_escala(reta.ponto2, fator_escala, cx, cy)

    for ponto in window.poligono:
        aplicar_escala(ponto, fator_escala, cx, cy)

# Função para reduzir a imagem em 10%
def escala_diminuir(window, fator_escala=0.9):
    # Redução é uma ampliação com fator < 1
    escala_ampliar(window, fator_escala)

#   funções para o segundo trabalho fim    #
