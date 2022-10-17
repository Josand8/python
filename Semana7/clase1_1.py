#Experimentando con interfaces graficas

import turtle
tortuga=turtle

tortuga.setup(800,600,0,0)
tortuga.screensize(800,600)
tortuga.title('Nombre ventana')

tortuga.shape('turtle')

#Forward: avanzar, Backward: retroceder, Left: girar a la izquierda, Right: girar a la derecha
tortuga.color('green','yellow')
tortuga.bgcolor('black')
tortuga.hideturtle()

# lados=int(input('Indique el numero de lados de la figura: '))
# move=int(input('Indique que distancia debe moverse la tortuga: '))

# for i in range(lados):
#     tortuga.left(360/lados)
#     tortuga.forward(move)


# for i in range(4):
#     tortuga.forward(100)
#     tortuga.left(90)
    
#goto(x, y): ir de x a y, 
tortuga.penup()

def punto(x,y):
    tortuga.goto(x,y)
    tortuga.dot(10,'red')
    
def cuadro(x,y):
    tortuga.fillcolor('green')
    tortuga.begin_fill()
    tortuga.goto(x-5,y-5)
    tortuga.pendown()
    tortuga.goto(x+5,y-5)
    tortuga.goto(x+5,y+5)
    tortuga.goto(x-5,y+5)
    tortuga.goto(x-5,y-5)
    tortuga.penup
    tortuga.end_fill
    
tortuga.onscreenclick(cuadro,3)
tortuga.onscreenclick(punto,1)
tortuga.write('Hola mundo',True, 'right', ('arial', 20,'bold italic'))
tortuga.write('Otra cosa')
nombre=tortuga.textinput('Titulo','Cual es su nombre?')
edad=tortuga.numinput('Edad','Cual es su edad' , 18,0,100)
tortuga.mainloop()

#tortuga.Screen().exitonclick()

