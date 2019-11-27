#! /usr/bin/python

from argparse import ArgumentParser
import sys, os, shutil
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


#Array de transformacion: el indice es el valor de source y el valor es el color en el destino
colores =  [
    [0,0,0,255],        # Fondo, negro
    [100,100,100,255],  # Cara, gris
    [255,255,0,255],    # Ceja derecha, amarilla
    [0,100,0,255],      # Ceja izquierda, verde oscuro
    [0, 255 ,255,255],   # Ojo  derecho, azul claro
    [0,0,100,255],      # Ojo izquierdo, azul oscuro
    [255,0,255,255],    # Nariz, violeta
    [255,0,0,255],      # Labio superior, rojo claro
    [0,0,255,255],      # Interior boca, Azul
    [0,255,0,255],      #Labio inferior, verde claro
    [255,255,255,255],    #pelo, blanco
]


parser = ArgumentParser(description='%(prog)s is an ArgumentParser demo')

parser.add_argument('-s', help='imagen que se transformará')
parser.add_argument('-f', help='dirección destino')
parser.add_argument('-t', default='False', help='si transformamos o destransformamos', action='store_true')
parser.add_argument('-n', default='', help='nombre del experimento')
parser.add_argument('-r', default='False', help='para borrar una transformacion', action='store_true')

#Cargamos los parametros
args = parser.parse_args()
sourceAddr = args.s
destinyAddr = args.f
name = args.n

if (args.r==True):
    n = sourceAddr.find('_t.png')
    if (n!=-1):
        os.remove(sourceAddr)
        print('borrado '+ sourceAddr)
    else:
        n = sourceAddr.find('.png')
        os.remove(sourceAddr[0:n]+'_t.png')
        print('borrado '+ sourceAddr[0:n]+'_t.png')
elif (args.t==True):
    #Calculamos la direccion destino y creamos las fotos nuevas si se necesita
    if (destinyAddr==None):
        n = sourceAddr.find(".png")
        if (n != -1):
            if (name!=''):
                print(name)
                print(sourceAddr)
                destinyAddr = sourceAddr[0:n] + '' + name + "_t.png"
                i = sourceAddr.find("/edit2_label/")
                shutil.copy(sourceAddr[0:i+1] + 'edit2_img/'+ sourceAddr[i+13:n]+'.png',
                            sourceAddr[0:i+1] + 'edit2_img/'+ sourceAddr[i+13:n]+''+name+'.png')
                shutil.copy(sourceAddr[0:i + 1] + 'edit_label/' + sourceAddr[i + 13:n] + '.png',
                            sourceAddr[0:i + 1] + 'edit_label/' + sourceAddr[i + 13:n] + '' + name + '.png')
                shutil.copy(sourceAddr[0:i + 1] + 'edit_img/' + sourceAddr[i + 12:n] + '.png',
                            sourceAddr[0:i + 1] + 'edit_img/' + sourceAddr[i + 12:n] + '' + name + '.png')
                print('creada el conjunto '+ sourceAddr[i+12:n]+''+name+'.png')
            else:
                destinyAddr = sourceAddr[0:n] + '_t.png'
        else:
            print("not valid source")
            exit()


    # Inicializamos la imagen
    img = Image.open(sourceAddr).convert('RGBA')
    a = np.array(img)
    b = a
    #Modificamos la imagen
    for j in range(len(a[0,:,0])):
        for k in range(len(a[:,j,0])):
            b[k,j,:]=colores[a[k,j,0]]
    img2 = Image.fromarray(b, 'RGBA')
    #Guardamos la imagen
    img2.show()
    print(destinyAddr)
    img2.save(destinyAddr)

else:
    #Caluclamos la direccion destino
    if (destinyAddr==None):
        n=sourceAddr.find(".png")
        if (n!=-1):
            if(name!=''):
                destinyAddr = sourceAddr[0:n]+''+name+"_t.png"
                sourceAddr = sourceAddr[0:n]+''+name+'.png'
            else:
                destinyAddr = sourceAddr[0:n]+'_t.png'
        else:
            print("not valid source")
            exit()

    #Inicializamos la imagen
    img = Image.open(destinyAddr)
    a = np.array(img)
    b = a[:, :, 0]
    #Modificamos la imagen
    for j in range(len(a[0,:,0])):
        for k in range(len(a[:,j,0])):
            for u in range(len(colores)):
                if ((a[k][j]==colores[u]).all()):
                    b[k,j]=u
    print(b.shape)
    img2 = Image.fromarray(b)
    #array_i = np.save("./datasets/helen_align/edit_label/b.npy", b)
    print('Borramos la imagen ' + destinyAddr)
    os.remove(destinyAddr)
    #Guardamos la imagen
    print('Guardamos la imagen ' + sourceAddr)
    img2.save(sourceAddr)

