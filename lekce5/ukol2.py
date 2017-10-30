from turtle import forward, left, shape, exitonclick
from math import sqrt

odpoved = input('Nakreslim ti domecek, chces? Odpovez ano nebo ne.')

while odpoved.lower() == 'ano':
    strana = int(input('Zadej delku strany ctverce. Nakreslim ti domecek!'))
    shape('turtle')
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
    odpoved = input('Nakreslim ti domecek, chces? Odpovez ano nebo ne.')
