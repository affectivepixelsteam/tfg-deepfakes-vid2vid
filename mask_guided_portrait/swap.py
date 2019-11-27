#! /usr/bin/python


from argparse import ArgumentParser
import sys, os, shutil

parser = ArgumentParser(description='%(prog)s is an ArgumentParser demo')

parser.add_argument('-s', help='imagen y label source')
parser.add_argument('-t', help='imagen y label target')
parser.add_argument('-n',default='', help='nuevo nombre')
parser.add_argument('-m', default='False', help='si queremos que el nombre sera m+source+target', action='store_true')
#parser.add_argument('-n', default='', help='nombre del experimento')
#parser.add_argument('-r', default='False', help='para borrar una transformacion', action='store_true')

#Cargamos los parametros

args = parser.parse_args()
sourceAddr=args.s
targetAddr=args.t
newAddr=args.n

if newAddr == '' :
    ns=sourceAddr.find('.png')
    nt=targetAddr.find('.png')
    if (ns!=-1 and nt !=-1):
        newAddr = sourceAddr[0:ns] + 'to' + targetAddr[0:nt]+'.png'
    else:
        newAddr=sourceAddr+'to'+targetAddr

if args.m ==True:
    newAddr='m'+newAddr

path = 'datasets/helen_align/'
shutil.copy(path+'edit_label/'+sourceAddr,
            path+'edit_label/'+newAddr)

shutil.copy(path+'edit_img/'+sourceAddr,
            path+'edit_img/'+newAddr)
shutil.copy(path+'edit_label/'+targetAddr,
            path+'edit2_label/'+newAddr)
shutil.copy(path+'edit_img/'+targetAddr,
            path+'edit2_img/'+newAddr)

print('creamos '+ path+'edit_label/'+newAddr)
print('creamos '+ path+'edit2_label/'+newAddr)
print('creamos '+ path+'edit_img/'+newAddr)
print('creamos '+ path+'edit2_img/'+newAddr)