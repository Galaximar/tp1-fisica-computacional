import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


################# Ejercicio 1#################
h = 0.00001


def dx(cb):
    def dfdx(x):
        return (cb(x+h)-cb(x))/h

    return dfdx


def func(x):
    return x**3


derivada = dx(func)
segundaDervada = dx(dx(func))


def secondDerivate(cb):
    def dfdx(x):
        return (cb(x+h)-2*cb(x)+cb(x-h))/h**2
    return dfdx


dxdx = secondDerivate(func)
print("Función x**3 evaluada en 2:\nSegunda derivada por definición:",
      segundaDervada(2), "\nSegunda derivada dada por el método de aproximación:", dxdx(2))


L = 0.1
n = 10
T0 = 0
T1s = 100
T2s = 0
dx = L/n
alpha = 0.00017
dt = 0.1
x = np.linspace(dx/2, L-dx/2, n)
T = np.ones(n)*T0
dTdt = np.empty(n)
fig, ax = plt.subplots()
ax.set_xlim(0, L)
ax.set_ylim(0, 100)
plt.xlabel('Distancia')
plt.ylabel('Temperatura')
line, = ax.plot(x, T)

# Número de pasos de tiempo
num_steps = int(30 / dt)
seconds = 0
finishCount = False
# Bucle de simulación
for _ in range(num_steps):
    # T_i+1-2T_i+T_i-1=-(T_i-T_i-1)+(T_i+1-T_i)
    for i in range(1, n-1):
        dTdt[i] = alpha * (-(T[i]-T[i-1])/dx**2 + (T[i+1]-T[i])/dx**2)
    dTdt[0] = alpha * (-(T[0]-T1s)/dx**2 + (T[1]-T[0])/dx**2)
    dTdt[n-1] = alpha * (-(T[n-1]-T[n-2])/dx**2 + (T2s-T[n-1])/dx**2)
    prev_T = T[1]
    T += dTdt * dt
    if np.abs(T[1] - prev_T) < 0.02:
        finishCount = True
    else:
        seconds += dt
    line.set_ydata(T)
    plt.pause(0.01)

# Mostrar la gráfica final
plt.show()
# Imprimir el tiempo de estado estacionario
print(f'Tiempo de estado estacionario: {seconds} segundos')
