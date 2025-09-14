import math
import math

# 🔹 Desafio 1 – Nível Fácil

print("\nCálculo de Raiz Quadrada")

numero = int(input("\nNúmero: "))

def raizQuadrada(numero):
    return round(math.sqrt(numero))

print(f"\nRaiz: {raizQuadrada(numero)}\n")

# 🔹 Desafio 2 – Nível Médio

print("\nArredondamento (cima, baixo e inteiro mais próximo)")

numeroReal = float(input("\nNúmero real: "))

def arredondarCima(numeroReal):
    return math.ceil(numeroReal)

def arredondarBaixo(numeroReal):
    return math.floor(numeroReal)

def arredondarProximo(numeroReal):
    return round(numeroReal)

print(
    f"\nNúmero arredondado para cima: {arredondarCima(numeroReal)}\n"
    f"Número arredondado para baixo: {arredondarBaixo(numeroReal)}\n"
    f"Número arredondado para o inteiro mais próximo: {arredondarProximo(numeroReal)}\n"
)

# 🔹 Desafio 3 – Nível Difícil

print("\nCalculadora Geométrica")

class FiguraGeometrica():
    
    def areaCirculo(raio):
        return round(math.pi * (math.pow(raio, 2)))

    def areaTriangulo(base, altura):
        return round((base * altura) / 2)
    
    def hipotenusaTrianguloReto(catetoOposto, catetoAdjacente):
        return round(math.sqrt(((math.pow(catetoOposto, 2)) + (math.pow(catetoAdjacente, 2)))))

opcao = int(input(
    "\n1 - Área de Circunferência\
    \n2 - Área de Triângulo\
    \n3 - Hipotenusa de Triângulo Retângulo\n\
    \nQual cálculo deseja realizar? (1, 2 ou 3): "
))

if opcao == 1:
    raio = float(input("\nRaio da circunferência: "))
    print(f"\nÁrea da circunferência: {FiguraGeometrica.areaCirculo(raio)}\n")

elif opcao == 2:
    base = float(input("\nBase do triângulo: "))
    altura = float(input("Altura do triângulo: "))
    print(f"\nÁrea do triângulo: {FiguraGeometrica.areaTriangulo(base, altura)}\n")

elif opcao == 3:
    catetoOposto = float(input("\nCateto oposto: "))
    catetoAdjacente = float(input("Cateto adjacente: "))
    print(f"\nHipotenusa do triângulo reto: {FiguraGeometrica.hipotenusaTrianguloReto(catetoOposto, catetoAdjacente)}\n")

else:
    print("\nOpção inválida.\n")

# 🔹 Desafio 4 – Nível Fácil

print("\nAnimais Simples\n")

class Animal():
    def falar(self):
        return "Som genérico"

class Gato(Animal):
    def falar(self):
        return "Miau!"

class Cachorro(Animal):
    def falar(self):
        return "Au au!"

animais = [Gato(), Cachorro()]

for animal in animais:
    print(animal.falar())

# 🔹 Desafio 5 – Nível Médio

print("\n\nAnimais com Atributos")

class Animal():

    def falar(self):
        return "Som genérico"
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"\nNome: {self.nome}\nIdade: {self.idade}"
    
class Gato(Animal):

    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def falar (self):
        return "Miau!"

class Cachorro(Animal):

    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def falar(self):
        return "Au au!"

animais = [Gato("Mingau", 3), Cachorro("Rex", 5)]

for animal in animais:
    print(animal.apresentar())
    print(animal.falar())

# 🔹 Desafio 6 – Nível Difícil

print ("\n\nZoológico Inteligente")

class Animal:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        return "Som genérico"

    def apresentar(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}"

class Gato(Animal):

    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def falar(self):
        return "Miau!"

class Cachorro(Animal):

    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def falar(self):
        return "Au au!"

class Zoologico:

    def __init__(self):
        self.animais = []

    def adicionarAnimal(self, animal):
        self.animais.append(animal)

    def listarAnimais(self):
        lista = []
        for animal in self.animais:
            info = f"{animal.apresentar()}\n{animal.falar()}"
            lista.append(info)
        return "\n\n".join(lista)

    def filtrarTipos(self, tipo):
        filtrados = [animal for animal in self.animais if isinstance(animal, tipo)]
        return filtrados

zoo = Zoologico()

zoo.adicionarAnimal(Gato("Mingau", 3))
zoo.adicionarAnimal(Cachorro("Rex", 5))
zoo.adicionarAnimal(Gato("Tom", 2))

print("\n• Todos os animais\n")
print(zoo.listarAnimais())

print("\n• Somente os gatos\n")
gatos = zoo.filtrarTipos(Gato)

for gato in gatos:
    print(f"{gato.apresentar()}\n{gato.falar()}\n")


