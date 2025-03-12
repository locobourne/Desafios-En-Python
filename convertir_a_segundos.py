dato_entrada= int(input("Ingrese la cantidad de segundos que desea convertir:\n"))

#-----------------------------------------------------------------------------------------------------------------------
 # A la variable "minutos" la tomamos en cuenta como calculo de intermedio para poder calcular las horas enteras y los segundos enteros.
 # Para esto nesecitamos una division entera entre "dato_entrada" y 60, por eso utilizamos //60.
#-----------------------------------------------------------------------------------------------------------------------

minutos = dato_entrada // 60

#-----------------------------------------------------------------------------------------------------------------------
 # El resto de la division entera entre "dato_entrada" y 60 nos da como resultado los segundos enteros, por eso utilizamos %60.
#-----------------------------------------------------------------------------------------------------------------------

segundos_enteros = dato_entrada % 60

#-----------------------------------------------------------------------------------------------------------------------
 # Como dijimos anteriormente la variable "minutos" nos va a ayudar a sacar las horas y segundos enteros.
 # La division entera entre la variable "minutos" y 60 nos dara como resultado las horas enteras, por eso utilizamos //60.
 # El resto de la division entera entre "minutos" y 60 nos da como resultado los minutos enteros, por eso utilizamos %60.
#-----------------------------------------------------------------------------------------------------------------------

horas_enteras = minutos // 60

minutos_enteros= minutos % 60

#-----------------------------------------------------------------------------------------------------------------------
 # Ahora para cumplir con el enunciado nesecitamos que al pasarse de 24 horas de como resultado "Excedido".
 # Esto quiere decir que al tener como entrada 89999 nos dara como resultado => Horas: 24 Minutos: 59 Segundos: 59 por lo tanto no se excede.
 # Pero si damos como entrada 90000, nos exedemos de las 24 horas, por lo tanto tenemos que avisar que estamos excedidos.
#-----------------------------------------------------------------------------------------------------------------------

if horas_enteras > 24:
    print("Excedido (Los segundos ingresados exceden las 24 horas)")
else:
    print("La conversion de los segundos es:","\nHoras:", horas_enteras, "\nMinutos:", minutos_enteros, "\nSegundos:",
          segundos_enteros)

    print("Formato:\n",str(horas_enteras)+":"+str(minutos_enteros)+":"+str(segundos_enteros))


#-----------------------------------------------------------------------------------------------------------------------
 # Ahora haremos el proceso inverso, convertir de "horas:minutos:segundos" a un numero entero de segundos
# -----------------------------------------------------------------------------------------------------------------------

h= int(input("Ingrese las horas:\n"))
m= int(input("Ingrese los minutos:\n"))
s= int(input("Ingrese los segundos:\n"))

# -----------------------------------------------------------------------------------------------------------------------
 # Pasamos las horas a segundos multiplicando por 3600, llamaremos a esta vaiable hx3600
 # Tambien pasamos los minutos a segundos multiplicando por 60, llamaremos a esta variable mx60
# -----------------------------------------------------------------------------------------------------------------------

hx3600= h * 3600
mx60= m * 60

# -----------------------------------------------------------------------------------------------------------------------
 # Por ultimo sumamos las 2 variables anteriores con los segundos de entrada, esto nos dara el resultado final
# -----------------------------------------------------------------------------------------------------------------------

total_de_segundos= hx3600 + mx60 + s

print("La cantidad de segundos totales es:\n", total_de_segundos , "segundos")




