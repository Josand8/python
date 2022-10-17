def cliente(informacion:dict):
    if informacion['edad']>18:
        atraccion='X-Treme'
        apto=True
        if informacion['primer_ingreso']==True:
            valor_bol=20000*0.95
        else:
            valor_bol=20000
    elif informacion['edad']>=15:
        atraccion='Carros chocones'
        apto=True
        if informacion['primer_ingreso']==True:
            valor_bol=5000*0.93
        else:
            valor_bol=5000
    elif informacion['edad']>=7:
        atraccion='Sillas voladoras'
        apto=True
        if informacion['primer_ingreso']==True:
            valor_bol=10000*0.95
        else:
            valor_bol=10000
    elif informacion['edad']<7:
        atraccion='N/A'
        apto=False
        if informacion['primer_ingreso']==True:
            valor_bol='N/A'
    resultado={'nombre':informacion['nombre'],'edad':informacion['edad'],'atraccion':atraccion,'apto':apto,'primer_ingreso':informacion['primer_ingreso'],'total_boleta':valor_bol}
    return resultado

inf={}
inf['id_cliente']=int(input('Digite el id: '))
inf['nombre']=input('Digite el nombre: ')
inf['edad']=int(input('Digite la edad: '))
inf['primer_ingreso']=bool(input('Es primer ingreso(1 si, '' no): '))
a=cliente(inf)
print(a)