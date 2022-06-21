""" Codigo de Jose Manuel Pedro Mendez, 315073120 correspondiente a la practica 02 Busquedas"""
import random
import sys
import re

def entradaValida():
    """ Funcion que nos permite obtener una entrada valida para la ejecucion de neustro algoritmo """
    args = sys.argv
    if len(args)>2:
        raise ValueError(f"Entrada invalida, python3 solo puede tener 2 parametros, no {len(args)} :D")
    else:
        num_format = re.compile(r'^\-?[1-9][0-9]*$')
        num_pos = args[1]
        num = re.match(num_format, num_pos )
        if num:
            numF = int(num_pos)

            if numF<0: 
                raise ValueError("El segundo parametro no puede ser negativo")
            else:
                print(f"Trabajareomos con m={numF}, es decir, con un arreglo de {numF} elementos.")
                return numF
        else:
            raise ValueError(f"El segundo parametro {num_pos} no representa un entero POSITIVO")

#Obtenemos una entrada valida
m= entradaValida()

array = []

def arregloRandom(n):
	
    """ Funcion que nos permite obtener un arreglo que cumpla nuestra primera precondicion"""
    base = random.randint(1, 100)
    arregloB = [base] #Base a partir de la que generaremos nuestro arreglo
    while n > len(arregloB):
        base = base + random.choice([-1, 0, 1]) 
        # Esto es para respetar la primera condición, entre cada par ordenado no podemos
        # encontrar diferencias mayores a 1.
        arregloB.append(base)
    return arregloB

secondCondition = False # Es decir, si arregloB[0] = X y arregloB[(len(arregloB)-1)]=Y ent X<Y
while not(secondCondition):
    array = arregloRandom(m)
    x = array[0]
    y = array[len(array) - 1]
    if (x<y):
        secondCondition = True
# Recordemos que z, el elemento buscado debe cumplir que X<z<Y

z = random.randint(array[0], array[len(array) - 1])

print("Elemento a buscar: ",z)
print("El arreglo donde buscaremos es: ",array)

def busquedaBinaria(z, array):
    minA = 0
    maxA = len(array)-1
    while(minA<=maxA):
        mitad=(maxA+minA)//2
        if array[mitad] == z:
            return mitad
        elif (array[mitad] < z):
            minA=mitad+1
        else:
            maxA=mitad-1
    return -1 #sin exito, aunque esto no llegará a pasar

indice = busquedaBinaria(z, array)
print(f"El indice del elemento {z} en el arreglo es: {indice}")