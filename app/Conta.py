class Conta:
    def __init__(self,titular,numero,saldo):
        self.saldo=100
        self.numero=numero
        self.titular=titular
    @property
    def saldo (self):
        return self._saldo 
    @saldo.setter
    def set_saldo(self,saldo):
        if(saldo<0):   
            print("O saldo não pode ser negativo")
        else:
            self._saldo=saldo
