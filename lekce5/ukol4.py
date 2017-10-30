from random import randint

#0 = kamen, 1 = nuzky, 2 = papir

tah_cloveka = input('kámen, nůžky, nebo papír?     ')
tah_pocitace = randint(0,3)

while tah_cloveka != 'konec':
    if tah_cloveka == 'kámen':
        if tah_pocitace == 0:
            print('Plichta.')
        elif tah_pocitace == 1:
            print('Vyhrála jsi!')
        elif tah_pocitace == 2:
            print('Počítač vyhrál.')
    elif tah_cloveka == 'nůžky':
        if tah_pocitace == 0:
            print('Počítač vyhrál.')
        elif tah_pocitace == 1:
            print('Plichta.')
        elif tah_pocitace == 2:
            print('Vyhrála jsi!')
    elif tah_cloveka == 'papír':
        if tah_pocitace == 0:
            print('Vyhrála jsi!')
        elif tah_pocitace == 1:
            print('Počítač vyhrál.')
        elif tah_pocitace == 2:
            print('Plichta.')
    else:
        print('Nerozumím.')
    tah_cloveka = input('kámen, nůžky, nebo papír? Budeme hrát dokud neřekneš konec.    ')
