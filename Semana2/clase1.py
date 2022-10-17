#calcule el area de un triangulo que tiene base 2 y altura 8, A=(b*h)/2
#y calcule la hipotenusa (h**2+b**2)**0.5

base=2
altura=8
area=(base*altura)/2
hipotenusa=(altura**2+base**2)**0.5
print("El area es:",area)
print("La hipotenusa es:",hipotenusa)

import funcion
c=funcion.suma(2,5)
print("la suma es:",c)

import funcion
name=input("ingrese su nombre:")
funcion.bienvenida(name)
a=float(input("Ingrese un numero:"))
b=int(input("Ingrese un numero"))
c=funcion.suma(a,b)
print("la suma es:",c)

numeros=(25,26,25,24)
maximo=max(numeros)
minimo=min(numeros)
suma=sum(numeros)
print("El numero mayor es:",maximo)
print("El numero menor es:",minimo)
print("La suma de los numero es es:",suma)

from funcion import raiz

x1=float(input("ingrese el numero que desea sacar raiz: "))
x2=float(input("ingrese la raiz: "))
y=raiz(x1,x2)
print("la raiz es: ", y)

x3=float(input("ingrese el numero que desea sacar raiz: "))
x4=float(input("ingrese la raiz: "))
y=raiz(x3,x4)
print("la raiz es: ", y)

from funcion import sumamultiplicacion

x5=float(input("ingrese el primer numero:"))
x6=float(input("ingrese el numero que desea sumar "))
x7=float(input("ingrese el numero que desea multiplicar "))
y1=sumamultiplicacion(x5,x6,x7)
print("El resultado es: ",y1)

from funcion import cdt

cantidad=int(input("Ingrese la cantidad de dinero: "))
