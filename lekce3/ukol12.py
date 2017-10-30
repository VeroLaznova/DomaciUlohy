from turtle import forward, left, exitonclick, right



opakovani = int(input('Nakreslim ti spiralu, kolikrat se ma zatocit?'))
delka_strany = 0
x=5

for i in range (opakovani):
    for i in range (18):
        right(10)
        forward (delka_strany)
    delka_strany += x

exitonclick()
