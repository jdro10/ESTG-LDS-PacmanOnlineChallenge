
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindows(object):
    def setupUi(self, MainWindows):
        MainWindows.setObjectName("MainWindows")
        MainWindows.resize(629, 454)
        self.centralwidget = QtWidgets.QWidget(MainWindows)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 30, 231, 231))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("pacman.png"))
        self.label_4.setObjectName("label_4")
        self.btn_Logar_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Logar_4.setGeometry(QtCore.QRect(200, 320, 211, 51))
        self.btn_Logar_4.setObjectName("btn_Logar_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 70, 191, 161))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("vermelho.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(110, 260, 111, 31))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(450, 260, 111, 31))
        self.checkBox_2.setObjectName("checkBox_2")
        MainWindows.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindows)
        self.statusbar.setObjectName("statusbar")
        MainWindows.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindows)
        QtCore.QMetaObject.connectSlotsByName(MainWindows)

    def retranslateUi(self, MainWindows):
        _translate = QtCore.QCoreApplication.translate
        MainWindows.setWindowTitle(_translate("MainWindows", "Choose your character"))
        self.btn_Logar_4.setText(_translate("MainWindows", "Search Opponent"))
        self.checkBox.setText(_translate("MainWindows", "Pacman"))
        self.checkBox_2.setText(_translate("MainWindows", "Ghost"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindows = QtWidgets.QMainWindow()
    ui = Ui_MainWindows()
    ui.setupUi(MainWindows)
    MainWindows.show()
    sys.exit(app.exec_())
