from functools import reduce
def ordenes(rutinaContable):
    rc=rutinaContable
    op1=lambda val1=0:val1[1:]
    op2=lambda val1=0:list(map(lambda val2=0:val2[1]*val2[2],val1))
    op3=lambda val1=0:reduce(lambda acum=0,el=0:acum+el,val1)
    op4=lambda val1=0:round(val1+25000,2) if (val1<600000) else round(val1,2)
    op5=lambda val1=0:val1[0]
    res1=list(map(op1,rc))
    res2=list(map(op2,res1))
    res3=list(map(op3,res2))
    res4=list(map(op4,res3))
    et=list(map(op5,rc))
    f=(list(zip(et,res4)))
    
    resultado='------------------------ Inicio Registro diario ---------------------------------\n'
    for i in range(len(et)):
        resultado+='La factura {} tiene un total en pesos de {:,.2f}\n'.format(et[i],res4[i])
    resultado+='-------------------------- Fin Registro diario ----------------------------------'
    return print(resultado)
   
ordenes([[1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)],
[1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
[1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)],
[1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)]
])