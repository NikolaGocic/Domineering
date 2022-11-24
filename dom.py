
import string
import sys

matrica = []

def init():
    global matrica
    matrica = [ [ " " for i in range(brojKolona) ] for j in range(brojVrsta) ]

def stampaj():
    top(brojKolona)

    for x in range(0,brojVrsta):
        print(str(brojVrsta-x)+"||",end='')
        for num in range(0,brojKolona):
            print(matrica[x][num]+'|',end='')
        print("|"+str(brojVrsta-x))
        
    bottom(brojKolona)    


def top(brojKolona):
    print('  ',end='')
    for num in range(0,brojKolona):
        print(' '+string.ascii_uppercase[num],end='')
    print('')
    print('  ',end='')
    for num in range(0,brojKolona):
        print(' =',end='')
    print('')

def bottom(brojKolona):
    print('  ',end='')
    for num in range(0,brojKolona):
        print(' =',end='')
    print('')
    print('  ',end='')
    for num in range(0,brojKolona):
        print(' '+string.ascii_uppercase[num],end='')
    print('')


print("Unesite broj vrsta:")
brojVrsta = int(sys.stdin.readline())
print("Unesite broj kolona:")
brojKolona = int(sys.stdin.readline())
init()
stampaj()

while True:
    vrsta = int(sys.stdin.readline())
    if vrsta == -1:
        break
    kolona = int(sys.stdin.readline())
    znak = sys.stdin.readline()
    matrica[vrsta][kolona]=znak[0]
    stampaj()

