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
    if(vrsta<0 or kolona<0):
        return False
    
    if(naPotezu=='X'):

        if((vrsta+1)>=brojVrsta or kolona>=brojKolona):
            return False

        if(matrica[vrsta][kolona]==' ' and matrica[vrsta+1][kolona]==' '):
            return True
        else:
            return False
    else:
        if(vrsta>=brojVrsta or (kolona+1)>=brojKolona):
            return False

        if(matrica[vrsta][kolona]==' ' and matrica[vrsta][kolona+1]==' '):
            return True
        else:
            return False

#Realizovati funkcije koje na osnovu zadatog poteza igrača menjaju trenutno stanjeproblema (igre) i prelaze u novo
def odigrajPotez(vrsta,kolona):
    global matrica
    global naPotezu

    if(potezValjan(vrsta,kolona)):
        if(naPotezu=='X'):
            matrica[vrsta][kolona]='X'
            matrica[vrsta+1][kolona]='X'
            naPotezu='O'
        else:
            matrica[vrsta][kolona]='O'
            matrica[vrsta][kolona+1]='O'
            naPotezu='X'
        stampaj(matrica)
    else:
        print("Uneli ste nevalidni potez!")

#Napisati funkcije za proveru kraja igre
def krajIgre(trenutno_stanje,na_potezu):
    if(na_potezu=='X'):
        for i in range(0,brojVrsta-1):
            for j in range(0,brojKolona):
                if(trenutno_stanje[i][j]==' ' and trenutno_stanje[i+1][j]==' '):
                    return False
    else:
        for i in range(0,brojVrsta):
            for j in range(0,brojKolona-1):
                if(trenutno_stanje[i][j]==' ' and trenutno_stanje[i][j+1]==' '):
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

#Vraca listu validnih poteza za X
def validni_potezi_X(stanje_matrice):
    potezi = []

    for i in range(0,brojVrsta-1):
        for j in range(0,brojKolona):
            if(stanje_matrice[i][j]==' ' and stanje_matrice[i+1][j]==' '):
                potezi.append([i,j])
    
    return potezi

#Vraca list validnih poteza za O
def valdini_potezi_O(stanje_matrice):
    potezi = []

    for i in range(0,brojVrsta):
        for j in range(0,brojKolona-1):
            if(stanje_matrice[i][j]==' ' and stanje_matrice[i][j+1]==' '):
                potezi.append([i,j])

    return potezi

#Vraca listu validnih poteza za trenutnog igraca
def validniPotezi(stanje_matrice):
    if naPotezu == 'X':
        return validni_potezi_X(stanje_matrice)
    else:
        return valdini_potezi_O(stanje_matrice)

#Vraca razliku broj validnih poteza za X i O
#Pozitivna vrednost - prednost za X
#Negativna vrednost - prednost za O
#Nula - nema prednosti
def heuristika(trenutno_stanje):
    validni_X = validni_potezi_X(trenutno_stanje)
    validni_O = valdini_potezi_O(trenutno_stanje)

    return len(validni_X) - len(validni_O)

def sledeceStanje(stanje,vrsta,kolona,igrac):
  
    if(igrac=='X'):
        stanje[vrsta][kolona]='X'
        stanje[vrsta+1][kolona]='X'
    else:
        stanje[vrsta][kolona]='O'
        stanje[vrsta][kolona+1]='O'

    return stanje

def minimax(pocetno_stanje, dubina: int, alpha: int, beta: int):

    najbolji_potez = None

    kraj = krajIgre(pocetno_stanje,naPotezu)
    if kraj==True or dubina == 0:
        return heuristika(pocetno_stanje), None

    if naPotezu=='X':
        najbolja_vrednost = -2000
        for potez in validni_potezi_X(pocetno_stanje):
            sledece_stanje = sledeceStanje(pocetno_stanje,potez[0], potez[1],'X')
            vrednost, _ = minimax(sledece_stanje, dubina - 1, alpha, beta)
            if vrednost > najbolja_vrednost:
                najbolja_vrednost = vrednost
                najbolji_potez = potez

            alpha = max(alpha, najbolja_vrednost)
            if beta <= alpha:
                break
    else:
        najbolja_vrednost = 2000
        for potez in valdini_potezi_O(pocetno_stanje):
            sledece_stanje = sledeceStanje(pocetno_stanje,potez[0], potez[1],'O')
            vrednost, _ = minimax(sledece_stanje, dubina - 1, alpha, beta)
            if vrednost < najbolja_vrednost:
                najbolja_vrednost = vrednost
                najbolji_potez = potez
            
            beta = min(beta, najbolja_vrednost)
            if beta <= alpha:
                break

    return najbolja_vrednost, najbolji_potez


def start():
    global kraj
    global matrica

    koIgraPrvi()

    init()

    stampaj(matrica)

    while True:
        if(krajIgre(matrica,naPotezu)):
            pobedio=""
            if(naPotezu=='X'):
                pobedio='O'
            else:
                pobedio='X'
            stampaj(matrica)
            print("Kraj Igre, pobedio je igrac "+pobedio+"!!!")
            break


        print("\nIgrac "+naPotezu+" na potezu")
        pocetno_stanje=[row[:] for row in matrica]
        vrednost, potez = minimax(pocetno_stanje, 3, -2000, +2000)
        if (igraPrvi==1 and naPotezu=='X') or (igraPrvi==0 and naPotezu=='O'):
            odigrajPotez(potez[0],potez[1])
        else:    
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
                    kol = ord(kolona[0])-65
                    vrs = brojVrsta-vrsta
                    odigrajPotez(vrs,kol)
                else:
                    print("Unesite kolonu (slovo A..Z):")
                    kolona = sys.stdin.readline()
                    kol = ord(kolona[0])-65
                    vrs = brojVrsta-vrsta
                    odigrajPotez(vrs,kol)
            
start()