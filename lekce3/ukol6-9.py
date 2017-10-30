from turtle import left, forward, shape, exitonclick


PocetUhlu = int(input('Zadej pocet uhlu (n). Nakreslim ti n-uhelnik :)'))
DelkaStrany = float(input('Zadej delku strany'))

for n_uhelnik in range (PocetUhlu):
    forward(DelkaStrany)
    left(180-(180*(1-2/PocetUhlu)))

exitonclick()
