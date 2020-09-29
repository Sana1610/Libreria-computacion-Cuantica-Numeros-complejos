import main
from matplotlib import pyplot

def DinamicaDeterminista(click,matriz,Rvecto):
    res = main.Accion(matriz, Rvecto)
    if click == 1:
        return res
    else:
        for clicks in range(click-1):
            resp = main.Accion(matriz,res)
            res = resp
        return res

def dibujo(vec):
    res = []
    pos = []
    for i in range(len(vec)):
        res.append(vec[i][0])
        pos.append(i)
    pyplot.title("Probabilidad experimento de rendija cuantica")
    pyplot.bar(pos, height=res, color='blue', width=0.5)
    pyplot.show()

def DinamicaDeterministaProbabilidad(rendijas,objetivo,probabilidades):
    vecIni = [(1, 0)]
    temp = rendijas + 1
    frac2 = 1 / rendijas
    divisiones = objetivo // 2
    tamaño = calcularTamaño(rendijas,divisiones) + rendijas
    matriz = crarGrafo(tamaño + 1, temp)
    matriz = llenarUno(matriz,rendijas,tamaño,frac2)
    matriz = llenarDos(matriz,rendijas,objetivo,probabilidades,divisiones)
    for i in range(tamaño):
        vecIni.append((0, 0))
    res = DinamicaDeterminista(2,matriz,vecIni)
    return res

def calcularTamaño(rendijas,divisiones):
    res = divisiones
    for i in range(rendijas):
        res += divisiones
    return res + rendijas

def crarGrafo(tamaño,temp):
    matriz = []
    for i in range(tamaño):
        row = []
        for j in range(tamaño):
            if i==temp and j==temp:
                row.append((1,0))
                temp += 1
            else:
                row.append((0,0))
        matriz.append(row)
    return matriz

def llenarUno(m,x,tam,frac2):
    for j in range(1, tam + 1):
        if j <= x:
            m[j][0] = (frac2, 0)
    return m

def llenarDos(m,r,o,p,div):
    temp = 0
    k = o
    vec = 0
    while temp != r:
        temp += 1
        i = 0
        while i != o:
            m[k][temp] = p[vec]
            vec += 1
            i += 1
            k += 1
        k -= div
    return m



