class CuentaBancaria:

    cuentas = [] #lista vacia para guardar todas las ctas bancarias q se van creando


    def __init__(self): 
        self.tasa_interés = 0.3 #no necesitamos recibirlo en el init
        self.balance = 0 #estamos diciendo q todas las cuentas comiencen con un balance en 0, por lo q en el consructor (init) 
        #no necesitamos poner nada 
        CuentaBancaria.cuentas.append(self) #Cada vez q creemos una cuenta, se va a guardar en la lista cuentas
        #CuentaBancaria.todas_las_instancias.append(self)


    
    def deposito(self, monto):
        self.balance += monto
        return (self)
        


    def retiro(self, amount):
        if amount <= self.balance: #primero comprobar si el monto a retirar es menor o igual a lo q tenemos en balance
        #si eso se da, hacemos el retiro (descuento)
            self.balance -= amount
        #si no se da, imprimimos
        else:
            print('Fondos insuficientes, cobrando una multa de $5')
            self.balance -= 5
            return(self)    



    def interes(self):
        if self.balance > 0:
            self.balance += self.balance * self.tasa_interés
        return(self)


