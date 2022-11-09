#Actualiza tu clase Usuario existente para que tenga una asociación con la clase CuentaBancaria.
from CuentaBancaria import CuentaBancaria

class Usuario:		

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cuenta = CuentaBancaria() #no necesitamos enviar nada en los (), pq ya x defcto viene el interes en 0.3 
        #y el balance en 0 desde cta bancaria)


    def hacer_deposito(self, monto):
        self.cuenta.deposito(monto)
        self.mostrar_balance()
        return(self)
        

    def hacer_retiro(self, amount):
        self.cuenta.retiro(amount)
        self.mostrar_balance()
        return(self)


    def hacer_transferencia(self, monto, otro_usuario):
        self.cuenta.retiro(monto)
        otro_usuario.cuenta.deposito(monto)
        self.mostrar_balance()
        otro_usuario.mostrar_balance()
        return(self)


    def mostrar_balance(self):
        print(f"Usuario: {self.name}, Balance: {self.cuenta.balance}")



    def generar_interes(self):
        self.cuenta.generar_interes()
        self.mostrar_balance()
        return(self)
