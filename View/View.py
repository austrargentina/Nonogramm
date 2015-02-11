__author__ = 'Isabella'
from PyQt5 import QtCore, QtGui, QtWidgets

class MyView(object):

    def __init__(self, model):
        self.model = model

    def setupUi(self, Dialog):

        Dialog.setObjectName("Nonogram")
        Dialog.setWindowTitle("Nonogram")
        Dialog.resize(700, 600)
        Dialog.setMaximumSize(QtCore.QSize(900, 800))
        #Dialog.setMiniumSize(QtCore.QSize(700,600))

        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 750, 881, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Offene Textfelder
        self.openFieldsLa = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.openFieldsLa.setMaximumSize(QtCore.QSize(150, 30))
        self.openFieldsLa.setObjectName("openFieldsLa")
        self.horizontalLayout.addWidget(self.openFieldsLa)


        self.textOpenField = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.textOpenField.setEnabled(False)
        self.textOpenField.setMaximumSize(QtCore.QSize(150, 30))
        self.textOpenField.setObjectName("textOpenField")
        #self.textOpenField.setAlignment
        self.horizontalLayout.addWidget(self.textOpenField)
        #
        self.loesung = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.loesung.setMaximumSize(QtCore.QSize(150, 30))
        self.loesung.setStyleSheet("")
        self.loesung.setObjectName("loesung")
        self.horizontalLayout.addWidget(self.loesung)

        self.schw = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.schw.setMaximumSize(QtCore.QSize(150, 30))
        self.schw.setEditable(False)
        self.schw.setObjectName("schw")
        self.schw.addItem("")
        self.schw.addItem("")
        self.schw.addItem("")
        self.schw.addItem("")
        self.schw.addItem("")
        self.horizontalLayout.addWidget(self.schw)

        self.neustart = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.neustart.setMaximumSize(QtCore.QSize(150, 30))
        self.neustart.setObjectName("neustart")
        self.horizontalLayout.addWidget(self.neustart)

        self.gridLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 541, 231))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.grid_oben = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.grid_oben.setContentsMargins(0, 0, 0, 0)
        self.grid_oben.setObjectName("grid_oben")

        self.textEdit_oben_alle = []

        for i in range(len(self.model.hilfeOben.hilfestellung)):
            self.textEdit_oben_alle.append([])
            for j in range(len(self.model.hilfeOben.hilfestellung[i])):
                self.textEdit_oben_alle[i].append(QtWidgets.QTextEdit(self.gridLayoutWidget_2))
                self.textEdit_oben_alle[i][j].setEnabled(False)
                self.textEdit_oben_alle[i][j].setMaximumSize(QtCore.QSize(30, 30))
                self.textEdit_oben_alle[i][j].setObjectName("textEdit_oben")
                self.grid_oben.addWidget(self.textEdit_oben_alle[i][j], i, j, 1, 1)

        self.gridLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 250, 541, 491))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridspielfeld = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridspielfeld.setContentsMargins(0, 0, 0, 0)
        self.gridspielfeld.setObjectName("gridspielfeld")

        self.button = []



        for i in range(self.model.anzReihen):
            self.button.append([])
            for j in range(self.model.anzSpalten):
                self.button[i].append(QtWidgets.QPushButton(self.gridLayoutWidget_3))
                self.button[i][j].setMaximumSize(QtCore.QSize(30, 30))
                self.button[i][j].setObjectName("button")
                self.gridspielfeld.addWidget(self.button[i][j], i, j, 1, 1)

        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(560, 250, 321, 491))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridlinks = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridlinks.setContentsMargins(0, 0, 0, 0)
        self.gridlinks.setObjectName("gridlinks")


        self.textEdit_rechts_alle = []

        for i in range(len(self.model.hilfeRechts.hilfestellung)):
            self.textEdit_rechts_alle.append([])
            for j in range(len(self.model.hilfeRechts.hilfestellung[i])):
                self.textEdit_rechts_alle[i].append(QtWidgets.QTextEdit(self.gridLayoutWidget_2))
                self.textEdit_rechts_alle[i][j].setEnabled(False)
                self.textEdit_rechts_alle[i][j].setMaximumSize(QtCore.QSize(30, 30))
                self.textEdit_rechts_alle[i][j].setObjectName("textEdit_oben")
                self.gridlinks.addWidget(self.textEdit_rechts_alle[i][j], i, j, 1, 1)

        self.retranslateUi(Dialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.openFieldsLa.setText(_translate("Dialog", "Felder offen:"))
        self.loesung.setText(_translate("Dialog", "Loesung"))
        self.schw.setItemText(0, _translate("Dialog", "Easy"))
        self.schw.setItemText(1, _translate("Dialog", "Medium"))
        self.schw.setItemText(2, _translate("Dialog", "Hard"))
        self.schw.setItemText(3, _translate("Dialog", "Expert"))
        self.schw.setItemText(4, _translate("Dialog", "Impossible"))
        self.neustart.setText(_translate("Dialog", "Neustart"))
