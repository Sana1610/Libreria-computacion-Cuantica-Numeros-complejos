# Santiago Naranjo
# 10 de agosto de 2020 primer entrega
# 24 de agosto de 2020 segunda entrega
# Mejoradas funciones de suma,resta, multiplicacion y division, agragadas funciones con matrices
import math
#crea una lista de 4 elementos donde los primeros 2 son un numero complejo y los otros 2 otro

#recibe dos listas de 2 elementos y los suma segun las propiedades de los numeros complejos
def suma(a,b):
    num = (a[0]+b[0], a[1]+b[1])
    return num

#recibe dos lista de 2 elementos y los resta segun las propiedades de los numeros complejos
def resta(a,b):
    num = (a[0] - b[0], a[1] - b[1])
    return num

#recibe dos lista de 2 elementos y los multiplica segun las propiedades de los numeros complejos
def mult(a,b):
    num = (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0])
    return num

#recibe dos lista de 2 elementos y los divide segun las propiedades de los numeros complejos
def divi(a,b):
    den = (b[0] ** 2) + (b[1] ** 2)
    num = (round((a[0]*b[0] + a[1]*b[1]) / den,2), round((a[0]*b[1] - a[1]*b[0]) / den,2))
    return num

#recibe una lista de 2 elementos y encuenta su modulo o la raiz de la suma de sus cuadrados
def modu(lista):
    a = lista[0]
    b = lista[1]
    mod = round(((a**2)+(b**2))**0.5,2)
    return mod

#recibe una lista de 2 elemento e invierte el valor del elemento en la segunda posicion
def conj(lista):
    res = (lista[0],-lista[1])
    return res

#recibe una lista de 2 elementos y encuentra el angulo entre los numeros
def fase(lista):
    a = lista[0]
    b = lista[1]
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

#recibe n vectores de n elementos y los suma
def sumaVec(a,b):
    resul = []
    for i in range(len(a)):
        resul += [suma(a[i],b[i])]
    return resul

#recibe un vector y encuentra su inverso aditivo
def inverso(a):
    resul = []
    for i in range(len(a)):
        resul += [mult(a[i],(-1,0))]
    return resul

#recibe un vector y un escalar y los multiplica
def EscxVect(a,b):
    resul = []
    for i in range(len(a)):
        resul += [mult(a[i],b)]
    return resul

#recibe dos matrices de tamaños iguales y las suma
def Sum_Ma(a,b):
    n, m = len(a), len(a[0])
    N, M = len(b), len(b[0])
    if n == N and m == M:
        c = [[0 for j in range(m)]for i in range(n)]
        for i in range(n):
            for j in range(m):
                c[i][j] = suma(a[i][j],b[i][j])
    return c

#recibe una matriz y encuentra su inversa aditiva
def Inver_Mat(a):
    n, m = len(a), len(a[0])
    c = [[0 for j in range(m)]for i in range(n)]
    for i in range(n):
        for j in range(m):
            c[i][j] = mult(a[i][j],[-1,0])
    return c

#recibe una matriz y un num escalar y multiplica cada elemento de la matriz por el num escalar
def MatxEsc(a,b):
    n, m = len(a), len(a[0])
    c = [[0 for j in range(m)]for i in range(n)]
    for i in range(n):
        for j in range(m):
            c[i][j] = mult(a[i][j],b)
    return c

#encuentra la transpuesta de una matriz
def Transp(a):
    n, m = len(a), len(a[0])
    c = [[0 for j in range(m)]for i in range(n)]
    for i in range(n):
        for j in range(m):
            c[i][j] = a[j][i]
    return c

#encuentra la conjugada de una matriz
def conj_ma(a):
    n, m = len(a), len(a[0])
    c = [[0 for j in range(m)]for i in range(n)]
    for i in range(n):
        for j in range(m):
            c[i][j] = conj(a[i][j])
    return c

#encuentra la adjunta de una matriz
def adjunta(a):
    c = Transp(conj_ma(a))
    return c

#recibe dos matrices de tamaños compatibles y las multiplica
def Mul_Ma(a,b):
    n, m = len(a), len(a[0])
    N, M = len(b), len(b[0])
    c = [[(0,0) for j in range(m)] for i in range(n)]
    if m == N:
        for i in range(n):
            for j in range(M):
                for k in range(N):
                    p = mult(a[i][k],b[k][j])
                    q = c[i][j]
                    c[i][j] = suma(p,q)
    return c

#calcula la accion de una matriz sobre un vector
def Accion(a,b):
    n, m = len(a), len(a[0])
    B = len(b)
    c = []
    if B == m:
        ceros = [0,0]
        for i in range (n):
            for j in range(m):
                p = mult(a[i][j],b[j])
                ceros = suma(ceros,p)
            c += [ceros]
            ceros = [0,0]
    return c

#calcula el producto interno de dos vectores
def interno(a,b):
    c = (0,0)
    for i in range(len(a)):
        aconj = conj(a[i])
        n = mult(aconj, b[i])
        c = suma(c, n)
    return c

#calcula la norma de un vector
def norma(a):
    e = interno(a,a)
    r = e[0]**0.5
    r = round(r,2)
    return r

#calcula la distancia entre dos vectores
def distancia(a,b):
    f = inverso(b)
    d = sumaVec(a,f)
    c = interno(d,d)
    res = c[0]**0.5
    res = round(res,2)
    return res

#crea una matriz identidad de n*m
def identidad(m,n):
    c = [[[0,0] for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if i == j:
                c[i][j] = ((2/2),0)
    return c

#verifica si una matriz es unitaria
def unitaria(a):
    mat = Mul_Ma(adjunta(a),a)
    iden = identidad(len(a),len(a[0]))
    if mat == iden:
        return True
    else:
        return False

#verifica si una matriz es hermitiana
def hermitiana(a):
    c = adjunta(a)
    if a == c:
        return True
    else:
        return False

#encuentra el producto tensor/cruz de dos matrices/vectores
def tensor(a,b):
    res = []
    m, n = 0, 0
    while (m<((len(a)-1)**2)):
        r1 = a[m]
        r2 = b[n]
        aux = []
        for i in r1:
            for j in r2:
                aux += [mult(i,j)]
        m += 1
        r2 = b[n]
        res += [aux]
        aux = []
        for i in r1:
            for j in r2:
                aux += [mult(i,j)]
        m += 1
        n -= 1
        res += [aux]
    return res
