import numpy as np
import matplotlib.pyplot as plt
from utils import E, V, show_E, show_V


# Puntos de los ejes x e y.
nx, ny = 100, 100
x = np.linspace(-10, 10, nx)  # Ajustar el rango del eje x
y = np.linspace(-2, 2, ny)
X, Y = np.meshgrid(x, y)


nq = 20  # Número total de cargas
charge_spacing = 1.0  # Espaciado entre las cargas en cada fila
half_width = (nq // 2 - 1) * charge_spacing / 2  # Calcula la mitad del ancho

charges = []

# fila superior de cargas negativas
for i in range(nq // 2):
    x_pos = i * charge_spacing - half_width
    charges.append((-1, (x_pos, 1.0)))

# fila inferior de cargas positivas
for i in range(nq // 2):
    x_pos = i * charge_spacing - half_width
    charges.append((1, (x_pos, -1.0)))

Ex, Ey = np.zeros((ny, nx)), np.zeros((ny, nx))
Vp = np.zeros((ny, nx))
for charge in charges:
    ex, ey = E(*charge, x=X, y=Y)
    vp = V(*charge, x=X, y=Y)
    Vp += vp
    Ex += ex
    Ey += ey

show_E(title="Campo eléctrico de distribución paralelas de cargas",
       charges=charges, Ex=Ex, Ey=Ey, x=x, y=y)
show_V(x=x, y=y, Vp=Vp)
