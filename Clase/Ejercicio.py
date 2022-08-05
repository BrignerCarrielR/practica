from datetime import date
class Departamento:
    def __init__(self,cd_epart, nom_depart, bloque):
        self.codigo=cd_epart
        self.nombre= nom_depart
        self.bloque=bloque

class Empleados():
    def __init__(self,nombre,cedula,telefono,ciudad,sueldo):
        self.nombre=nombre
        self.cedula=cedula
        self.telefono=telefono
        self.sueldo=sueldo
        self.ciudad=ciudad

    def mostrarCliente(self):
        print("Cliente: {} - {} - {}".format(self.cedula,self.nombre,self.correo))

class EmpleadoObrero(Empleados):
    _iva=0.12
    def __init__(self,nombre,cedula,telefono,sueldo,ciudad,sobretiempo):
        super().__init__(nombre,cedula,telefono,ciudad,sueldo)
        self.sobretiempo=sobretiempo
        self.fecha=date.today()
    def GananciaObrero(self):
        print('Sueldo :{}  descuento:$15'.format(self.sueldo))
        self.sueldo= self.sueldo-15
        print('{} Gana: {} de su sueldo base'.format(self.nombre,self.sueldo))

class EmpleadoAdministrativo(Empleados):
    def __init__(self,nombre,cedula,telefono,sueldo,ciudad,sobretiempo):
        super().__init__(nombre,cedula,telefono,ciudad,sueldo)
        self.sobretiempo=sobretiempo

    def GananciaObrero(self):
        print('Gana: {} gana ${} de su sueldo base: ${}'.format(self.nombre, self.sobretiempo, self.sueldo))


        


emple=EmpleadoObrero('brigner','098765431','1234567890',200,'vinces',5)
emple.GananciaObrero()