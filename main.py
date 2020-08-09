# Santiago Naranjo
# 10 de agosto de 2020
import math
#crea una lista de 4 elementos donde los primeros 2 son un numero complejo y los otros 2 otro
comple = [1, 2]
mat = [1, 2, 3, 4]
"""cont = 1
mat = []
resp = []
polares = [0,0]
while cont <= 2:
    print("Ingrese el numero imaginario separado por un coma: ", end="")
    num = input()
    cont += 1
    comple = num.split(",")
    mat = mat + comple"""

#recibe una lista de 4 elementos y los suma segun las propiedades de los numeros complejos
def suma(lista):
    num = [0, 0]
    num[0] = int(lista[0]) + int(lista[2])
    num[1] = int(lista[1]) + int(lista[3])
    return num

#recibe una lista de 4 elementos y los resta segun las propiedades de los numeros complejos
def resta(lista):
    num = [0, 0]
    num[0] = int(lista[0]) - int(lista[2])
    num[1] = int(lista[1]) - int(lista[3])
    return num

#recibe una lista de 4 elementos y los multiplica segun las propiedades de los numeros complejos
def mult(lista):
    num = [0, 0]
    a1 = int(lista[0])
    b1 = int(lista[1])
    a2 = int(lista[2])
    b2 = int(lista[3])
    num[0] = a1 * a2 - b1 * b2
    num[1] = a1 * b2 + a2 * b1
    return num

#recibe una lista de 4 elementos y los divide segun las propiedades de los numeros complejos
def divi(lista):
    num = [0, 0]
    a1 = int(lista[0])
    b1 = int(lista[1])
    a2 = int(lista[2])
    b2 = int(lista[3])
    den = (a2 ** 2) + (b2 ** 2)
    num[0] = round((a1 * a2 + b1 * b2) / den,2)
    num[1] = round((a1 * b2 - a2 * b1) / den,2)
    return num

#recibe una lista de 2 elementos y encuenta su modulo o la raiz de la suma de sus cuadrados
def modu(lista):
    a = int(lista[0])
    b = int(lista[1])
    mod = round(((a**2)+(b**2))**0.5,2)
    return mod

#recibe una lista de 2 elemento e invierte el valor del elemento en la segunda posicion
def conj(lista):
    lista[1] = int(lista[1])*-1
    return lista

#recibe una lista de 2 elementos y encuentra el angulo entre los numeros
def fase(lista):
    a = int(lista[0])
    b = int(lista[1])
    theta = round(math.atan(b/a),2)
    return theta

#recibe una lista con coordenadas polares y las cambia al sistema cartesiano
def pola(lista):
    a = round(int(lista[0])*math.cos(float(lista[1])),2)
    b = round(int(lista[0])*math.sin(float(lista[1])),2)
    carte = [a,b]
    return carte

#recibe una lista con coordenadas cartesianas y las cambia al sistema polar
def car_pol(lista):
    a = modu(lista)
    b = fase(lista)
    coord = [a,b]
    return coord

"""print (suma(mat))
print (resta(mat))
print (mult(mat))
print (divi(mat))
print (modu(comple))
print (car_pol(comple))
print (fase(comple)"""
