'''
Crie um projeto contendo as classes:

Quadrado, Retângulo e Círculo, crie também uma interface chamada AreaCalculavel que será implementada pelas classes.

Essa interface conterá um método que calcula a área:
Área do Quadrado = lado*lado;
Área do Retangulo = largura * altura;
Área do Círculo = π*r^2

Crie uma classe principal Teste instanciando os objetos passando valores via construtor, e exibe no console o cálculo da área.
'''
# Classes em python
class Quadrado:
    def __init__(self, lado):
        self.lado = lado
        self.__ferramenta = None

# objeto do calculo da area
    @property
    def areaQuadrado(self, lado):
        return self.lado * lado
# resposta
    def respostaQuadrado(self):
        print(f'A área do quadrado é {self.areaQuadrado} ')



class Retangulo:
    def __init__(self, largura):
        self.lardura = largura


    @property
    def areaRetangulo(self, largura):
        return self.largura * largura


    def respostaRetangulo(self):
        print(f'A área do reatgulo é {self.areaRetangulo} ')


class Circulo:
    def __init__(self, raio):
        self.raio = raio


    @property
    def areaCirculo(self, raio):
        self.raio = (raio * 3.14) ** 2
        return self.raio


    def respostaCirculo(self):
        print(f'A areado cículo é {self.areaCirculo} ')

quadrado = Quadrado(4)
circulo = Circulo(10)
retangulo =  Retangulo(8)


quadrado.respostaQuadrado()
retangulo.respostaRetangulo()
circulo.respostaCirculo()

