import numpy as np
import matplotlib.pyplot as plt
from utils import E, V, show_E, show_V


def aleatorias(random=True, seed=1):

    # Puntos de los ejes x e y.
    nx, ny = 64, 64
    x = np.linspace(-2, 2, nx)
    y = np.linspace(-2, 2, ny)
    X, Y = np.meshgrid(x, y)

    # Crear una distribución aleatoria de cargas dentro de un círculo
    nq = 10  # Número de cargas
    charges = []
    np.random.seed(seed)  # Seed para reproducibilidad
    for i in range(nq):
        q = 0
        if (random):
            q = np.random.choice([-1, 1])  # Carga positiva o negativa
        else:
            q = 1 if i <= 4 else -1
        angle = np.random.uniform(0, 2 * np.pi)  # Ángulo aleatorio
        radius = np.random.uniform(0, 1)  # Radio aleatorio dentro del círculo
        x_pos = radius * np.cos(angle)
        y_pos = radius * np.sin(angle)
        charges.append((q, (x_pos, y_pos)))

    # Vector de campo eléctrico como componentes separadas (Ex, Ey)
    Ex, Ey = np.zeros((ny, nx)), np.zeros((ny, nx))
    Vp = np.zeros((ny, nx))
    for charge in charges:
        ex, ey = E(*charge, x=X, y=Y)
        vp = V(*charge, x=X, y=Y)
        Vp += vp
        Ex += ex
        Ey += ey

    show_E(title="Distribución aleatoria de cargas no neutras" if random else "Distribución aleatorias de cargas neutras",
           charges=charges, Ex=Ex, Ey=Ey, x=x, y=y, withCircle=True)
    show_V(x=x, y=y, Vp=Vp)


aleatorias(seed=10)
aleatorias(False)
