import numpy as np
#forma 1 desde lista
lista = [1,2,3,4]
arr = np.array(lista)
#print(arr)
#forma 2
arr2 = np.array ([5,6,7,8])
#print(arr2)

#funciones con arreglos
arreglo=np.array([5,6,7,8,9,10,11,12])
##print(arreglo.ndim)
##print(arreglo [4:7]) #muestra intervalo de numeros
##print (arreglo[0:7:3])# muestsa entre intervalo
##print(arreglo[::3])

c = [i for i in range(0,101)]
print(c[0:101:2]) #muestra numeros pares de 2 en 2 desde el 0 hasta el 100
print(c[1:100:2]) #muestra numeros impares de 2 en 2 desde el 1 hasta el 99
