#************************************************************
#************************************************************
# En el siguiente ejemplo podemos ver como la class SwitchElectrico depende directamente de la class Lampara para funcionar.
# Usando el principio de dependecia inversa crearemos una nueva class que tomando los methods necesarios, en este caso
# encendido y apagado, reemplace la dependencia de SwitchElectrico hacia Lampara, dandonos la posibilidad de crear mas classes
# que utilicen los mismos methods y asi poder reutilizar la class SwitchElectrico, generando un codigo mas limpio y reutilizable.
#************************************************************
#************************************************************

# class Lampara:
#     def encendido(self):
#         print("Lampara: encendida")

#     def apagado(self):
#         print("Lampara: apagada")


# class SwitchElectrico:
#     def __init__(self, l: Lampara):
#         self.lampara = l
#         self.on = False

#     def presionar(self):
#         if self.on:
#             self.lampara.apagado()
#             self.on = False
#         else:
#             self.lampara.encendido()
#             self.on = True

# l = Lampara()
# switch = SwitchElectrico(l)
# switch.presionar()
# switch.presionar()

#************************************************************
#************************************************************
# A continuacion importamos ABC y abstractclassmethod para crear una class abstracta que tomara como referencia los methods
# base que necesitamos usar, en este caso se refiere a que se enciende y que se apaga, luego se la aplicamos como parent a
# las clases que la utilicen.
# Ahora SwitchElectrico depende de Switchable y ya no mas de Lampara, pudiendo de esta manera agregar otros objetos que
# utilicen estos methods, en este caso agregaremos Televisor, por ejemplo.
#************************************************************
#************************************************************

from abc import ABC, abstractclassmethod

class Switchable(ABC):
    @abstractclassmethod
    def encendido(self):
        pass

    def apagado(self):
        pass


class Lampara(Switchable):
    def encendido(self):
        print("Lampara: encendida")

    def apagado(self):
        print("Lampara: apagada")


class Televisor(Switchable):
    def encendido(self):
        print("Televisor: encendido")

    def apagado(self):
        print("Televisor: apagado")


class SwitchElectrico:
    def __init__(self, a: Switchable):
        self.aparato = a
        self.on = False

    def presionar(self):
        if self.on:
            self.aparato.apagado()
            self.on = False
        else:
            self.aparato.encendido()
            self.on = True

l = Lampara()
t = Televisor()
switch = SwitchElectrico(t)
switch.presionar()
switch.presionar()
