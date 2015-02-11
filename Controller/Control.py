__author__ = 'Isabella'

from View.View import MyView
from Model.Model import Spielfeld, Hilfestellung
#from View import MyView
#from Model import Spielfeld, Hilfestellung
import sys
from PyQt5.QtWidgets import *


class Controller(QWidget, object):

    schw = "medium" #anfangseinstellung ist medium

    def __init__(self, parent=None):
        super().__init__(parent)
        self.model = Spielfeld()
        self.view = MyView(self.model)
        self.view.setupUi(self)

        self.view.schw.setCurrentIndex(1)
        self.view.textOpenField.setText(str(self.model.get_anzFarbFelder()))

        self.view.neustart.clicked.connect(self.newGame)
        self.view.loesung.clicked.connect(self.Loesung)
        self.view.schw.activated.connect(self.getLevel)

        self.buttonreg()

        self.showHelpOben()
        self.showHelpRechts()

    def buttonreg(self):
        for i in range(self.model.anzReihen):
            for j in range(self.model.anzSpalten):
                self.view.button[i][j].clicked.connect(self.buttonClicked)

    def getLevel(self):
        if self.view.schw.currentIndex() is 0:
            self.level = 0
            self.schw = "easy"
            #self.newGame(self.level,self.schw)
        elif self.view.schw.currentIndex() is 1:
            self.level = 1
            self.schw = "medium"
            #self.newGame(self.level,self.schw)
        elif self.view.schw.currentIndex() is 2:
            self.level = 2
            self.schw = "hard"
            #self.newGame(self.level,self.schw)
        elif self.view.schw.currentIndex() is 3:
            self.level = 3
            self.schw = "expert"
            #self.newGame(self.level,self.schw)
        elif self.view.schw.currentIndex() is 4:
            self.level = 4
            self.schw = "impossible"
            #self.newGame(self.level,self.schw)


    def newGame(self):
        #Spiel neu generieren
        self.model.set_schw(self.schw)
        #self.view.schw.setCurrentIndex(self.level) #Anzeigen des SCwhierigkeitsgrads in der Combobox
        self.model.neuAnordnen()    #Anordnen des Feldes
        #Leeren des Spielfelds
        for i in range(self.model.anzReihen):
            for j in range(self.model.anzSpalten):
                self.view.button[i][j].setStyleSheet("QPushButton {background-color: yellow}")

        self.model.hilfeErstellen() #Hilfestellungen erstellen
        self.showHelpOben()         #Hilfestellung oben anzeigen
        self.showHelpRechts()       #Hilfestellung rechts anzeigen
        self.view.textOpenField.setText(str(self.model.get_anzFarbFelder())) #Anzahl der fehlenden anzeigen

    def showHelpOben(self):
        for i in range(len(self.model.hilfeOben.hilfestellung)):
            for j in range(len(self.model.hilfeOben.hilfestellung[i])):
                self.view.textEdit_oben_alle[i][j].setText(str(self.model.hilfeOben.hilfestellung[i][j]))

    def showHelpRechts(self):
        for i in range(len(self.model.hilfeRechts.hilfestellung)):
            for j in range(len(self.model.hilfeRechts.hilfestellung[i])):
                self.view.textEdit_rechts_alle[i][j].setText(str(self.model.hilfeRechts.hilfestellung[i][j]))

    def Loesung(self):
        for i in range(self.model.anzReihen):
            for j in range(self.model.anzSpalten):
                if str(self.model.spielfeld[i][j]) == "1":
                    self.view.button[i][j].setStyleSheet("QPushButton {background-color: blue}")
                else:
                    self.view.button[i][j].setStyleSheet("QPushButton {background-color: yellow}")

    def buttonClicked(self):
        button = self.sender()
        i = button.x
        j = button.y
        if button.aktiviert is False: #wenns nicht aktiviert ist (gelb)
            button.aktiviert = True
            button.setStyleSheet("QPushButton {background-color: blue}")
            if self.model.spielfeld[i][j] is 1:
                self.model.anzFehlendeFelder -= 1
                if self.model.anzFehlendeFelder == 0: #falls alle gefunden
                    print("YEAH GEWONNEN!")
        else:
            button.aktiviert = False
            button.setStyleSheet("QPushButton {background-color: yellow}")
            if self.model.spielfeld[i][j] is 1:
                self.model.anzFehlendeFelder += 1


        self.view.textOpenField.setText(str(self.model.anzFehlendeFelder)) #Anzahl der fehlenden anzeigen


        #print(self.x, self.y, self.objectName())

        #print("Gedrückt :D" + str(i) + str(j))




    def __iter__(self):
        """
        Zeigt, dass Objekt iterable ist
        :return:
        """
        return self

if __name__ == '__main__':
    app = QApplication(sys.argv)
    c = Controller()
    c.show()
    sys.exit(app.exec_())