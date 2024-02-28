from cuentaCorriente import cuentaCorriente
from cuentaAhorros import cuentaAhorros

class simulador_bancario:
    #Aqui va el codigo del simulador bancario
    '''----------------------------------------------------------------------------atributos--------------------------------------------------------'''

    cedula=0
    nombres=0
    mes_actual=0

    '''-----------------------------------------asociaciones--------------------------------'''

    cuentaCorriente = cuentaCorriente()
    cuentaAhorros = cuentaAhorros()

    '''------------------------------------metodos-------------------------------------'''

    def ConsignarCuentaCorriente(self.saldo):
        #Aqui va el codigo del metodo
        return 'el saldo a consignar es de:'+self.saldo()

    def calcularSaldoCuentaCorriente(self):
        #Aqui va el codigo del metodo
        return 'este es el saldo'+self.calcularSaldo

    def ConsignarCuentaAhorro(self):
        #Aqui va el codigo del metodo
        return 'este es el saldo'+self.saldo()

    def CalcularSaldoCuentaAhorro(self):
        #Aqui va el codigo del metodo
        return 'este es el saldo'+self.saldo()

    def CalcularSaldoTotal(self):
        #Aqui va el codigo del metodo
        return 'este es el saldo total'+ self.CalcularSaldoCuentaAhorro + CalcularSaldoCuentaCorriente()