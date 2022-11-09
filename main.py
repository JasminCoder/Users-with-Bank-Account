#from CuentaBancaria import CuentaBancaria / ya no necesitamos importarla, pq usuario, la está importando
from Usuario import Usuario

#Crea 3 instancias de la clase Usuario
elena = Usuario("Elena", "elena@dojo.com")
juana = Usuario("Juana", "renata@dojo.com")
antonieta = Usuario("Antonieta", "catalina@dojo")


juana.hacer_retiro(100)
juana.hacer_deposito(500)

elena.hacer_deposito(1000).hacer_retiro(400)

elena.hacer_transferencia(300,antonieta)


antonieta.generar_interes()