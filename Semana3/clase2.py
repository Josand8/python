semana={'lunes':1,
        'martes':2,
        'miercoles':3,
        'jueves':4,}
for i,j in semana.items():
    if i=='miercoles':
        print(i)

for i in range(1,100):        #for anidado
    div=0
    for j in range(1,i+1):
        if (i%j)==0:
            div=div+1
    if div==2:
        print("el numero ",i," es primo")
        
        
nombres=[]
edad=[]
for x in range(5):
    a=input('Digite un nombre: ')
    b=int(input('Digite la edad: '))
    nombres.append(a)
    edad.append(b)
    
for x in range(0,5):
    if edad[x]>=18:
        print('Estas personas son mayores de edad',nombres[x])

print(nombres,edad)


padres=[]
hijos=[]
for i in range(3):
    a=input('ingrese el nombre del padre:')
    b=input('ingrese el nombre de la madre: ')
    padres.append([a,b])
    c=int(input('Ingrese la cantidad de hijos: '))
    hijos.append([])
    for j in range(c):
        d=input('Ingrese el nombre del hijo: ')
        hijos[i].append(d)

for i in range(3):
    print(padres[i])
    for j in range(len(hijos[i])):
        print(hijos[i][j])
for i in range(3):
    print('{} tiene {} hijos'.format(padres[i][0],len(hijos[i])))
print(padres,hijos)