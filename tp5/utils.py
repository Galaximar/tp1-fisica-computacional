import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Campo


def E(q, r0, x, y):
    den = np.hypot(x - r0[0], y - r0[1]) ** 3
    return q * (x - r0[0]) / den, q * (y - r0[1]) / den

# Potencial


def V(q, r0, x, y):
    r = np.hypot(x-r0[0], y-r0[1])
    return q/r

# Gráfico del potencial


def show_E(title, charges, Ex, Ey, x, y, withCircle=False):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    if (withCircle):
        # Dibujo del círculo de radio 1 unidad
        circle = Circle((0, 0), 1, fill=False, color='green')
        ax.add_patch(circle)

    color = 2 * np.log(np.hypot(Ex, Ey))
    ax.streamplot(x, y, Ex, Ey, color=color, linewidth=1, cmap=plt.cm.inferno,
                  density=2, arrowstyle='->', arrowsize=1.5)

    # Círculos para las cargas.
    charge_colors = {True: '#aa0000', False: '#0000aa'}
    for q, pos in charges:
        ax.add_artist(Circle(pos, 0.05, color=charge_colors[q > 0]))

    # Grafico E
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    plt.title(title)
    plt.show()


def show_V(x, y, Vp):
    plt.contourf(x, y, Vp, cmap='viridis')
    plt.colorbar()
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.title('Potencial Eléctrico')
    plt.show()
