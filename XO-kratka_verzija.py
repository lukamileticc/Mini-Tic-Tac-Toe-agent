class Igra: #banalan primer ali implementira igru prc
    def __init__(self):
        self.inicijalizuj()

    def inicijalizuj(self):
        self.trenutno_stanje = ['.','.','.']
        self.na_potezu = 'O'
        self.broj_iteracija = 0

    def nacrtaj_tablu(self):
        print(" 0 1 2")
        print("|",end="")
        for i in range (3):
            print("{}".format(self.trenutno_stanje[i]),end="|")
        print() #new line

    def validnost(self,px):
        if px < 0 and px > 3 :
            print("Brojeve od 0 do 2!")
            return False
        elif self.trenutno_stanje[px] != '.':
            print("Polje je zauzeto!")
            return False
        else:
            return True

    def the_end(self):

        if self.trenutno_stanje == ['X','X','O']:
              return 'X'
        if self.trenutno_stanje == ['O','X','X']:
              return 'X'
        if self.trenutno_stanje == ['X','O','O']:
              return 'O'
        if self.trenutno_stanje == ['O', 'O', 'X']:
              return 'O'
        if self.trenutno_stanje == ['O','X','O']:
              return '.'
        if self.trenutno_stanje == ['X','O','X']:
              return '.' #nereseno

        for i in self.trenutno_stanje:
            if i == '.':
                return None #igra jos nije gotova

    #ovo je komp! znaci O
    def Max(self):
        #imamo neku funkciju evaluacija:
        # 0 - nereseno 1-pobeda -1 poraz
        #trazimo maksimalnu znaci stavljamo na minimanlu vrednost!
        maxv = -2
        px = None
        self.broj_iteracija +=1
        rez = self.the_end()
        if rez == 'X':
            return (-1,None)
        elif rez == 'O':
            return (1,None)
        elif rez == '.':
            return (0,None)

        for i in range(0,3):
            if self.trenutno_stanje[i] =='.':
                self.trenutno_stanje[i] = 'O'
                m = self.Min()
                if m > maxv:
                    maxv = m
                    px = i

                self.trenutno_stanje[i] = '.'

        return (maxv,px)

    def Min(self):

        self.broj_iteracija += 1
        minv = 2

        rez = self.the_end()
        if rez == 'X':
            return -1
        elif rez == 'O':
            return 1
        elif rez == '.':
            return 0

        for i in range(3):
            if self.trenutno_stanje[i] == '.':
                self.trenutno_stanje[i] = 'X'
                (m,px) = self.Max()
                if m < minv:
                    minv = m
                self.trenutno_stanje[i] = '.'

        return minv

    def play(self):

        while True:
            self.nacrtaj_tablu()

            rezultat = self.the_end()
            if rezultat != None:
                if rezultat == 'X':
                    print("Pobedio je X")
                elif rezultat == 'O':
                    print("Pobedio je O")
                else:
                    print("Nereseno je!")

                print("Broj ponavljanja: ", self.broj_iteracija)
                break

            # #covek igra prvi
            # if self.na_potezu == 'X':
            #     while True:
            #         px = int(input("Unesite koordinatu: "))
            #         if self.validnost(px):
            #             self.trenutno_stanje[px] = 'X'
            #             self.na_potezu = 'O'
            #             break
            #
            # else: #komp igra ovde!
            #     (m,px) = self.Max()
            #     self.trenutno_stanje[px] = 'O'
            #     self.na_potezu = 'X'
            #     #covek igra prvi

            if self.na_potezu == 'O':  # komp igra ovde!
                (m, px) = self.Max()
                self.trenutno_stanje[px] = 'O'
                self.na_potezu = 'X'

            elif self.na_potezu == 'X':
                 while True:
                    px = int(input("Unesite koordinatu: "))
                    if self.validnost(px):
                        self.trenutno_stanje[px] = 'X'
                        self.na_potezu = 'O'
                        break


i = Igra()
i.play()
