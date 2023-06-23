import turtle as t
import time  
import random as r

dellay = 0.1
vel = 0
puntos = 0
record = 0

#Pantalla
wn = t.Screen()
wn.title('Snake')
wn.setup(width=600, height=600)
#wn.bgcolor('black')
wn.tracer(0)

#Marcador
score = t.Turtle()
score.speed(0)
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Puntuación: {}".format(puntos), align="center", font=("Courier", 24, "normal"))

#Cabeza de la serpiente
head = t.Turtle()
head.speed(0)
head.shape('square')
head.penup()
head.goto(0,0)
head.direction = 'stop'

#Cuerpo de la serpiente
cuerpo = []

#Comida
food = t.Turtle()
food.speed(vel)
food.shape('circle')
food.color('red')
food.penup()
x = r.randint(-280,280)
y = r.randint(-280,280)
food.goto(x,y)
food.goto(x,y)


#Movimiento

def arriba():
    head.direction = "up"

def abajo():
    head.direction = "down"

def izquierda():
    head.direction = "left"

def derecha():
    head.direction = "right"

def movimiento():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

#Mapeo de teclado

wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

#Bucle
while(True):
    wn.update()

    #Colisiones mapa
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        [i.hideturtle() for i in cuerpo]
        cuerpo*0
        cuerpo.clear()
        puntos = 0
        score.clear()
        score.write("Puntuación: {}".format(puntos), align="center", font=("Courier", 24, "normal"))

        

    if head.distance(food) < 20:
        x = r.randint(-280,280)
        y = r.randint(-280,280)
        food.goto(x,y)
        puntos+=10
        score.clear()
        score.write("Puntuación: {}".format(puntos), align="center", font=("Courier", 24, "normal"))

        

        nuevo_cuerpo = t.Turtle()
        nuevo_cuerpo.speed(0)
        nuevo_cuerpo.shape('square')
        nuevo_cuerpo.color('green')
        nuevo_cuerpo.penup()
        cuerpo.append(nuevo_cuerpo)
        pass

    totalCuerpo = len(cuerpo)
    for i in range(totalCuerpo -1,0,-1):
        x=cuerpo[i-1].xcor()
        y=cuerpo[i-1].ycor()
        cuerpo[i].goto(x,y)

    if totalCuerpo > 0:
        x = head.xcor()
        y = head.ycor()
        cuerpo[0].goto(x,y)

    movimiento()

    #Colisiones con el cuerpo

    for i in cuerpo:
        if i.distance(head) < 15:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            [i.hideturtle() for i in cuerpo]
            cuerpo*0
            cuerpo.clear()
            puntos = 0
            score.clear()
            score.write("Puntuación: {}".format(puntos), align="center", font=("Courier", 24, "normal"))
            #log()  
            
    time.sleep(dellay)




#Indica el final del bucle, sin esta función, la ventana se cerrará.    
t.done() 
