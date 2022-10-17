def semana(dia):
    if dia=="lunes":
        valor=1
    elif dia=="martes":
        valor=2
    elif dia=="miercoles":
        valor=3
    elif dia=="jueves":
        valor=4
    elif dia=="viernes":
        valor=5
    elif dia=="sabado":
        valor=6
    elif dia=="domingo":
        valor=7
    else:
        valor="Digite el dia en minuscula"
    return valor

dia2=input("Ingrese el dia de la semana: ")

print(semana(dia2))

def promedioNotas(Notas):
    sumatoria=0
    sumatoria+=Notas["Nota1"] #Esto es igual que: sumatoria=sumatoria+Notas
    sumatoria+=Notas["Nota2"]
    sumatoria+=Notas["Nota3"]
    sumatoria+=Notas["Nota4"]
    promedio=round(sumatoria/4,2)
    notamaxima=max(Notas["Nota1"],Notas["Nota2"],Notas["Nota3"],Notas["Nota4"])
    if notamaxima==Notas["Nota1"]:
        print("La nota maxima es: Nota1")
    elif notamaxima==Notas["Nota2"]:
        print("La nota maxima es: Nota2")
    elif notamaxima==Notas["Nota3"]:
        print("La nota maxima es: Nota3")
    elif notamaxima==Notas["Nota4"]:
        print("La nota maxima es: Nota4")
    resultado={"Estudiante: ":Notas["Estudiante"],"Codigo":Notas["Codigo"],"promedio":promedio,"notamaxima":notamaxima}
    return resultado
dicNotas={}
dicNotas["Nota1"]=float(input("Digite la nota 1: "))
dicNotas["Nota2"]=float(input("Digite la nota 2: "))
dicNotas["Nota3"]=float(input("Digite la nota 3: "))
dicNotas["Nota4"]=float(input("Digite la nota 4: "))
dicNotas["Estudiante"]=input("Ingrese el nombre: ")
dicNotas["Codigo"]=int(input("Ingrese el codigo del estudiante: "))
print(promedioNotas(dicNotas))