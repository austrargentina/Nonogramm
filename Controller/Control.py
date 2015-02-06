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

        self.view.neustart.clicked.connect(self.newGame)
        self.view.loesung.clicked.connect(self.Loesung)
        self.view.schw.activated.connect(self.getLevel)
        self.view.textOpenField.setText(str(self.model.getFehlendeFelder()))

        self.showHelpOben()
        #self.showHelpRechts()

    def newGame(self):
        c.close()
        c.show()

    def Loesung(self):
        print("Loesung")

    def getLevel(self):
        if self.view.schw.currentText() is "Easy":
            self.model.schwGrad = "easy"
            self.view.schw.setCurrentText(self,"Easy")
        elif self.view.schw.currentText() is "Medium":
             self.model.anzFarbFelderFestlegen("Medium")
             self.view.schw.setCurrentText(self,"Medium")
        elif self.view.schw.currentText() is "Hard":
             self.model.anzFarbFelderFestlegen("Hard")
             self.view.schw.setCurrentText(self,"Hard")
        elif self.view.schw.currentText() is "Expert":
             self.model.anzFarbFelderFestlegen("Expert")
             self.view.schw.setCurrentText(self,"Expert")
        elif self.view.schw.currentText() is "Impossible":
            self.model.anzFarbFelderFestlegen("Impossible")
            self.view.schw.setCurrentText(self,"Impossible")

    def showHelpOben(self):
        #print(len(self.model.hilfeOben.hilfestellung))
        #print(self.view.textEdit_oben.setText("1"))
        for i in range(len(self.model.hilfeOben.hilfestellung)):
            for j in range(len(self.model.hilfeOben.hilfestellung[i])):
                self.view.textEdit_oben_alle[i][j].setText(str(self.model.hilfeOben.hilfestellung[i][j]))

    def showHelpRechts(self):
        #print(len(self.model.hilfeOben.hilfestellung))
        for i in range(len(self.model.hilfeRechts.hilfestellung)):
            self.view.textEdit_oben.setText(str(self.model.hilfeRechts.hilfestellung[i]))

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