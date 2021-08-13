import if_name_main

# En este caso importamos el archivo y si ejecutamos directamente este archivo podemos ver como la funcion de if_name_main
# pasa directamente al else. ¿Por que?

# Si imprimimos desde este archivo podemos ver que el resultado del print ya no es: "Nombre del primero archivo: __main__"
# sino que es: "Nombre del primero archivo: if_name_main"

# Si agregamos un print igual aqui, podemos ver que ahora __main__ pertenece a este archivo (siempre y cuando lo ejecutemos directamente)

print ("Nombre del segundo archivo: {}".format(__name__))

# ¿Que podemos lograr con esto?
# Si agregaramos nuevas lineas de codigo en el primer archivo, pero fuera de la funcion main, se ejecutarian sin importar cual
# de los dos archivos estemos ejectuando. Pero todo lo que este dentro de la funcion main, solo seria llamado si ejecutaramos
# el primer archivo directamente.

# ¿Pero por que no poner nuestro codigo directamente en la condicion if else?.
# No solo por orden usamos la funcion main en este caso, ademas en el momento que queramos podriamos llamarla desde un
# archivo ajeno, por ejemplo, de la siguiente manera:
#if_name_main.main()