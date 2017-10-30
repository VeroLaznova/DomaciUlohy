from turtle import forward, left, shape, exitonclick
from math import sqrt



strana = int(input('Zadej delku strany ctverce. Nakreslim ti domecek!'))
pocetdomu = int(input('Zadej pocet domu a bude z toho vesnice'))

shape('turtle')

for vesnice in range (pocetdomu):
    for ctverec in range (4):
        forward(strana)
        left (90)

    left(45)
    forward(sqrt(2)*strana)
    left(90)
    forward(sqrt(2)*strana/2)
    left(90)
    forward(sqrt(2)*strana/2)
    left(90)
    forward(sqrt(2)*strana)
    left(45)
    forward(strana/2)

exitonclick()
