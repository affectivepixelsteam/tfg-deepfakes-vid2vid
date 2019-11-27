#! /usr/bin/python

from argparse import ArgumentParser
import sys, os, shutil
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

#Array de transformacion: el indice es el valor de source y el valor es el color en el destino
colores =  np.array([
    [0,0,0,255],        # Fondo, negro
    [100,100,100,255],  # Cara, gris
    [255,255,0,255],    # Ceja derecha, amarilla
    [0,100,0,255],      # Ceja izquierda, verde oscuro
    [0, 255 ,255,255],  # Ojo  derecho, azul claro
    [0,0,100,255],      # Ojo izquierdo, azul oscuro
    [255,0,255,255],    # Nariz, violeta
    [255,0,0,255],      # Labio superior, rojo claro
    [0,0,255,255],      # Interior boca, Azul
    [0,255,0,255],      # Labio inferior, verde claro
    [255,255,255,255],  # pelo, blanco
])

parser = ArgumentParser(description='%(prog)s is an ArgumentParser demo')

parser.add_argument('-s', help='imagen que se arreglara')
args = parser.parse_args()
sourceAddr = args.s

def calcDist (pixel, label):
    d=0;
    for i in  range(len(colores[label])-1):
        d+=abs(colores[label][i]-pixel[i])
    return d

def calcColor (pixel):
    label=int(0)
    dmin=int(255*4)
    for i in range(len(colores)):
        if (calcDist(pixel, i) < dmin):
            label=i
            dmin=calcDist(pixel,i)
    return dmin, label


img = Image.open(sourceAddr)
a = np.array(img)
n=0
for i in range(len(a)):
    for j in range(len(a[i])):
        dmin, label = calcColor(a[i][j])
        if (dmin>0):
            a[i][j]=colores[label]
            n+=1

print(str(n)+ 'bits corregidos')
img = Image.fromarray(a);
print('Guardamos'+ sourceAddr)
img.save(sourceAddr)
img.show()