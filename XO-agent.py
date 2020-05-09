class Game:
    def __init__(self):
        self.inicijalizuj_igru()

        #inicijalizujemo igru napocetno stanje
    def inicijalizuj_igru(self):
        self.trenutno_stanje = [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']
        ]

        self.na_potezu = 'X'

        #da uporedimo brzine alfa beta i minimaxa algortima
        self.broj_poziva = 0

    def nacrtaj_tablu(self):
        for i in range(3):
            for j in range(3):
                print('{}|'.format(self.trenutno_stanje[i][j]),end=" ")
            print()
        print()

    def ispitaj_koord(self,px,py):
        if px < 0 or px > 2 or py <0 or py >2:
            return False
        elif self.trenutno_stanje[px][py] != '.':
            return False
        else:
            return True

    #ispitujemo da li smo dosli do kraja igre
    def kraj(self):
        #ispitujemo po vertikali
        for i in range(0,3):
            if (self.trenutno_stanje[0][i] != '.' and
            self.trenutno_stanje[0][i] == self.trenutno_stanje[1][i]
            and self.trenutno_stanje[1][i] == self.trenutno_stanje[2][i]):
                return self.trenutno_stanje[0][i]
        #ispitiujemo po horizontali
        for i in range(0,3):
            if(self.trenutno_stanje[i][0] != '.' and
            self.trenutno_stanje[i][0] == self.trenutno_stanje[i][1]
            and self.trenutno_stanje[i][1] == self.trenutno_stanje[i][2]):
                return self.trenutno_stanje[i][0]

        #ispitujemo po glavnoj dijagonali
        if (self.trenutno_stanje[0][0] != '.'
            and self.trenutno_stanje[0][0] == self.trenutno_stanje[1][1]
            and self.trenutno_stanje[1][1] == self.trenutno_stanje[2][2]):
            return self.trenutno_stanje[0][0]

        #ispitujemo po sporendnoj dijagonali
        sporedna = []
        sporedna.append(self.trenutno_stanje[0][2])
        sporedna.append(self.trenutno_stanje[1][1])
        sporedna.append(self.trenutno_stanje[2][0])
        if sporedna == ['X','X','X']:
            return 'X'
        elif sporedna == ['O','O','O']:
            return 'O'

        #ispitujemo da li je popunjena cela tabela
        for i in range(0,3):
            for j in range(0,3):
                if self.trenutno_stanje[i][j] == '.':
                    return None

        #Nereseno
        return '.'

    #igrac Max je 'O'
    def Max(self):
        self.broj_poziva+=1
        #moguce vrednosti su -1,0,1
        maxv = -2
        px = None
        py = None

        rezultat = self.kraj()
        if rezultat == 'X':
            return (-1,None,None)
        elif rezultat == 'O':
            return (1,None,None)
        elif rezultat == '.':
            return (0,None,None)

        for i in range(0,3):
            for j in range(0,3):
                if self.trenutno_stanje[i][j] == '.':
                    self.trenutno_stanje[i][j] = 'O'
                    m = self.Min()
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j

                        #vracamo polje ponovo na prazno
                    self.trenutno_stanje[i][j] = '.'
        return (maxv,px,py)

    def Min(self):

        self.broj_poziva +=1

        minv = 2
        rezultat = self.kraj()

        if rezultat == 'X':
            return (-1)
        elif rezultat == 'O':
            return (1)
        elif rezultat == '.':
            return (0)

        for i in range(0,3):
            for j in range(0,3):
                if self.trenutno_stanje[i][j] == '.':
                    self.trenutno_stanje[i][j] = 'X'
                    (m,max_i,max_j) = self.Max()
                    if m < minv:
                        minv = m

                    self.trenutno_stanje[i][j] ='.'


        return minv

    def play(self):

        while True:
            self.nacrtaj_tablu();

            self.rezultat = self.kraj()

            if self.rezultat != None:
                if self.rezultat == 'X':
                    print("Pobedio je X")
                elif self.rezultat == 'O':
                    print("Pobedio je O")
                elif self.rezultat == '.':
                    print("Nereseno je")

                print("Broj poziva: ",self.broj_poziva)
                return

        #ako je na potezu igrac X
            if self.na_potezu == 'X':
                while True:
                    px = int(input("Unesi x koordinatu: "))
                    py = int(input("Unesi y koordinatu: "))

                    if self.ispitaj_koord(px,py):
                        self.trenutno_stanje[px][py] ='X';
                        self.na_potezu = 'O'
                        break
                    else:
                        print("Potez nije validan!")
        #ako je na potezu O odnosno komp
            else:

                (m,px,py) = self.Max()
                self.trenutno_stanje[px][py] = 'O'
                self.na_potezu = 'X'

g = Game()
g.play()




