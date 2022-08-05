from cliente import Cliente
from empresa import Empresa
print('Datos de la Venta')
emp=Empresa('12345','Somos Mas','092321341','Duran','db@gmail.com')
print("Empresa: {} - {}".format(emp.ruc,emp.razonsocial))
print('Factura# XXX')
cli1 = Cliente('0960285305','Brigner','0962164367','bcarriel@unemi.edu.ec')
cli1.mostrarCliente()
