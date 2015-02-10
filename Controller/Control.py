__author__ = 'Isabella'

from View.View import MyView
from Model.Model import Spielfeld
from Model.Model import Hilfestellung
import sys
from PyQt5.QtWidgets import *


class Controller(QWidget):

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
            self.newGame(self.level,self.schw)
        elif self.view.schw.currentIndex() is 1:
            self.level = 1
            self.schw = "easy"
            self.newGame(self.level,self.schw)
        elif self.view.schw.currentIndex() is 2:
            self.level = 2
            self.schw = "easy"
            self.newGame(self.level,self.schw)
        elif self.view.schw.currentIndex() is 3:
            self.level = 3
            self.schw = "easy"
            self.newGame(self.level,self.schw)
        elif self.view.schw.currentIndex() is 4:
            self.level = 4
            self.schw = "easy"
            self.newGame(self.level,self.schw)


    def newGame(self,level,schw):
        #Spiel neu generieren
        self.model.set_schw(schw)
        self.view.schw.setCurrentIndex(level)
        self.view.textOpenField.setText(str(self.model.get_anzFarbFelder()))

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
                    self.view.button[i][j].setText("1")
                else:
                    self.view.button[i][j].setText("0")

    def buttonClicked(self):
        print("Gedrückt :D")




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