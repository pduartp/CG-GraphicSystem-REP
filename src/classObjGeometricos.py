# Definindo as classes para representar os objetos geométricos
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def copy(self):
        return Ponto(self.x, self.y)

class Reta:
    def __init__(self, Ponto1, Ponto2):
        self.ponto1 = Ponto1
        self.ponto2 = Ponto2

    def copy(self):
        ponto01 = Ponto(self.ponto1.x,self.ponto1.y)
        ponto02 = Ponto(self.ponto2.x,self.ponto2.y)
        return Reta(ponto01,ponto02)

class Poligono:
    def __init__(self,pontos1):
        tamanho = len(pontos1)
        self.pontos = []
        self.pontos.extend(pontos1[i] for i in range(tamanho))

    def copy(self):
        pontos2 = []
        for ponto in self.pontos:
            ponto1 = ponto.copy()
            pontos2.append(ponto1)

        return Poligono(pontos2)
