class acudientes:
    
    def __init__(self):
        self.__acudiente1=input('Nombre acudiente')
        
    def getacudiente(self):
        return (self.__acudiente1)

class Estudiante:
    
    def __init__(self):
        self.nombre=input('Digite el nombre: ')
        self.codigo=input('Digite el codigo: ')
        self.nota=float(input('Digite la nota: '))
        self.acudiente=acudientes()
        
    def info_est(self):
        print('---------------------- Informacion Estudiante --------------------')
        print('Codigo: ' ,self.codigo)
        print('Nombre: ' ,self.nombre)
        print('Nota: ' ,self.nota)
        print('Acudiente: ' ,self.acudiente.__acudiente1)
        print('----------------------------- Fin Informacion ------------------------')