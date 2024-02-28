from Fecha import Fecha

...
class Empleado:
    #Aqui va el codigo de empleado
    '''
    #Atributos
    '''
    nombre=''
    apellido=''
    '''-----------------------------------------------------------------------------------------#1=Masculino y 2 Femenino----------------------------------------------------------'''
    sexo=0
    salario=0
    '''--------------------------------------------------------------------------------------------------------------------
    #Asociaciones----------------------------------------------------------------------------------------------------------'''

    fechaNacimiento=Fecha()
    fechaIngreso=Fecha()
    '''--------------------------------------------------------# Metodos---------------------------------------------'''
    def CambiarSalario(self, nuevoSalario):
        #Aqui va el codigo del metodo
        return 0
    def CambiarEmpleado(self, nNombre, nApellido, nSexo, nSalario):
        #Aqui va el codigo de nuevo empleado
        return None

    def ConsultarSalario(self):
        #Aqui va el codigo del metodo
        return self.salario
    def Consultarnombre(self):
        #Aqui va el codigo del metodo
        return self.nombre

    def ConsultarApellido(self):
        #Aqui va el codigo del metodo
        return self.apellido

    palabra1 = nombre
    palabra2 = apellido
    nombreCompleto = nombre+''+apellido

    def ConsultarNombreCompleto(self):

        return self.nombre +" "+ self.apellido

    def AumentoSalarial(self):
        nSalario = self.salario * 0.05
        nSalario = nSalario + self.salario
        self.salario = nSalario

    def duplicarSalario(self):
        #Aqui va el codigo
        #Forma 1
        #Self.salario = self.salario*=12
        #Forma 2 pro
        self.salario *= 2

    def CalcularSalarioAnual(self):
        #Aqui va el codigo
        #Self.salario = self.salario*=12
        return salarioAnual
        #Forma 2
        SalarioAnual = self.salario*12
    '''-----------------------------------------------------metodos-------------------------------------------------------------------'''

    def ConsultarDiaCumpleaños(self)
        return "el dia de cumpleaños es: "+self.fechaNacimiento.ConsultarDia()

    def CalcularImpuesto(self):
        #Forma1
        total = self.CalcularSalarioAnual()
        return (total * 19.5) / 100
    #Forma2
        return self.CalcularSalarioAnual() * 0.195