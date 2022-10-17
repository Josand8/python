def notaquices(codigo: str, nota: int, nota1: int, nota2: int, nota3: int, nota4: int) -> str:
    promedioMaximo=5
    notaMaxima=100
    notatotalsinmenor=4
    calcular=0
    if(nota<nota1 and nota<nota2 and nota<nota3 and nota<nota4):
        calcular=(nota1+nota2+nota3+nota4)/notatotalsinmenor
        calcular=(calcular*5)/100
    elif (nota1<=nota and nota1<=nota2 and nota1<=nota3 and nota1<=nota4):
        calcular=(nota+nota2+nota3+nota4)/notatotalsinmenor
        calcular=(calcular*5)/100
    elif (nota2<=nota and nota2<=nota1 and nota2<=nota3 and nota2<=nota4):
        calcular=(nota+nota1+nota3+nota4)/notatotalsinmenor
        calcular=(calcular*5)/100
    elif (nota3<=nota and nota3<=nota1 and nota3<=nota2 and nota3<=nota4):
        calcular=(nota+nota1+nota2+nota4)/notatotalsinmenor
        calcular=(calcular*5)/100
    elif (nota4<=nota and nota4<=nota1 and nota4<=nota2 and nota4<=nota3):
        calcular=(nota+nota1+nota2+nota3)/notatotalsinmenor
        calcular=(calcular*5)/100
    calcular=round(calcular,2)
    return f'El promedio ajustado del estudiante: {codigo} Es:{calcular}'