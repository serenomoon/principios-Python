import string
import random

#***********************************************************************************
#***********************************************************************************
# Acoplamiento y cohesión son términos que ocurren juntos muy frecuentemente. El acoplamiento se refiere a la
# interdependencia entre módulos, mientras que la cohesión describe cómo se relacionan las funciones dentro de
# un modulo independiente.
# A continuación tomamos de ejemplo dos clases que se encargan del registro de vehículos:
# RegistroVehiculo se encarga de generar una id y una licencia(patente) en base a esa id.
# Por otro lado Aplicación se encarga de registrar el vehículo:
#   Tomar y guardar en una variable el id y la patente (de RegistroVehiculo), crear el precio mediante un catalogo,
#   chequear el tipo de impuesto a agregar dependiendo del vehículo (el impuesto cambia si el vehículo es eléctrico)
#   y calcular el total del impuesto.
#   Para luego imprimir toda la información del vehículo creado.
#***********************************************************************************
#***********************************************************************************

# class RegistroVehiculo:

#   def generar_vehiculo_id(self, length):
#     return ''.join(random.choices(string.ascii_uppercase, k=length))

#   def generar_vehiculo_licencia(self, id):
#     return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"


# class Aplicacion:

#   def registrar_vehiculo(self, marca: string):
#     #crea una instancia del registro
#     registro = RegistroVehiculo()

#     #genera un id del vehículo de 12 caracteres
#     vehiculo_id = registro.generar_vehiculo_id(12)

#     #ahora genera una patente para el vehículo
#     #usando los primeros dos caracteres del id del vehículo
#     patente = registro.generar_vehiculo_licencia(vehiculo_id)

#     #computa el precio de catalogo
#     precio_catalogo = 0
#     if marca == "Tesla Model 3":
#       precio_catalogo = 60000
#     elif marca == "Volkswagen ID3":
#       precio_catalogo = 35000
#     elif marca == "BMW 5":
#       precio_catalogo = 45000
   
#     #computa el porcentaje de impuestos (el precio normal por catalogo es 5%, menos para vehículos eléctricos, donde es 2%)
#     porcentaje_imp = 0.05
#     if marca == "Tesla Model 3" or marca == "Volkswagen ID3":
#       porcentaje_imp = 0.02
   
#     #computa el total de impuesto
#     total_imp = porcentaje_imp * precio_catalogo

#     #imprime la información del vehículo registrado
#     print("Registro completo. Información del Vehículo:")
#     print(f"Marca: {marca}")
#     print(f"Id: {vehiculo_id}")
#     print(f"Patente: {patente}")
#     print(f"Total impuestos: {total_imp}")

# app = Aplicacion()
# app.registrar_vehiculo("BMW 5")


#***********************************************************************************
#***********************************************************************************
# Como podemos ver tenemos dos clases que se encargan de varios factores a la vez y tienen muchas responsabilidades,
# y que si modificaramos una de las dos, la otra clase seguramente dejaría de funcionar.

# Por ejemplo, si quisiéramos agregar un nuevo vehículo eléctrico,
# tendríamos que agregar una nueva linea al if de precio_catalogo, y además agregar otro "or" en el if de porcentaje_imp,
# y así con cada nuevo vehículo agregado.

# Otro ejemplo de poca cohesión es que si cambiara algún método de RegistroVehiculo tendría que también
# cambiarlo en Aplicacion (cuando es llamado):

#    RegistroVehiculo                Aplicacion

# generar_vehiculo_id(self, length) -> vehiculo_id = registro.generar_vehiculo_id(12)

# generar_vehiculo_licencia(self, id) -> patente = registro.generar_vehiculo_licencia(vehiculo_id) 
#***********************************************************************************
#***********************************************************************************
# A continuación mejoramos nuestro código tomando en cuenta los distintos tipos de datos generados en nuestras class
# y separandolos como es debido.


# Primer separamos la información del vehículo y tenemos en cuanta con un booleano si es eléctrico o no.
# En esta misma información tenemos el impuesto y calculamos el total (esto podríamos también hacerlo en otra class)
# Luego creamos un método para imprimir la marca y el impuesto total.

class VehiculoInfo:
    marca: str
    precio_catalogo: int
    electrico: bool

    def __init__(self, marca, electrico, precio_catalogo):
        self.marca = marca
        self.electrico = electrico
        self.precio_catalogo = precio_catalogo
    
    def computar_imp(self):
        porcentaje_imp = 0.05
        if self.electrico:
            porcentaje_imp = 0.02
        return porcentaje_imp * self.precio_catalogo

    def print(self):
        print(f"Marca: {self.marca}")
        print(f"Impuesto Total: {self.computar_imp()}")


# En esta class tenemos el id, la patente, y llamamos a la anterior class como info.
# Luego imprimimos el id y la patente, a su vez llamamos el método de info para sumar los datos impresos.
class Vehiculo:
    id: str
    patente: str
    info: VehiculoInfo

    def __init__(self, id, patente, info):
        self.id = id
        self.patente = patente
        self.info = info

    def print(self):
        print(f"ID: {self.id}")
        print(f"Patente: {self.patente}")
        self.info.print()


# Esta class se encarga de llamar a las anteriores class, insertar los datos y registrarlos en un diccionario.
class RegistroVehiculo:

    vehiculo_info = { } #En un ambiente mas real insertariamos los datos en una db, por ejemplo.

    def agregar_vehiculo_info(self, marca, electrico, precio_catalogo):
        self.vehiculo_info[marca] = VehiculoInfo(marca, electrico, precio_catalogo)

    # Como vemos, ahora podemos agregar nuevos vehículos sin necesidad de modificar nada.
    # Ya que ahora el factor determinante para calcular los impuestos es un booleano que insertamos al introducir el nuevo
    # vehículo (si es eléctrico o no).
    def __init__(self):
        self.agregar_vehiculo_info("Tesla Model 3", True, 60000)
        self.agregar_vehiculo_info("Volkswagen ID3", True, 30000)
        self.agregar_vehiculo_info("BMW 5", False, 45000)
        
    def generar_vehiculo_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generar_vehiculo_licencia(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def crear_vehiculo(self, marca):
        vehiculo_id = self.generar_vehiculo_id(12)
        patente = self.generar_vehiculo_licencia(vehiculo_id)
        return Vehiculo(vehiculo_id, patente, self.vehiculo_info[marca])


# Ahora Aplicación solo se encarga de llamar a RegistroVehiculo y su método crear_vehiculo.
class Aplicacion:

    def registrar_vehiculo(self, marca: string):
        #crea una instancia del registro
        registro = RegistroVehiculo()

        #crea el vehiculo
        return registro.crear_vehiculo(marca)

app = Aplicacion()
vehiculo = app.registrar_vehiculo("BMW 5")
vehiculo.print()
