class Email:
    def __init__(self):
        self.enviado= False
    def enviar_correo(self):
        self.enviado= True

mi_correo= Email()
print(mi_correo.enviado)
mi_correo.enviar_correo()
print(mi_correo.enviado)

class Pokemon:
    def __init__(self,nombre,tipo):
        self.nombre= nombre
        self.tipo= tipo

    def descripcion(self):
        return '{} es un pokemon de tipo: {}'.format(self.nombre,self.tipo)
class pikachu (Pokemon):
    def ataque(self,tipoatraque):
        return '{} tipo de ataque: {}'.format(self.nombre,tipoatraque)
class charmander(Pokemon):
    def ataque(self,tipoatraque):
        return '{} tipo de ataque: {}'.format(self.nombre,tipoatraque)


nuevo_pokemon= pikachu('Brigner','Fuego')
print(nuevo_pokemon.descripcion())
print(nuevo_pokemon.ataque('Nieve'))

class Calculadora:
    def __init__(self, numero):
        self.n=numero
        self,datos = [0 for i in range(numero)]


