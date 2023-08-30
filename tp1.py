import matplotlib.pyplot as plt
import math as m

# Ejercicio 1


def getTypeOfTriangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "No es un triángulo válido"
    if a**2+b**2 == c**2:
        return 'rectangulo'
    if a**2+b**2 > c**2:
        return 'acutangulo'
    if a**2+b**2 < c**2:
        return 'obtusangulo'


print("Lados 3,4,5:", getTypeOfTriangle(3, 4, 5))
print("Lados 5,3,5:", getTypeOfTriangle(5, 3, 5))
print("Lados 8,15,17:", getTypeOfTriangle(8, 15, 17))

# Ejercicio 2


def getTriplasPitagorica(m, n=2):
    triplas = []

    def eq(i, j, n):
        return (i**n+j**n)**(1/n)
    countOfTriplas = 0
    for i in range(1, m+1):
        for j in range(1, m+1):
            k = eq(i, j, n)
            if k <= m and int(k) == k:
                countOfTriplas += 1
                triplas.append(dict(i=i, j=j, k=eq(i, j, n)))
    print(f"Cantidad de triplas con exponente {n}: {countOfTriplas}")
    return triplas


getTriplasPitagorica(100, 1)

print(f"2_a {getTriplasPitagorica(100, 2)}")
getTriplasPitagorica(100, 3)
getTriplasPitagorica(100, 4)
getTriplasPitagorica(100, 40)

# Ejercicio 3


def serie_fourier(x, a, b, N=50):
    s = a[0]/2
    for n in range(1, N+1):
        s += a[n] * m.cos(n*x) + b[n] * m.sin(n*x)
    return s


def buildList(cb, N=50):
    return [cb(i) for i in range(0, N+1)]


def b_serrucho(i):
    return 0 if i == 0 else 2*(-1)**(i+1)/i/m.pi


def a_serrucho(i):
    return 0


def f(x):
    return 2*((x+1/2) - m.floor(x+1/2)) - 1


xmin = - 2
xmax = 2
nx = 1000


def compareFunctions(N=50):

    xs = [xmin + i * (xmax-xmin) / nx for i in range(nx+1)]
    ys = [serie_fourier(x*2*m.pi, buildList(a_serrucho, N),
                        buildList(b_serrucho, N), N) for x in xs]
    yss = [f(x) for x in xs]
    plt.plot(xs, ys, color='red', label='Serie de fourier')
    plt.plot(xs, yss, color="blue", label='Función serrucho')
    plt.title(
        f"Compración de funciones con {N} iteraciones")
    plt.legend()
    plt.show()


compareFunctions(6)
