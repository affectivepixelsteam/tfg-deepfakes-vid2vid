#! /usr/bin/python
from argparse import ArgumentParser
import sys, os, shutil
import numpy as np
from PIL import Image

parser = ArgumentParser(description='%(prog)s is an ArgumentParser demo')

parser.add_argument('-s', help='imagen que se transformará')
parser.add_argument('-f',default='', help='dirección destino')
parser.add_argument('-n', help='dirección destino')
parser.add_argument('-r', default='False', help='Para borrar la foto original', action='store_true')
parser.add_argument('-m', default='False', help='Para mostrar la imagen', action='store_true')
parser.add_argument('-p', default='False', help='Preparar par al hace test_netP crear las mascaras', action='store_true')

args = parser.parse_args()
sourceAddr=args.s
destinyAdd=args.f
nArg = int(args.n) * 256
if (destinyAdd==''):
    n = sourceAddr.find('.')
    destinyAdd = sourceAddr[0:n]+'.png'

img = Image.open(sourceAddr).convert('RGB')
a = np.array(img)

x, y, n = len(a[0]), len(a), 0
while(x>256 and y>256):
   n+=256
   x-=256
   y-=256

y_i, y_f, x_i, x_f = int((y+nArg)/2),int((y-nArg)/2+n),int((x+nArg)/2),int((x-nArg)/2+n)
b=a[y_i:y_f,x_i:x_f,:]

img2 = Image.fromarray(b)
img2 = img2.resize((256,256))

img2.save(destinyAdd)
print ('Guardamos la foto '+ destinyAdd)
if (args.r == True):
    os.remove(sourceAddr)
    print('Borramos la foto '+ sourceAddr)
if (args.m==True):
    img2.show()

if(args.p==True):
    n1=destinyAdd.find('_img')
    shutil.copy(destinyAdd[0:n1]+'_label/173.png',
                destinyAdd[0:n1]+'_label/'+destinyAdd[n1+5:len(destinyAdd)])
    img2.save(destinyAdd[0:n1]+'2'+destinyAdd[n1:len(destinyAdd)])

    print('Generamos la mascara falsa '+ destinyAdd[0:n1]+'_label/'+destinyAdd[n1+5:len(destinyAdd)])
    print(destinyAdd[0:n1]+'2'+destinyAdd[n1:len(destinyAdd)])
exit()