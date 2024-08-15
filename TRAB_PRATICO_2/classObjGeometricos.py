# Definindo as classes para representar os objetos geométricos
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Reta:
    def __init__(self, Ponto1, Ponto2):
        self.ponto1 = Ponto1
        self.ponto2 = Ponto2

class Poligono:

    def __init__(self,pontos):
        self.pontos = []
        tamanho = len(pontos)
        i = 0
        while(i<tamanho):
            self.pontos.append(pontos[i])
            i+=1