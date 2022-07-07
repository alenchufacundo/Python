class Cuenta:

    def __init__(self,saldo):
        self.saldo = saldo #el valor saldo es el parametro, mientras que el self.saldo es el atributo.

    def evaluarMovimiento(self,montoMovimiento):
        if montoMovimiento == 0:
            print("movimiento invalido")
        elif montoMovimiento < 0 and (montoMovimiento * -1) > self.saldo:
            print("no tiene suficiente saldo")
        else:
            if montoMovimiento > 0:
                print("se ha realidad un deposito")
            elif montoMovimiento < 0:
                print("se ha realizado un retiro")
            self.saldo = self.saldo + montoMovimiento

cuentaFacundo = Cuenta (0) #el parametro que recibe es el saldo
cuentaMartin  = Cuenta (100)
cuentaFacundo.evaluarMovimiento(50) #el parametro que recibe es el montoMovimiento
cuentaMartin.evaluarMovimiento(500)