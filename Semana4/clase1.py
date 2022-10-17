#Creando funciones
def suma(val1:0,val2:0):
    return val1+val2

def operacion(funcion,val1=0,val2=0):
    return funcion(val1,val2)
funcion_suma=suma
resultado=operacion(funcion_suma,10,200)
print(resultado)

def crear_funcion(operador):
    if operador == '*':
        def multiplicacion(val1=1,val2=1):
            return val1*val2
        return multiplicacion
def operacion(funcion,val1=1,val2=1):
    return funcion(val1,val2)

multiplicacion=crear_funcion('*')
resultado=operacion(multiplicacion,2,10)
print(resultado)

# si las conbinamos quedaria

def crear_funcion(operador):
    if operador == '+':
        def suma(val1=1,val2=1):
            return val1+val2
        return suma
    if operador == '*':
        def multiplicacion(val1=1,val2=1):
            return val1*val2
        return multiplicacion