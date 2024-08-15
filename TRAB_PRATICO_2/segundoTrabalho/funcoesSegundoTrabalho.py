############################################
#funções para o segundo trabalho
############################################   

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