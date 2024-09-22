from turtle import *
import turtle;
import math;
import random;
import colorcet;

# Configuración inicial
turtle.tracer(2)
turtle.bgcolor('black')
turtle.pensize(2)
turtle.color('yellow')

# Dibujar puntos blancos aleatorios
for _ in range(100):
    x = random.randint(-turtle.window_width() // 2, turtle.window_width() // 2)
    y = random.randint(-turtle.window_height() // 2, turtle.window_height() // 2)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(5, 'white')

# Posición inicial para el primer patrón
turtle.penup()
x_inicial = 0  # Cambia este valor si lo deseas
y_inicial = 0  # Cambia este valor si lo deseas
turtle.goto(x_inicial, y_inicial)
turtle.pendown()

# Dibujo del primer patrón
h = 0
for i in range(120):
    h += 0.006
    turtle.lt(179)
    turtle.backward(i * 0.1)
    turtle.circle(i * 0.3, 120)
    turtle.rt(14)
    turtle.forward(i * 0.1)
    turtle.circle(i * 0.3, 120)

# Dibujo del segundo patrón desde la misma posición final del primero
turtle.shape('turtle')
turtle.pencolor('orangered')
turtle.fillcolor('orange')
phi = 137.508 * (math.pi / 180.0)

# Guarda la posición final del primer patrón
final_x = turtle.xcor()
final_y = turtle.ycor()

turtle.penup()
turtle.goto(final_x, final_y)  # Mueve a la posición final del primer patrón
turtle.pendown()

for i in range(300):
    r = 4 * math.sqrt(i)
    theta = i * phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(i * 137.508)
    turtle.pendown()
    turtle.stamp()

turtle.done()
