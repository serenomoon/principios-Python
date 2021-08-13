import if_name_main

# En este caso importamos el archivo y si ejecutamos directamente este archivo podemos ver como la función de if_name_main
# pasa directamente al else. ¿Por que?

# Si imprimimos desde este archivo podemos ver que el resultado del print ya no es: "Nombre del primero archivo: __main__"
# sino que es: "Nombre del primero archivo: if_name_main"

# Si agregamos un print igual aquí, podemos ver que ahora __main__ pertenece a este archivo (siempre y cuando lo ejecutemos directamente)

print ("Nombre del segundo archivo: {}".format(__name__))

# ¿Qué podemos lograr con esto?
# Si agregáramos nuevas líneas de código en el primer archivo, pero fuera de la función main, se ejecutarían sin importar cual
# de los dos archivos estemos ejecutando. Pero todo lo que este dentro de la función main, solo seria llamado si ejecutáramos
# el primer archivo directamente.

# ¿Pero por que no poner nuestro código directamente en la condición if else?.
# No solo por orden usamos la función main en este caso, además en el momento que queramos podríamos llamarla desde un
# archivo ajeno, por ejemplo, de la siguiente manera:
#if_name_main.main()
