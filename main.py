import math

# 🔹 Desafio 1 – Nível Fácil

numero = int(input("\nNúmero: "))

def raizQuadrada(numero):
    
    raiz = math.sqrt(numero)

    return raiz

print(f"\nRaiz: {raizQuadrada(numero)}\n")

# 🔹 Desafio 2 – Nível Médio

numeroReal = float(input("\nNúmero real: "))

def arredondarCima(numeroReal):

    paraCima = math.ceil(numeroReal)
    return paraCima

def arredondarBaixo(numeroReal):

    paraBaixo = math.floor(numeroReal)
    return paraBaixo

def arredondarProximo(numeroReal):

    intProximo = round(numeroReal)
    return intProximo

print (f"\nNúmero arredondado para cima (teto): {arredondarCima(numeroReal)}")
print (f"Número arredondado para baixo: {arredondarBaixo(numeroReal)}")
print (f"Número arredondado para o inteiro mais próximo: {arredondarProximo(numeroReal)}\n")

# 🔹 Desafio 3 – Nível Difícil

class FiguraGeometrica():

    def areaCirculo(raio):

        area = math.pi * (math.pow(raio, 2))
        return area

    def areaTriangulo(base, altura):

        area = (base * altura) / 2
        return area
    
    def hipotenusaTrianguloReto(catetoOposto, catetoAdjacente):

        hipotenusa = math.sqrt((math.pow(catetoOposto, 2)) + (math.pow(catetoAdjacente, 2)))
        return hipotenusa

opcao = int(input("\nQual cálculo deseja realizar? (1-areaCirculo, 2-areaTriangulo, 3-hipotenusa): "))

if opcao == 1:

    raio = float(input("\nRaio da circunferência: "))
    print (f"\nÁrea da circunferência: {FiguraGeometrica.areaCirculo(raio)}\n")

elif opcao == 2:

    base = float(input("\nBase do triângulo: "))
    altura = float(input("Altura do triângulo: "))
    print (f"\nÁrea do triângulo: {FiguraGeometrica.areaTriangulo(base, altura)}\n")

elif opcao == 3:

    catetoOposto = float(input("\nCateto oposto do triângulo retângulo: "))
    catetoAdjacente = float(input("Cateto adjacente do triângulo retângulo: "))
    print (f"\nHipotenusa do triângulo retângulo: {FiguraGeometrica.hipotenusaTrianguloReto(catetoOposto, catetoAdjacente)}\n")

else:

    print ("\nOpção inválida.")

# 🔹 Desafio 4 – Nível Fácil

class Animal():

    def falar (self):

        return "Som genérico"

class Gato(Animal):

    def falar (self):

        return "Miau!"

class Cachorro(Animal):

    def falar (self):

        return "Au au!"

animais = [Gato(), Cachorro()]

for animal in animais:

    print(animal.falar())

# 🔹 Desafio 5 – Nível Médio

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

        return "Miau!\n"

class Cachorro(Animal):

    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def falar (self):

        return "Au au!\n"

animais = [Gato("Mingau", 3), Cachorro("Rex", 5)]

for animal in animais:

    print(animal.apresentar())
    print(animal.falar())