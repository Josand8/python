#Diccionario

dic={}
dic['item1']=1
dic['item2']=2
dic['item3']=3
dic['nombre']='luis'
print (dic)

a=int(input('Digite un numero: '))
if a==0:
    print('el valor es',a)
else:
    print('el valor es diferente de cero')

a=int(input('Digite un numero: '))
if a==0:
    print('el valor es',a)
elif a==1:
    print('el valor es diferente de cero y es: ',a)
elif a==2:
    print('el valor es 2')
else:
    print('es otro valor')

try:
    a=int(input('Digite un numero: '))
    b=int(input('Digite un numero: '))
    try:
        c=a/b
        print(c)
    except:
        print('la division entre cero no esta definida')
except:
    print('no digito un numero')
