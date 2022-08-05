from abc import ABC, abstractmethod
class Cliente(ABC):
    def __init__(self,cedula,nombre,telefono,correo):
        self.cedula=cedula
        self.nombre=nombre
        self.telefono=telefono
        self.correo=correo

    @abstractmethod
    def validaCedula(self):
        pass

    def mostrarCliente(self):
        print("Cliente: {} - {} - {}".format(self.nombre,self.cedula,self.correo))
    
class ClienteCorporativo(Cliente):
    def __init__(self, nombre,  cedula,telefono, correo, contrato):
        super().__init__(nombre,cedula, telefono, correo)
        self.__contrato='Con contrato vigente' if contrato else "Sin Contrato"

    def validaCedula(self):
        if len(self.cedula) == 13:
            return self.cedula
        else:
            return None

clie1=ClienteCorporativo('brigner','0954826178','0962164367','abr@gmail.com',False)
clie1.mostrarCliente()
