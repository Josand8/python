def CDT(usuario:str,capital:int,tiempo:int):
    if tiempo>2:
        valor_int=(capital*0.03*tiempo)/12
        valor_total=valor_int+capital
    else:
        if tiempo<=2:
            valor_per=capital*0.02
            valor_total=capital-valor_per
            
    d=print("Para el usuario",str(usuario),"La cantidad de dinero a recibir, según el monto inicial",str(capital),"para un tiempo de",str(tiempo),"meses es:",str(valor_total))

a=input("Digite el usuario:")
b=int(input("Digite el capital:"))
c=int(input("Digite el tiempo:"))
r=CDT(a,b,c)
print(r)

