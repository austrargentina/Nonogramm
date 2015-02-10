__author__ = 'Daniel'

import random
from math import ceil

class Spielfeld():

    """
    Ist das gesamte Spielfeld und beinhaltet darber hinaus auch die zwei Hilfestellungen (oben und rechts vom Spielfeld)
    """

    anzReihen = 15 #anzahl der Reihen
    anzSpalten = 15 #anzahl der Spalten

    schwGrad = "medium" #schwierigkeitsgrad (entscheidet Ã¼ber anzFarbFelder)
    anzFarbFelder = 0 #anzahl der felder, die farbig sind
    anzFehlendeFelder = 0 #felder, die noch aufgedeckt werden mÃ¼ssen

    spielfeld = [] #spielfeld selber

    hilfeOben = None #hilfestellung (zahlen) oben
    hilfeRechts = None #hilfestellung (zahlen) rechts

    aktElement = 0 #fuer iteration Ã¼ber spielfeld

    def __init__(self):
        #fuellen des spielfelds mit lauter 0en
        for i in range(self.anzReihen):
                self.spielfeld.append([])
                for j in range(self.anzSpalten):
                    self.spielfeld[i].append(0)

        #neuanodrnung der farbigen felder
        self.neuAnordnen()

        #bereitstellen der hilfestellungen
        self.hilfeOben = Hilfestellung(self, "oben")
        self.hilfeRechts = Hilfestellung(self, "rechts")

    def anzFarbFelderFestlegen(self):
        """
        Je nach Schwierigkeitsgrad wird anzFarbFelder festgelegt
        :return: -
        """
        if self.schwGrad is "easy":
            self.anzFarbFelder = ceil(self.anzSpalten*self.anzReihen*0.888) #88% sind farbig
        elif self.schwGrad is "medium":
            self.anzFarbFelder = ceil(self.anzSpalten*self.anzReihen*0.666)    #66% sind farbig
        elif self.schwGrad is "hard":
            self.anzFarbFelder = ceil(self.anzSpalten*self.anzReihen*0.555) #55% sind farbig
        elif self.schwGrad is "expert":
            self.anzFarbFelder = ceil(self.anzSpalten*self.anzReihen*0.4)  #40% sind farbig
        elif self.schwGrad is "impossible":
            self.anzFarbFelder = ceil(self.anzSpalten*self.anzReihen*0.222) #22% sind farbig

    def neuAnordnen(self):
        """
        Spielfeld wird neu mit 1en gefÃ¼llt
        :return: -
        """

        self.anzFarbFelderFestlegen()

        self.anzFehlendeFelder = 0

        while self.anzFehlendeFelder < self.anzFarbFelder:
            for i in range(self.anzReihen):
                for j in range(self.anzSpalten):
                    #Nur wenn aktuelles Feld nicht farbig ist und noch nicht genÃ¼gend Felder farbig sind
                    if self.spielfeld[i][j] is 0 and self.anzFehlendeFelder < self.anzFarbFelder:
                        #Random, ob null (keine Farbe) oder eins (Farbe)
                        wahl = random.randint(0,1)
                        #zuweisung
                        self.spielfeld[i][j] = wahl
                        #Falls eins wird anzFehlendeFelder zugezÃ¤hlt
                        if wahl is 1:
                            self.anzFehlendeFelder += 1

    def anzeigen(self):
        """
        Gibt das Spielfeld in der Konsole aus
        :return: -
        """
        for i in range(self.anzReihen):
            print(self.spielfeld[i])

    def __iter__(self):
        """
        Zeigt, dass Objekt iterable ist
        :return:
        """
        return self

    def __next__(self):
        """
        Gibt immer nÃ¤chste Reihe des Spielfelds zurÃ¼ck
        :return:
        """
        if self.aktElement >= self.anzReihen:
            raise StopIteration
        else:
            self.aktElement += 1;
            return self.spielfeld[self.aktElement - 1]

    def __getitem__(self, key):
        return self.spielfeld[key]

    def get_anzFarbFelder(self):
       return self.anzFarbFelder

    def get_schw(self):
        return self.schw

    def set_schw(self,schw):
        self.schw = schw

class Hilfestellung(object):

    spielfeld = None #Spielfeld, zu welchem die Hilfestellungen erstellt werden sollen
    art = None #ob oben oder rechts vom Spielfeld
    hilfestellung = [] #hilfestellung selber

    anzReihen = 0 #anzahl der Reihen
    anzSpalten = 0 #anzahl der Spalten

    aktElement = 0 #aktuelles Element fuer Iteration


    def __init__(self, spielfeld, art):
        self.spielfeld = spielfeld
        self.art = art
        self.hilfestellung = []

        #Falls Hilfestellung oben platziert ist
        if art is "oben":
            self.anzSpalten = self.spielfeld.anzSpalten #Ã¼bernehmen der anzahl der spalten
            self.anzReihen = ceil(self.spielfeld.anzReihen/2.0); #nach formel n/2 +1

        #Falls Hilfestellung rechts platziert ist
        elif art is "rechts":
            self.anzReihen = self.spielfeld.anzReihen #Ã¼bernehmen der anzahl der reihen
            self.anzSpalten = ceil(self.spielfeld.anzSpalten/2.0); #nach fromel n/2 +1

        #fuellen des spielfelds mit lauter 0en
        for i in range(self.anzReihen):
                self.hilfestellung.append([])
                for j in range(self.anzSpalten):
                    self.hilfestellung[i].append(0)

        self.neuBerechnen()

    def neuBerechnen(self):
        if self.art is "oben":
            for spalte in range(self.spielfeld.anzSpalten):
                vorherigesWar0 = True #war das vorherige eine 0
                letztesFeld = False
                aktAnzFarbige = 0
                aktHSFeld = 0   #Aktuelles Feld im Hilfestellungsraster

                for reihe in range(self.spielfeld.anzReihen):
                    current = self.spielfeld[reihe][spalte]

                    if reihe + 1 not in range(self.spielfeld.anzReihen): #falls letztes feld
                        letztesFeld = True

                    if vorherigesWar0 is True: #falls vorheriges eine 0 war
                        if current is 0: #falls dieses wieder 0 ist
                            continue #nÃ¤chstes feld
                        elif current is 1: #falls dieses 1 (farbig)
                            aktAnzFarbige += 1
                            vorherigesWar0 = False
                            if letztesFeld is True: #wenns das letzte Feld ist, dann reinschreiben
                                self.hilfestellung[aktHSFeld][spalte] = aktAnzFarbige #aktuelles feld im hs raster bekommt aktuelle anzahl der farbigen
                                aktAnzFarbige = 0 #zurÃ¼cksetzen von den aktuellem wert
                    elif vorherigesWar0 is False:
                        if current is 0:
                            self.hilfestellung[aktHSFeld][spalte] = aktAnzFarbige #aktuelles feld im hs raster bekommt aktuelle anzahl der farbigen
                            aktAnzFarbige = 0 #zurÃ¼cksetzen von den aktuellem wert
                            aktHSFeld += 1 #eins weiter zÃ¤hlen in hs raster
                            vorherigesWar0 = True
                        elif current is 1:
                            aktAnzFarbige += 1
                            if letztesFeld is True: #wenns das letzte Feld ist, dann reinschreiben
                                self.hilfestellung[aktHSFeld][spalte] = aktAnzFarbige #aktuelles feld im hs raster bekommt aktuelle anzahl der farbigen
                                aktAnzFarbige = 0 #zurÃ¼cksetzen von den aktuellem wert

            self.hilfestellung.reverse() #umdrehen, weil hilfestellung umgedreht ist im Spiel (beginnt von unten)


        elif self.art is "rechts":
            for reihe in range(self.spielfeld.anzReihen):
                vorherigesWar0 = True #war das vorherige eine 0
                letztesFeld = False
                aktAnzFarbige = 0
                aktHSFeld = 0   #Aktuelles Feld im Hilfestellungsraster

                for spalte in range(self.spielfeld.anzSpalten):
                    current = self.spielfeld[reihe][spalte]

                    if spalte + 1 not in range(self.spielfeld.anzSpalten): #falls letztes feld
                        letztesFeld = True

                    if vorherigesWar0 is True: #falls vorheriges eine 0 war
                        if current is 0: #falls dieses wieder 0 ist
                            continue #nÃ¤chstes feld
                        elif current is 1: #falls dieses 1 (farbig)
                            aktAnzFarbige += 1
                            vorherigesWar0 = False
                            if letztesFeld is True: #wenns das letzte Feld ist, dann reinschreiben
                                self.hilfestellung[reihe][aktHSFeld] = aktAnzFarbige #aktuelles feld im hs raster bekommt aktuelle anzahl der farbigen
                                aktAnzFarbige = 0 #zurÃ¼cksetzen von den aktuellem wert
                    elif vorherigesWar0 is False:
                        if current is 0:
                            self.hilfestellung[reihe][aktHSFeld] = aktAnzFarbige #aktuelles feld im hs raster bekommt aktuelle anzahl der farbigen
                            aktAnzFarbige = 0 #zurÃ¼cksetzen von den aktuellem wert
                            aktHSFeld += 1 #eins weiter zÃ¤hlen in hs raster
                            vorherigesWar0 = True
                        elif current is 1:
                            aktAnzFarbige += 1
                            if letztesFeld is True: #wenns das letzte Feld ist, dann reinschreiben
                                self.hilfestellung[reihe][aktHSFeld] = aktAnzFarbige #aktuelles feld im hs raster bekommt aktuelle anzahl der farbigen
                                aktAnzFarbige = 0 #zurÃ¼cksetzen von den aktuellem wert





    def __iter__(self):
        """
        Zeigt, dass Objekt iterable ist
        :return:
        """
        return self

    def __next__(self):
        """
        Gibt immer nÃ¤chste Reihe des Spielfelds zurÃ¼ck
        :return:
        """
        if self.aktElement >= self.anzReihen:
            raise StopIteration
        else:
            self.aktElement += 1;
            return self.hilfestellung[self.aktElement - 1]

    def __getitem__(self, key):
        return self.hilfestellung[key]

    def anzeigen(self):
        """
        Gibt die Hilfestellung in der Konsole aus
        :return: -
        """
        for i in range(self.anzReihen):
            print(self.hilfestellung[i])


"""
a = Spielfeld()
print("--- Hilfestellung oben ---")
a.hilfeOben.anzeigen();
print("--- Spielfeld ---")
a.anzeigen()
print("--- Hilfestellung rechts")
a.hilfeRechts.anzeigen();"""
