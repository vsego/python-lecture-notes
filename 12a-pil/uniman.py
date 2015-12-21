#!/usr/bin/env python3

"""
Create an animated GIF of a rotating logo of The University of Manchester.
"""

from PIL import Image
import numpy as np
from math import cos, sin, pi

sides = 4
dh = 30
steps = 11
fname = "uniman.png"

def find_coeffs(pa, pb):
    """
    Return the coefficients matrix.

    `pb` is the four vertices in the current plane, and
    `pa` contains four vertices in the resulting plane.

    Taken from [here](http://stackoverflow.com/a/14178717/1667018).
    """
    matrix = []
    for p1, p2 in zip(pa, pb):
        matrix.append([p1[0], p1[1], 1, 0, 0, 0, -p2[0]*p1[0], -p2[0]*p1[1]])
        matrix.append([0, 0, 0, p1[0], p1[1], 1, -p2[1]*p1[0], -p2[1]*p1[1]])

    A = np.matrix(matrix, dtype=np.float)
    B = np.array(pb).reshape(8)

    res = np.dot(np.linalg.inv(A.T * A) * A.T, B)
    return np.array(res).reshape(8)

logo = Image.open(fname)
width, height = logo.size

phi = 0
r = width/2
shift = 2*pi/sides

for idx,phi in enumerate(np.arange(0, pi/2, pi/2/steps)):
    print("Creating image #{}...".format(idx+1))
    im = Image.new("RGB", (width, height), "white")
    for alpha in np.arange(3/4*pi, 7/4*pi, shift):
        (x0, y0) = (r * (1+cos(alpha+phi)), dh * (1+sin(alpha+phi)))
        (x1, y1) = (r * (1+cos(alpha+phi+1.01*shift)), dh * (1+sin(alpha+phi+1.01*shift)))
        coeffs = find_coeffs(
            [(x0, y0), (x1, y1), (x1, height-y1), (x0, height-y0)],
            [(0, 0), (width, 0), (width, height), (0, height)]
        )
        logo_tr = logo.transform((width, height), Image.PERSPECTIVE, coeffs, Image.BICUBIC)
        im.paste(logo_tr, (0, 0), logo_tr)
    im.save("img{:05d}.png".format(idx))

