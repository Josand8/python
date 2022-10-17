num=int(input("Digite el numero: "))
if num<0:
    print("El numero es negativo")
if num>0:
    print("El numero es positivo")
if num==0:
    print("El numero es nulo")
    

num2=int(input("Digite el numero: "))
if num2<0:
    print("El numero es negativo")
else:
    if num2>0:
        print("El numero es positivo")
    else:
        print("El numero es nulo")
print("Finalizo")


c=int(input("Digite el numero:"))
if c<0:
    c=c*(-1)
if c>=1 and c<=9:
    print("El numero tiene un digito")
else:
    if c>=10 and c<=99:
        print("El numero tiene dos cifras")
    else:
        if c>=100 and c<=999:
            print("El numero tiene 3 cifras")
        else:
            if c>=1000 and c<=9999:
               print("El numero tiene 4 cifras")
            else:
                 print("El numero es mayor a 4 cifras")
                 

d=int(input("Ingrese el numero: "))
if d<0:
    d=d*(-1)
if d>=0 and d<=9:
    print("El numero tiene un digito")
elif d>=10 and d<=99:
    print("El numero tiene dos cifras")
elif d>=100 and d<=999:
    print("El numero tiene tres cifras")
elif d>=1000 and d<=9999:
    print("El numero tiene cuatro cifras")
else:
    print("el numero tiene mas de cuatro cifras") 

