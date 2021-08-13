# En este caso vamos a ver porque la utilizacion de if __name__ == '__main__'
# Cuando creamos un archivo con codigo dentro, a veces necesitamos que solo cierta parte de este se ejecute, dependiendo
# de desde donde esta siendo ejecutado.

# Como podemos ver tenemos una funcion 'main' y el famoso if __name__.

def main():
    print ("Nombre del primero archivo: {}".format(__name__))


if __name__ == '__main__':
    main()
else:
    print("Nombre del primero archivo: {}".format(__name__))

# Si comentaramos todo y hariamos --> print (__name__), veriamos que nos imprime __main__. ¿Que quiere decir esto?.

# Python tiene variables especiales y __name__ es una de esas, cuando ejecutamos un archivo directamente, Python dice
# que la variable __name__ es igual a __main__.
# En este caso el if tomaria la referencia como True y ejecutaria la funcion main dandonos como resultado del print:
# "Nombre del primero archivo: __main__".

# ¿Pero que pasa si importamos el archivo?
# Vayamos a el archivo if_name_main_import y veamos.




