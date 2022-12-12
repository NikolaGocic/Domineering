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
def stampaj(matrica):
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

    if(vrs<0 or kol<0):
        return False
    
    if(naPotezu=='X'):

        if((vrs+1)>=brojVrsta or kol>=brojKolona):
            return False

        if(matrica[vrs][kol]==' ' and matrica[vrs+1][kol]==' '):
            return True
        else:
            return False
    else:
        if(vrs>=brojVrsta or (kol+1)>=brojKolona):
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
        krajIgre()
        stampaj(matrica)
    else:
        print("Uneli ste nevalidni potez!")

#Napisati funkcije za proveru kraja igre
def krajIgre():
    if(naPotezu=='X'):
        for i in range(0,brojVrsta-1):
            for j in range(0,brojKolona):
                if(matrica[i][j]==' ' and matrica[i+1][j]==' '):
                    return False
    else:
        for i in range(0,brojVrsta):
            for j in range(0,brojKolona-1):
                if(matrica[i][j]==' ' and matrica[i][j+1]==' '):
                    return False
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

#Realizovati funkcije koje na osnovu zadatog igrača na potezu i zadatog stanje igre formiraju sva moguća stanje igre (sve moguće table)
def svaMogucaStanja():
    if(naPotezu=='X'):
        for i in range(0,brojVrsta-1):
            for j in range(0,brojKolona):
                if(matrica[i][j]==' ' and matrica[i+1][j]==' '):
                    matrica[i][j] = 'X'
                    matrica[i+1][j] = 'X'
                    stampaj(matrica)
                    matrica[i][j] = ' '
                    matrica[i+1][j] = ' '

    else:
        for i in range(0,brojVrsta):
            for j in range(0,brojKolona-1):
                if(matrica[i][j]==' ' and matrica[i][j+1]==' '):
                    matrica[i][j] = 'O'
                    matrica[i][j+1] = 'O'
                    stampaj(matrica)
                    matrica[i][j] = ' '
                    matrica[i][j+1] = ' '

def start():
    global kraj
    global matrica

    koIgraPrvi()

    init()

    stampaj(matrica)

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
        print("Unesite vrstu (broj 1..N)(-1 prekid igre, -2 stampanje svih mogucih stanja):")
        vrsta = int(sys.stdin.readline())
        if vrsta == -1:
            break
        else:
            if vrsta == -2:
                svaMogucaStanja()
                print("Unesite vrstu (broj 1..N)(-1 prekid igre, -2 stampanje svih mogucih stanja):")
                vrsta = int(sys.stdin.readline())
                print("Unesite kolonu (slovo A..Z):")
                kolona = sys.stdin.readline()
                odigrajPotez(vrsta,kolona[0])
            else:
                print("Unesite kolonu (slovo A..Z):")
                kolona = sys.stdin.readline()
                odigrajPotez(vrsta,kolona[0])
            
start()