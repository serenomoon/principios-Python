# Usando los principios SOLID para mejorar y ordenar classes y methods:
# El codigo esta simplificado para el entendimiento, sobre todo las partes de autorizacion.

# Aquí tenemos una class Order que se encarga de generar un objeto en base a un pedido, en este caso supongamos
# que es una tienda de cafe.
# Dentro de la class tenemos 4 atributos: items(el tipo de producto),quantities(las cantidades de ese producto), 
# prices(el precio del producto) y status (el estatus del producto).
# Usando el method add_item podemos agregar un nuevo item al pedido con sus caracteristicas.
# Usando el method total_price obtendremos (luego de haber generado uno o mas productos y que se vayan sumando 
# al array con append) el precio final de la compra usando un for loop.

# Luego tenemos el method pay, y sus atributos de instancia, que son: payment_type (el tipo de pago) y security_code (el codigo
# de seguridad para habilitar dicho pago).

# class Order:
#     item = []
#     quantities = []
#     prices = []
#     status = "open"

#     def add_item(self,name,quantity,price):
#         self.item.append(name)
#         self.quantities.append(quantity)
#         self.prices.append(price)
    
#     def total_price(self):
#         total = 0
#         for i in range(len(self.prices)):
#             total += self.quantities[i] * self.prices[i]
#         return total

#     def pay(self,payment_type,security_code):
#         if payment_type == "debito":
#             print("Procesando pago tipo debito")
#             print(f"Verificando codigo de seguridad: {security_code}")
#             self.status = "paid"
#         elif payment_type == "credito":
#             print("Procesando pago tipo credito")
#             print(f"Verificando codigo de seguridad: {security_code}")
#             self.status = "paid"
#         else:
#             raise Exception(f"Error en el tipo de pago: {payment_type}")


# Tomamos la class Order, generamos varios objetos, obtenemos el precio total y habilitamos el tipo de pago:

# order = Order()
# order.add_item("cafe",2,50)
# order.add_item("te",1,30)
# order.add_item("medialuna",5,15)
# print(order.total_price())
# order.pay("debito","0303456")

# **********************************************************************************
# **********************************************************************************
# S -> SINGLE RESPONSiBILITY PRINCIPLE.

# El problema que tenemos ahora, es que la class Order se ocupa tambien del metodo de pago, siendo mas prudente
# que ambas actividades esten por separado, si queremos agregar un nuevo metodo de pago tendriamos que estar
# modificando la class Order cada vez que eliminemos o agreguemos uno.
# **********************************************************************************
# **********************************************************************************
# Para resolver este problema creamos otra class llamada PaymentProcessor y sus metodos pay_debit y pay_credit.
# De esta forma ya no necesitamos modificar la class Order para agregar un nuevo metodo de pago, ni tampoco especificar,
# a la hora de crear el objeto, que tipo de pago se va a efectuar, simplemente llamamos al method que necesitemos dentro
# de la class PaymentProcessor.


# class Order:
#     item = []
#     quantities = []
#     prices = []
#     status = "open"

#     def add_item(self,name,quantity,price):
#         self.item.append(name)
#         self.quantities.append(quantity)
#         self.prices.append(price)
    
#     def total_price(self):
#         total = 0
#         for i in range(len(self.prices)):
#             total += self.quantities[i] * self.prices[i]
#         return total

# class PaymentProcessor:
#     def pay_debit(self,order,security_code):
#         print("Procesando pago tipo debito")
#         print(f"Verificando codigo de seguridad: {security_code}")
#         order.status = "paid"
#     def pay_credit(self,order,security_code):
#         print("Procesando pago tipo credito")
#         print(f"Verificando codigo de seguridad: {security_code}")
#         order.status = "paid"

# order = Order()
# order.add_item("cafe",2,50)
# order.add_item("te",1,30)
# order.add_item("medialuna",5,15)

# print(order.total_price())

# processor = PaymentProcessor()
# processor.pay_debit(order,"0303456")

# **********************************************************************************
# **********************************************************************************
# O -> OPEN/CLOSE PRINCIPLE

# Este principio se refiere a que deberiamos ser capaces de extender el codigo existente con nuevas funcionalidades
# sin necesidad de modificarlo.
# Basicamente si queremos agregar otro tipo de pago, debemos modificar la class PaymentProcessor constantemente, sea
# para agregar o eliminar un metodo de pago.
# **********************************************************************************
# **********************************************************************************
# En este caso usamos ABC para convertir el method pay de la class PaymentProcessor en un method abstracto 
# (un method que esta declarado pero que no tiene una implementacion de por si).
# A continuacion creamos 3 nuevas child classes: DebitPaymentProcessor, CreditPaymentProcessor y PaypalPaymentProcessor 
# que heredan las propiedades y methods de PaymentProcessor.
# Ahora cada vez que queramos agregar un metodo de pago a nuestro codigo, simplemente creamos una nueva child class.


# from abc import ABC, abstractmethod

# class Order:
#     item = []
#     quantities = []
#     prices = []
#     status = "open"

#     def add_item(self,name,quantity,price):
#         self.item.append(name)
#         self.quantities.append(quantity)
#         self.prices.append(price)
    
#     def total_price(self):
#         total = 0
#         for i in range(len(self.prices)):
#             total += self.quantities[i] * self.prices[i]
#         return total

# class PaymentProcessor(ABC):
#     @abstractmethod
#     def pay(self,order,security_code):
#         pass

# class DebitPaymentProcessor(PaymentProcessor):
#     def pay(self,order,security_code):
#         print("Procesando pago tipo debito")
#         print(f"Verificando codigo de seguridad: {security_code}")
#         order.status = "paid"
            
# class CreditPaymentProcessor(PaymentProcessor):
#     def pay(self,order,security_code):
#         print("Procesando pago tipo credito")
#         print(f"Verificando codigo de seguridad: {security_code}")
#         order.status = "paid"

# class PaypalPaymentProcessor(PaymentProcessor):
#     def pay(self,order,security_code):
#         print("Procesando pago tipo paypal")
#         print(f"Verificando codigo de seguridad: {security_code}")
#         order.status = "paid"

# En este caso el cliente eligio pagar con debito y usamos la child class DebitPaymentProcessor.

# order = Order()
# order.add_item("cafe",2,50)
# order.add_item("te",1,30)
# order.add_item("medialuna",5,15)

# print(order.total_price())

# processor = DebitPaymentProcessor()
# processor.pay(order,"0303456")

# **********************************************************************************
# **********************************************************************************
# L -> LISKOV SUBSTITUTION PRINCIPLE

# Nuestro siguiente problema a resolver es el siguiente: no todos los metodos de pago usan el mismo metodo de verificacion.
# Este principio se refiere a que si tenemos objetos en nuestro codigo, deberiamos ser capaces de reemplazar estos objetos
# por instancias de sus "subtipos" o "subclases" sin alterar el buen funcionamiento del codigo.
# **********************************************************************************
# **********************************************************************************
# En este caso el problema es nuestra class PaypalPaymentProcessor y su instancia security_code, ya que Paypal utiliza 
# verificacion por email y no por codigo de segurirad.
# Para resolver este problema le pedimos a la class PaymentProcessor que ya no pida el security_code, a continuacion 
# creamos una funcion __init__ en cada class de metodo de pago, donde pida como instancia su metodo de verificacion.
# De esta manera si queremos agregar otro metodo de pago, con otro tipo de verificacion, podemos creas su class y su nueva
# instancia sin problemas.

# from abc import ABC, abstractmethod

# class Order:
#     item = []
#     quantities = []
#     prices = []
#     status = "open"

#     def add_item(self,name,quantity,price):
#         self.item.append(name)
#         self.quantities.append(quantity)
#         self.prices.append(price)
    
#     def total_price(self):
#         total = 0
#         for i in range(len(self.prices)):
#             total += self.quantities[i] * self.prices[i]
#         return total

# class PaymentProcessor(ABC):
#     @abstractmethod
#     def pay(self,order):
#         pass

# class DebitPaymentProcessor(PaymentProcessor):

#     def __init__(self,security_code):
#         self.security_code = security_code

#     def pay(self,order):
#         print("Procesando pago tipo debito")
#         print(f"Verificando codigo de seguridad: {self.security_code}")
#         order.status = "paid"

# class CreditPaymentProcessor(PaymentProcessor):

#     def __init__(self,security_code):
#         self.security_code = security_code

#     def pay(self,order):
#         print("Procesando pago tipo credito")
#         print(f"Verificando codigo de seguridad: {self.security_code}")
#         order.status = "paid"

# class PaypalPaymentProcessor(PaymentProcessor):

#     def __init__(self,email_address):
#         self.email_address = email_address

#     def pay(self,order):
#         print("Procesando pago tipo paypal")
#         print(f"Verificando email: {self.email_address}")
#         order.status = "paid"

# order = Order()
# order.add_item("cafe",2,50)
# order.add_item("te",1,30)
# order.add_item("medialuna",5,15)

# print(order.total_price())

# processor = PaypalPaymentProcessor("saulo@gmail.com")
# processor.pay(order)

# **********************************************************************************
# **********************************************************************************
# I -> INTERFACE SEGREGATION PRINCIPLE

# Este principio se refiere a que es mejor, ya sea por funcionamiento, mantenimiento y entendimiento de los programadores
# tener una interfaz para cada proposito en vez de tener una para varios.
# **********************************************************************************
# **********************************************************************************
# En este caso hemos agregado a la class PaymentProcessor un methdo llamado auth_sms, este metodo se encargaria de verificar
# mediante un codigo SMS si el pago es valido o no.
# Como podemos ver el pago con tarjeta de credito no requiere una verificacion SMS, por lo que seria innecesario traer a
# colacion el method auth_sms.

# from abc import ABC, abstractmethod

# class Order:
#     item = []
#     quantities = []
#     prices = []
#     status = "open"

#     def add_item(self,name,quantity,price):
#         self.item.append(name)
#         self.quantities.append(quantity)
#         self.prices.append(price)
    
#     def total_price(self):
#         total = 0
#         for i in range(len(self.prices)):
#             total += self.quantities[i] * self.prices[i]
#         return total

# class PaymentProcessor(ABC):
#     @abstractmethod
#     def pay(self,order):
#         pass

#     @abstractmethod
#     def auth_sms(self,code):
#         pass

# class DebitPaymentProcessor(PaymentProcessor):

#     def __init__(self,security_code):
#         self.security_code = security_code
#         self.verified = False
    
#     def auth_sms(self,code):
#         print(f"Verificando codigo SMS: {code}")
#         self.verified = True

#     def pay(self,order):
#         if not self.verified:
#             raise Exception("No autorizado")
#         print("Procesando pago tipo debito")
#         print(f"Verificando codigo de seguridad: {self.security_code}")
#         order.status = "paid"

# class CreditPaymentProcessor(PaymentProcessor):

#     def __init__(self,security_code):
#         self.security_code = security_code

#     def auth_sms(self,code):
#         raise Exception("Los pagos con tarjeta de credito no necesitan autorizacion por codigo SMS")

#     def pay(self,order):
#         print("Procesando pago tipo credito")
#         print(f"Verificando codigo de seguridad: {self.security_code}")
#         order.status = "paid"

# class PaypalPaymentProcessor(PaymentProcessor):

#     def __init__(self,email_address):
#         self.email_address = email_address
#         self.verified = False

#     def auth_sms(self,code):
#         print(f"Verificando codigo SMS: {code}")
#         self.verified = True

#     def pay(self,order):
#         if not self.verified:
#             raise Exception("No autorizado")
#         print("Procesando pago tipo paypal")
#         print(f"Verificando email: {self.email_address}")
#         order.status = "paid"

#------------------- Solucion -----------------
# Creamos una nueva child class de PaymentProcessor llamada PaymentProcessor_SMS y procedemos a colocar el abstractmethod
# auth_sms dentro. Luego usamos PaymentProcessor_SMS como parent class para las child class que utilicen el metodo de 
# autentificacion por SMS, puediendo de esta manera eliminar las lineas de codigo innecesarias en CreditPaymentProcessor.

# from abc import ABC, abstractmethod

# class Order:
#     item = []
#     quantities = []
#     prices = []
#     status = "open"

#     def add_item(self,name,quantity,price):
#         self.item.append(name)
#         self.quantities.append(quantity)
#         self.prices.append(price)
    
#     def total_price(self):
#         total = 0
#         for i in range(len(self.prices)):
#             total += self.quantities[i] * self.prices[i]
#         return total

# class PaymentProcessor(ABC):
#     @abstractmethod
#     def pay(self,order):
#         pass


# class PaymentProcessor_SMS(PaymentProcessor):
#     @abstractmethod
#     def auth_sms(self,code):
#         pass


# class DebitPaymentProcessor(PaymentProcessor_SMS):
#     def __init__(self,security_code):
#         self.security_code = security_code
#         self.verified = False
    
#     def auth_sms(self,code):
#         print(f"Verificando codigo SMS: {code}")
#         self.verified = True

#     def pay(self,order):
#         if not self.verified:
#             raise Exception("No autorizado")
#         print("Procesando pago tipo debito")
#         print(f"Verificando codigo de seguridad: {self.security_code}")
#         order.status = "paid"

# class CreditPaymentProcessor(PaymentProcessor):
#     def __init__(self,security_code):
#         self.security_code = security_code

#     def pay(self,order):
#         print("Procesando pago tipo credito")
#         print(f"Verificando codigo de seguridad: {self.security_code}")
#         order.status = "paid"

# class PaypalPaymentProcessor(PaymentProcessor_SMS):
#     def __init__(self,email_address):
#         self.email_address = email_address
#         self.verified = False

#     def auth_sms(self,code):
#         print(f"Verificando codigo SMS: {code}")
#         self.verified = True

#     def pay(self,order):
#         if not self.verified:
#             raise Exception("No autorizado")
#         print("Procesando pago tipo paypal")
#         print(f"Verificando email: {self.email_address}")
#         order.status = "paid"

#------------------- Solucion 2-----------------
# Para mejorar el codigo usaremos composicion en vez de heredar la class.
# Creamos una nueva class llamada SMSauth que verifica el codigo SMS y lo autoriza mediante un booleano.
# De esta manera las classes DebitPaymentProcessor y PaypalPaymentProcessor volveran a recibir como parent a la class
# PaymentProcessor, pero les agregaremos una nueva instancia de autorizacion, deribada de la nueva class SMSAuth.
# De esta manera la verificacion ya no se hara dentro de la class del metodo de pago.

# from abc import ABC, abstractmethod

# class Order:
#     item = []
#     quantities = []
#     prices = []
#     status = "open"

#     def add_item(self,name,quantity,price):
#         self.item.append(name)
#         self.quantities.append(quantity)
#         self.prices.append(price)
    
#     def total_price(self):
#         total = 0
#         for i in range(len(self.prices)):
#             total += self.quantities[i] * self.prices[i]
#         return total

# class PaymentProcessor(ABC):
#     @abstractmethod
#     def pay(self,order):
#         pass

# class SMSauth:
#     authorized = False

#     def verify_code(self,code):
#         print(f"Verificando codigo: {code}")
#         self.authorized = True
    
#     def is_authorized(self) -> bool:
#         return self.authorized


# class DebitPaymentProcessor(PaymentProcessor):
#     def __init__(self,security_code,authorizer: SMSAuth):
#         self.security_code = security_code
#         self.authorizer = authorizer

#     def pay(self,order):
#         if not self.authorized.is_authorized():
#             raise Exception("No autorizado")
#         print("Procesando pago tipo debito")
#         print(f"Verificando codigo de seguridad: {self.security_code}")
#         order.status = "paid"

# class CreditPaymentProcessor(PaymentProcessor):
#     def __init__(self,security_code):
#         self.security_code = security_code

#     def pay(self,order):
#         print("Procesando pago tipo credito")
#         print(f"Verificando codigo de seguridad: {self.security_code}")
#         order.status = "paid"

# class PaypalPaymentProcessor(PaymentProcessor):
#     def __init__(self,email_address,authorizer: SMSAuth):
#         self.email_address = email_address
#         self.authorizer = authorizer

#     def pay(self,order):
#         if not self.authorized.is_authorized():
#             raise Exception("No autorizado")
#         print("Procesando pago tipo paypal")
#         print(f"Verificando email: {self.email_address}")
#         order.status = "paid"

# order = Order()
# order.add_item("cafe",2,50)
# order.add_item("te",1,30)
# order.add_item("medialuna",5,15)

# print(order.total_price())
# authorizer = SMSAuth()
# processor = PaypalPaymentProcessor("saulo@gmail.com", authorizer)
# authorizer.verify_code(303456)
# processor.pay(order)

# **********************************************************************************
# **********************************************************************************
# D -> Dependency Inversion

# Lo que haremos aqui sera hacer que las clases dependan de clases abstractas en lugar de clases no abstractas.
# Hacer que las clases hereden de las clases abstractas.
# **********************************************************************************
# **********************************************************************************
# En este caso crearemos una nueva class abstracta llamada Authorized, de la que deribaran las classes que se utilicen
# para autenticacion.
# Sumaremos como ejemplo una nueva class de autenticacion llamada NotARobot, en la que verificaremos (muy simplemente)
# si el usuario es un robot.

from abc import ABC, abstractmethod

class Order:
    item = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self,name,quantity,price):
        self.item.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)
    
    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self,order):
        pass

class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self) -> bool:
        pass

class SMSauth(Authorizer):
    authorized = False

    def verify_code(self,code):
        print(f"Verificando codigo: {code}")
        self.authorized = True
    
    def is_authorized(self) -> bool:
        return self.authorized

class NotARobot(Authorizer):
    authorized = False

    def not_a_robot(self):
        print("¿Eres un Robot? No lo creo...")
        self.authorized = True
    
    def is_authorized(self) -> bool:
        return self.authorized


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code, authorizer: Authorizer):
        self.security_code = security_code
        self.authorizer = authorizer

    def pay(self,order):
        if not self.authorizer.is_authorized():
            raise Exception("No autorizado")
        print("Procesando pago tipo debito")
        print(f"Verificando codigo de seguridad: {self.security_code}")
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self,order):
        print("Procesando pago tipo credito")
        print(f"Verificando codigo de seguridad: {self.security_code}")
        order.status = "paid"

class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_address, authorizer: Authorizer):
        self.email_address = email_address
        self.authorizer = authorizer

    def pay(self,order):
        if not self.authorizer.is_authorized():
            raise Exception("No autorizado")
        print("Procesando pago tipo paypal")
        print(f"Verificando email: {self.email_address}")
        order.status = "paid"

# A continuacion elegiremos que class/method utilizar a la hora de autenticar y lo pondremos a prueba.

order = Order()
order.add_item("cafe",2,50)
order.add_item("te",1,30)
order.add_item("medialuna",5,15)

print(order.total_price())

authorizer =  NotARobot()

processor = PaypalPaymentProcessor("saulo@gmail.com", authorizer)
authorizer.not_a_robot()
processor.pay(order)

# **********************************************************************************
#                               Por Saulo Fernandez
# **********************************************************************************
