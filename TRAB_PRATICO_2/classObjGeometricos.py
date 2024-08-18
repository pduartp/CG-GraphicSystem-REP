# Definindo as classes para representar os objetos geométricos
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def copy(self):
        ponto2 = Ponto(self.x, self.y)
        return ponto2

class Reta:
    def __init__(self, Ponto1, Ponto2):
        self.ponto1 = Ponto1
        self.ponto2 = Ponto2

    def copy(self):
        ponto01 = Ponto(self.ponto1.x,self.ponto1.y)
        ponto02 = Ponto(self.ponto2.x,self.ponto2.y)
        reta2 = Reta(ponto01,ponto02)
        return reta2

class Poligono:
    def __init__(self,pontos1):
        tamanho = len(pontos1)
        self.pontos = []
        i = 0
        while(i<tamanho):
            self.pontos.append(pontos1[i])
            i+=1

    def copy(self):
        pontos2 = []
        for ponto in self.pontos:
            ponto1 = ponto.copy()
            pontos2.append(ponto1)

        poligono2 = Poligono(pontos2)

        return poligono2
