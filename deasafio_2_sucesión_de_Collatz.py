n = int(input('Ingrese el valor de "n": '))

original_n = n
sucesion = str(n)
suma_n = n
mayor = 0
bandera1= True
orbita = 1



while n != 1:


    if n % 2 == 0:
        n = n / 2
        if n % 1 == 0:
            n = int(n)

    else:
        n = (n * 3) + 1

    sucesion += ', ' + str(n)
    orbita += 1
    suma_n += n

    if n > mayor:
        mayor = n

promedio = suma_n / orbita

print('n =', original_n)
print('Orbita de n =' , original_n , '(valores calculados incluyendo al', original_n ,'y al 1):', sucesion)
print('Longitud de la órbita (cantidad de valores calculados hasta llegar al 1):', orbita)
print('Promedio de todos los valores de la órbita:', promedio)
print('Mayor de los números en esa órbita:', mayor)
