from turtle import forward, left, exitonclick

n = int(input('zadej pocet uhlu, zacnu kreslit spiralu'))
opakovani = int(input('kolikrat se ma zatocit?'))
delka_strany = 5

for spirala in range (1,opakovani):
    forward (delka_strany*1/spirala)
    left(180-(180*(1-2/n)))

exitonclick()
