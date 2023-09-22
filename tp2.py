import numpy as np
import math
import matplotlib.pyplot as plt

#############
## Ejercicio 1

x = np.linspace(-3 * np.pi, 3 * np.pi, 1000)
f_x = np.cos(x**2)
plt.figure(figsize=(6, 6))
plt.plot(x, f_x, label='f(x) = cos(x^2)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico de f(x) = cos(x^2) en [-3π, 3π]')
plt.grid(True)
plt.legend()
plt.show()
#############
x = np.linspace(-1, 1, 1000)

if (0 in x):
    x = x[x != 0]
    
f_x = x*np.sin(1/x)
plt.plot(x, f_x, label='f(x) = x * sin(1/x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico de f(x) = x * sin(1/x) en [-2, 2]')
plt.grid(True)
plt.legend()
plt.show()
#############


def bessel_first_kind(order, x):
    if order < 0:
        raise ValueError("El orden de la función de Bessel debe ser un número entero no negativo.")
    
    result = 0.0
    for k in range(0, 100):
        term = ((-1)**k) / (math.factorial(k) * math.factorial(order + k))
        term *= (x / 2)**(order + 2*k)
        result += term
    
    return result

x = np.linspace(0, 10, 500)

orders = [1, 2, 3, 4, 5]

for order in orders:
    y = [bessel_first_kind(order, xi) for xi in x]
    plt.plot(x, y, label=f'J{order}(x)')

plt.xlabel('x')
plt.ylabel('J_n(x)')
plt.legend()
plt.title('Funciones de Bessel de primer tipo')
plt.grid(True)
plt.show()
##############################

## Ejercicio 2


def mu(t):
    return np.exp(1j*t) + 0.5 * np.exp(6j*t) + (1j/3) * np.exp(-14j*t)
t_values = np.linspace(0, 2*np.pi, 1000)

R_mu = np.real(mu(t_values))
I_mu = np.imag(mu(t_values))

plt.figure(figsize=(6, 6))
plt.plot(R_mu, I_mu, label='Curva paramétrica')
plt.xlabel('Rμ(t) (Parte Real)')
plt.ylabel('Iμ(t) (Parte Imaginaria)')
plt.title('Curva paramétrica (Rμ(t), Iμ(t))')
plt.legend()
plt.grid(True)
plt.show()

##############################

## Ejercicio 3

# Parámetros para la curva de Lissajous
a = np.pi
b = 3
delta = np.pi   # Fase en radianes
A = 1.0  # Amplitud en dirección x
B = 1.0  # Amplitud en dirección y

def x(t):
    return A * np.sin(a * t + delta)

def y(t):
    return B * np.sin(b * t)

def calcular_area(t):
    # Número de puntos para la aproximación del área
    num_puntos = 1000
    dt = t / num_puntos

    # Calcular las coordenadas en los puntos
    tiempos = np.linspace(0, t, num_puntos)
    x_vals = x(tiempos)
    y_vals = y(tiempos)

    # Calcular el área de cada segmento y sumarlas
    area_total = 0.0
    for i in range(num_puntos - 1):
        area_total += 0.5 * (x_vals[i] + x_vals[i + 1]) * (y_vals[i + 1] - y_vals[i])

    return area_total

tiempos = np.linspace(0, 50, 500) 
areas = [calcular_area(t) for t in tiempos]
plt.figure(figsize=(6, 6))
plt.plot(tiempos, areas)
plt.ylabel('Área cubierta')
plt.xlabel('Tiempo')
plt.title('Área cubierta por la curva de Lissajous en función del tiempo')
plt.figure(figsize=(6, 6))
plt.plot(x(tiempos),y(tiempos),color="red")
plt.xlabel('Tiempo')

plt.grid(True)
plt.show()