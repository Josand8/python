#Faltan añadir funciones para terminarlo,
def create(tareas,identificador,tareaNueva):
    tareas[identificador]=tareaNueva
    return tareas
def estaElemento(identificador,tareas):
    conjuntoIdentificadores=set(tareas.keys())
    
    if identificador in conjuntoIdentificadores:
        return True
    else:
        return False

tareas={
         '01':{
                'descripcion':'ir a mercar',
                'estado':'pendiente',
                'tiempo':60
               },
         '02':{
                'descripcion':'Estudiar',
                'estado':'pendiente',
                'tiempo':180
               },
         '03':{
                'descripcion':'Hacer ejercicio',
                'estado':'pendiente',
                'tiempo':50
               },
}
n=0
while n!=5:
    print('-- Aplicación CRUD Tareas Pendientes ---')
    print('1. Adicionar Tarea')
    print('2. Consultar Tarea')
    print('3. Actualizar Tarea')
    print('4. Eliminar Tarea')
    print('5. Salir')
    try:
        n=int(input('Ingrese una opcion: '))
        if n==1:
            print('\n Adicionar Tarea \n')
            identificador=str(input('Ingrese Identificador de la tarea: '))
            descripcion=str(input('Ingrese descripcion de la tarea: '))
            estado=str(input('Ingrese el estado inicial de la tarea: '))
            tiempo=int(input('Ingrese el tiempo de la realizacion: '))
            
            tareaNueva={'descripcion':descripcion,'estado':estado,'tiempo':tiempo}
            
            tareas=create(tareas,identificador,tareaNueva)
        elif n==2:
            print('\n Consultar Tarea \n')
        elif n==3:
            print('\n ->Actualizar Tarea \n')
            identificador=str(input('Ingrese el identificador de la tarea a modificar: '))
            if estaElemento(identificador,tareas):
                nuevaDescripcion=str(input('Nueva descripcion'))
                if nuevaDescripcion:
                    tareas[identificador]['descripcion']=nuevaDescripcion
                nuevoestado=str(input('Nuevo estado'))
                if nuevoestado:
                    tareas[identificador]['estado']=nuevoestado
                    nuevotiempo=int(input('tiempo: '))
                if nuevotiempo:
                    tareas[identificador]['tiempo']=nuevotiempo
            else:
                print('No ha sido encontrada la tarea')
        elif n==4:
            print('\n Eliminar Tarea \n')
        elif n==5:
            print('\n Saliendo... \n')
        else:
            print('\n Seleccione una opcion valida \n')
        
    except:
        print('\n No digito un numero \n')