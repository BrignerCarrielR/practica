from datetime import date
from empresa import Empresa
from cliente import ClienteCorporativo
class Articulo:
    _secuencia=0
    def __init__(self,des,pre,sto):
        Articulo._secuencia +=1
        self.codigo= Articulo._secuencia
        self.descripcion=des
        self.precio=pre
        self.stock=sto
    def mostrarArticulo(self):
        print(self.codigo,self.descripcion)

class DetalleVenta:
    _linea=0
    def __init__(self,producto,cantidad):
        DetalleVenta._linea+=1
        self.linea=DetalleVenta._linea
        self.articulo=producto
        self.precio=producto.precio
        self.cantidad=cantidad

class Venta:
    _factura=0
    _iva=0.12
    def __init__(self,cliente) -> None:
        Venta._factura=Venta._factura+1
        self.factura='F'+str(Venta._factura)
        self.fecha=date.today()
        self.cliente=cliente
        self.subtotal=0
        self.iva=0
        self.total=0
        self.detalleVenta=[]

    def agregarDatalle(self,articulo,cantidad):
        detalle=DetalleVenta(articulo,cantidad)
        self.subtotal += round(detalle.precio*detalle.cantidad,2)
        self.iva=round(self.subtotal*Venta._iva,2)
        self.total=round(self.subtotal+self.iva,2)
        self.detalleVenta.append(detalle)

    def mostrarVenta(self,empNombre,empRuc):
        print('Empresa: {:17} Ruc:{}'.format(empNombre,empRuc))
        print('Factura#:{:13} Fecha:{}'.format(self.factura,self.fecha))
        self.cliente.mostrarCliente()
        print('Linea Articulo       Precio Cantidad Subtotal')
        for det in self.detalleVenta:
            print('{:5} {:15} {} {:6} {:7}'.format(det.linea,det.articulo.descripcion,det.precio,det.cantidad,det.precio*det.cantidad))
        print('*'*23,'Subtotal=> ',self.subtotal)
        print('*'*26,'Iva=> ',self.iva)
        print('*'*23,'Total=> ',self.total)



empresa=Empresa()
cliente1=ClienteCorporativo('0912345678','Brigner','0962164367','abc@g,ail.com',False)
venta=Venta(cliente1) 
art1=Articulo('Aceite',3,100)
art2=Articulo('Coca cola',1,200)
venta.agregarDatalle(art1,3)
venta.agregarDatalle(art2,2)
venta.mostrarVenta(empresa.razonsocial,empresa.ruc)
