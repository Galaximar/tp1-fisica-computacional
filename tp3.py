import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Parámetros del sistema
m = 1.0  # Masa
omega0 = 2.0  # Frecuencia angular natural

# Amplitud de la fuerza externa y su frecuencia angular
F0 = 1.0

# Definición de la función que representa el sistema de EDOs
def system(zeta):

    def eq(y, t):
        x, v = y  # Desempaqueta las variables de estado
        return  [v, (-2 * zeta * omega0 * v - omega0**2 * x + F0 * np.sin(omega0 * t)/m)]
    
    return eq

# Condiciones iniciales
x0 = 1.0  # Posición inicial
v0 = 2.0  # Velocidad inicial
initialValues = [x0, v0]  # Condiciones iniciales como un array

# Tiempo de integración
t = np.linspace(0, 50, 1000)  # Desde 0 hasta 10 segundos, 1000 puntos

solSubCrt = odeint(system(0.1), initialValues, t)
solCrt=odeint(system(1), initialValues, t)
solSobreCrt=odeint(system(10), initialValues, t) 

def calculate_average_energy(x,w0):
    A = np.max(np.abs(x))  # Amplitud de la solución estacionaria
    return 0.5 * m * A**2 * w0**2


fig, ax1 = plt.subplots()




def showPlt(sol,label,ax,color):
    x = sol[:, 0]
    ax.plot(t, x, color,label=label)
    ax.set_xlabel('Tiempo')
    ax.set_ylabel('Posición',)
    ax.tick_params('y')
    plt.legend()
    plt.grid(True)



    
showPlt(solSubCrt,"Sub crítica",ax1,"red")
showPlt(solCrt,"Crítica",ax1,"blue")
showPlt(solSobreCrt,"Sobre crítica",ax1,"green")
plt.title("Posición en función del tiempo con fuerza restauradora")
plt.show()
w0Energy=np.linspace(0, 50, 1000)
energyProm=[calculate_average_energy(solCrt[:, 0],i) for i in w0Energy]
plt.plot(w0Energy,energyProm)
plt.xlabel('Frecuencia')
plt.ylabel('Energia promedio')
plt.title("Energía promedio en estado estacionario")


# Definición de la función que representa el sistema de EDOs sin fuerza restauradora
def systemWithoutF(zeta):
    def eq(y, t):
        x, v = y  # Desempaqueta las variables de estado
        return  [v, (-2 * zeta * omega0 * v - omega0**2 * x )]
    
    return eq

fig2, ax2 = plt.subplots()
solSubCrtWithoutF = odeint(systemWithoutF(0.1), initialValues, t)
solCrtWithoutF=odeint(systemWithoutF(1), initialValues, t)
solSobreCrtWithoutF=odeint(systemWithoutF(10), initialValues, t) 

showPlt(solSubCrtWithoutF,"Sub crítica",ax2,"red")
showPlt(solCrtWithoutF,"Crítica",ax2,"blue")
showPlt(solSobreCrtWithoutF,"Sobre crítica",ax2,"green")
plt.title("Posición en función del tiempo sin fuerza restauradora")
plt.show()

## La energía promedio aumenta en función de la frecuencia