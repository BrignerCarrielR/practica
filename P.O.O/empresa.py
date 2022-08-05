class Empresa:
    def __init__(self,ruc='0960285305',nombre='Somos Mas',tel='0962164367',dir='Duran',correo='gta@gmail.com'):
        self.ruc=ruc
        self.razonsocial=nombre
        self.tel=tel
        self.dir=dir
        self.correo=correo

if __name__ == '__main__':
    emp1=Empresa()
    emp2=Empresa('1234567890','Union hace la fuerza','0987654321','Milagros','abc@gmail.com')
    print(emp1.ruc,emp1.razonsocial)
    print(emp2.ruc,emp2.razonsocial)