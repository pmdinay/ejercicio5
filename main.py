""" Cálculo de media,mediana y varianza """

numero1 = float(input("Numero 1: "))
numero2 = float(input("Numero 2: "))
numero3 = float(input("Numero 3: "))

lista = [numero1, numero2, numero3]
def mean(datos):
    return sum(datos) / len(datos)

print("Media de la lista: ", mean(lista))

def median(data):
    data = sorted(data)
    n = len(data)
    if n == 0:
        raise StatisticsError("no median for empty data")
    if n % 2 == 1:
        return data[n // 2]
    else:
        i = n // 2
        return (data[i - 1] + data[i]) / 2

print("Mediana: ", median(lista))

#Necesidad de descargar de Python Packages numpy.
import numpy
varianza = numpy.var(lista)
print("Varianza: ", varianza)


