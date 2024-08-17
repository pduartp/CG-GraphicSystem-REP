
############################################
#funções para o segundo trabalho
############################################   

#FUNÇÕES PARA MOVER A IMAGEM


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
