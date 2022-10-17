def AutoPartes(ventas: list):
    resultado={}
    for i in range(len(ventas)):
        resultado[i]=[ventas[i]]
    return resultado
def consultaRegistro(ventas, idProducto):
    res={}
    res2=''
    for i in range(len(ventas)):
        if ventas[i][0][0]==idProducto:
            res[i]=ventas[i]
    if (len(res))==0:
        res2='No hay registro de venta de ese producto'
    for i in res:
        res2+='Producto consultado : {}  Descripción  {}  #Parte  {}  Cantidad vendida  {}  Stock  {}  Comprador {}  Documento  {}  Fecha Venta  {}\n'.format(res[i][0][0],res[i][0][1],res[i][0][2],res[i][0][3],res[i][0][4],res[i][0][5],res[i][0][6],res[i][0][7])
    return print(res2)

print(consultaRegistro(AutoPartes([
(2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
(2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
(2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
(3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
(9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]), 2010))