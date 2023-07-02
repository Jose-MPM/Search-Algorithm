# Search Algorithm (Binary Search) :shipit:

### Problem ⁉️ 
* Algoritmo de busqueda para resolver el siguiente problema:
    - Dado un arreglo A[0..n − 1] de n enteros, no necesariamente distintos, tal que ∀i, 0 ≤ i ≤ n − 1, se tiene que |A[i] − A[i + 1]| ≤ 1. Además, si A[0] = x y A[n − 1] = y entonces x < y. Diseñar un algoritmo de búsqueda, de tiempo logarı́tmico, que localice al ı́ndice j tal que a[j] = z, para un valor dado de z, con x ≤ z ≤ y. 

### Solution 👍 ☑️
* Por nuestras condiciones del ejercicio podemos establecer lo siguiente como precondiciones:
    1. ∀i tq 0<=i<=(n-1) |A[i]-A[i+1]| <= 1, es decir, para cada par ordenado no podemos encontrar diferencias mayores a 1.
    2. Si A[0]=X y A[n-1]=Y ent X<Y

* Primero nos encargamos de crear un arreglo que cumpla nuestras precondiciones, para después poder aplicar la misma logica empleada en busqueda binaria y como X<=Z<=Y entonces siempre encontraremos el indice de Z.

#### Input

* El programa recibe como entrada un entero n que es el número de elementos que debe tener el arreglo de números, los cuales son generados aleatoriamente.

#### Output

* El programa imprime en pantalla el arreglo generado y un elemento z escogido de manera aleatoria, junto a la posición de este elemento en el arreglo, o bien imprime −1 si no se encontró.

## Solution in Python 3.8.10 ⌨️
* Solo hay que ejecutar en la carpeta src:

```
$ python3 BynaryS.py k
```

* Donde k es un numero entero positivo, el cual indicara el tamaño de nuestro arreglo(el numero de elementos).


---
🥇⌨️ con ❤️ por [Jose-MPM](https://github.com/Jose-MPM) 😊🔧
