import numpy as np

import matplotlib.pyplot as plt

from utils import E, V, show_E, show_V

# count=1 -> dipolo, count=2 quadrupolo


def campo(count=1):

    nx, ny = 64, 64

    x = np.linspace(-2, 2, nx)

    y = np.linspace(-2, 2, ny)

    X, Y = np.meshgrid(x, y)

    # Multipolo con nq cargas
    nq = 2**int(count)

    charges = []

    for i in range(nq):
        q = (i % 2 * 2 - 1)

        charges.append((q, (np.cos(2*np.pi*i/nq), np.sin(2*np.pi*i/nq))))

    Ex, Ey = np.zeros((ny, nx)), np.zeros((ny, nx))
    Vp = np.zeros((ny, nx))
    for charge in charges:
        ex, ey = E(*charge, x=X, y=Y)
        vp = V(*charge, x=X, y=Y)
        Vp += vp
        Ex += ex
        Ey += ey

    show_E(title="Campo eléctrico del dipolo" if count ==
           1 else "Campo eléctrico del quadrupolo", charges=charges, Ex=Ex, Ey=Ey, x=x, y=y)
    show_V(x=x, y=y, Vp=Vp)


campo(1)
campo(2)
