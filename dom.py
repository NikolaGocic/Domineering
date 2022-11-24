import string
import sys

matrica = []
igraPrvi = 0
naPotezu = 'X'
brojVrsta = 0
brojKolona = 0

#Implementirati funkcije koje obezbeđuju unos početnih parametara igre
def init():
    global matrica
    global brojVrsta
    global brojKolona

    print("Unesite broj vrsta:")
    brojVrsta = int(sys.stdin.readline())

    print("Unesite broj kolona:")
    brojKolona = int(sys.stdin.readline())

    matrica = [ [ " " for i in range(brojKolona) ] for j in range(brojVrsta) ]

#Implementirati funkcije koje obezbeđuju prikaz proizvoljnog stanja problema (igre)
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


#Realizovati funkcije koje proveravaju da li je potez valjan
# vrsta 1..N | kolona A..Z
def potezValjan(vrsta,kolona): 
    kol = ord(kolona)-65
    vrs = brojVrsta-vrsta
    
    if(naPotezu=='X'):
        if(vrs+1>=brojVrsta or kol>=brojKolona):
            return False

        if(matrica[vrs][kol]==' ' and matrica[vrs+1][kol]==' '):
            return True
        else:
            return False
    else:
        if(vrs>=brojVrsta or kol+1>=brojKolona):
            return False

        if(matrica[vrs][kol]==' ' and matrica[vrs][kol+1]==' '):
            return True
        else:
            return False

#Realizovati funkcije koje na osnovu zadatog poteza igrača menjaju trenutno stanjeproblema (igre) i prelaze u novo
def odigrajPotez(vrsta,kolona):
    global matrica
    global naPotezu

    if(potezValjan(vrsta,kolona)):
        kol = ord(kolona)-65
        vrs = brojVrsta-vrsta
        if(naPotezu=='X'):
            matrica[vrs][kol]='X'
            matrica[vrs+1][kol]='X'
            naPotezu='O'
        else:
            matrica[vrs][kol]='O'
            matrica[vrs][kol+1]='O'
            naPotezu='X'
        stampaj()
    else:
        print("Uneli ste nevalidni potez!")

#Napisati funkcije za proveru kraja igre
def krajIgre():
    
    if(naPotezu=='X'):
        vrs=0
        kol=0
        while(kol<brojKolona):
            while(vrs<brojVrsta-1):
                if(matrica[vrs][kol]==' ' and matrica[vrs+1][kol]==' '):
                    return False
                else:
                    vrs+=1
            kol+=1
    
    else:
        vrs=0
        kol=0
        while(vrs<brojVrsta):
            while(kol<brojKolona-1):
                if(matrica[vrs][kol]==' ' and matrica[vrs][kol+1]==' '):
                    return False
                else:
                    kol+=1
            vrs+=1
    
    return True #Kraj je igre zato sto nema slobodnih polja za igraca koj je na potezu


#Omogućiti izbor ko će igrati prvi (čovek ili računar)
def koIgraPrvi():
    global igraPrvi

    print("Ko igra prvi? (0-covek, 1-racunar):")
    igraPrvi = int(sys.stdin.readline())
    if(igraPrvi==0):
        print("Covek je prvi na potezu!")
    else:
        print("Racunar je prvi na potezu!")


def start():

    koIgraPrvi()

    init()

    stampaj()

    while True:
        if(krajIgre()):
            pobedio=""
            if(naPotezu=='X'):
                pobedio='O'
            else:
                pobedio='X'
            print("Kraj Igre, pobedio je igrac "+pobedio+"!!!")
            break


        print("\nIgrac "+naPotezu+" na potezu")
        print("Unesite vrstu (broj 1..N):")
        vrsta = int(sys.stdin.readline())
        if vrsta == -1:
            break
        print("Unesite kolonu (slovo A..Z):")
        kolona = sys.stdin.readline()
        odigrajPotez(vrsta,kolona[0])


start()