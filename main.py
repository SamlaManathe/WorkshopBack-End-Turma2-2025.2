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

