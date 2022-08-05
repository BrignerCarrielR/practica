class Cliente:
    def __init__(self,cedula,nombre,telefono,correo):
        self.cedula=cedula
        self.nombre=nombre
        self.telefono=telefono
        self.correo=correo

    def validaCedula(self):
        if len(self.cedula) == 10:
            return self.cedula
        else:
            return "999999999"

    def mostrarCliente(self):
        print("Cliente: {} - {} - {}".format(self.nombre,self.cedula,self.correo))

class ClienteCorporativo(Cliente):
    def __init__(self, nombre,  cedula,telefono, correo, contrato):
        super().__init__(nombre,cedula, telefono, correo)
        self.contrato=contrato

    def mostrarCliente(self):
        contra="Contrato Vigente" if self.contrato else "Sin Contrato"
        super().mostrarCliente()
        print("{}".format(contra))

class ClientePersonal(Cliente):
    def __init__(self, nombre,  cedula, telefono, correo, promocion=False):
        super().__init__(nombre, cedula, telefono, correo)
        self.__promocion=promocion

    @property
    def promocion(self):    #Getter: obtener el valor del atributo privado
        if self.__promocion==True:
            self.__promocion=0.10
        else:
            self.__promocion=0
        return self.__promocion

    @promocion.setter
    def promocion(self,value):  #Setter: setear el valor del atributo privado
        if value==True:
            self.__promocion=0.10
        else:
            self.__promocion=0

    def mostrarCliente(self):
        print("Cliente: {} - {} - {} - {}".format(self.nombre,self.cedula,self.correo,self.__promocion))

if __name__ == "__main__":

    cli = ClienteCorporativo("0960285305",'Brigner','0962164367','bcarriel@unemi.edu.ec',True)
    cli.mostrarCliente()