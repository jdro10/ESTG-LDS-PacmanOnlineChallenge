
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindows(object):
    def setupUi(self, MainWindows):
        MainWindows.setObjectName("MainWindows")
        MainWindows.resize(637, 745)
        self.centralwidget = QtWidgets.QWidget(MainWindows)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_Logar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Logar.setGeometry(QtCore.QRect(250, 300, 151, 51))
        self.btn_Logar.setObjectName("btn_Logar")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(540, 680, 81, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 0, 331, 271))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("image.png"))
        self.label_4.setObjectName("label_4")
        self.btn_Logar_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Logar_2.setGeometry(QtCore.QRect(220, 370, 211, 51))
        self.btn_Logar_2.setObjectName("btn_Logar_2")
        self.btn_Logar_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Logar_3.setGeometry(QtCore.QRect(250, 450, 151, 51))
        self.btn_Logar_3.setObjectName("btn_Logar_3")
        self.btn_Logar_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Logar_4.setGeometry(QtCore.QRect(220, 530, 211, 51))
        self.btn_Logar_4.setObjectName("btn_Logar_4")
        self.btn_Logar_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Logar_5.setGeometry(QtCore.QRect(250, 610, 151, 51))
        self.btn_Logar_5.setObjectName("btn_Logar_5")
        MainWindows.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindows)
        self.statusbar.setObjectName("statusbar")
        MainWindows.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindows)
        QtCore.QMetaObject.connectSlotsByName(MainWindows)

    def retranslateUi(self, MainWindows):
        _translate = QtCore.QCoreApplication.translate
        MainWindows.setWindowTitle(_translate("MainWindows", "POC - MENU"))
        self.btn_Logar.setText(_translate("MainWindows", "SinglePlayer"))
        self.pushButton.setText(_translate("MainWindows", "Logout"))
        self.btn_Logar_2.setText(_translate("MainWindows", "MultiPlayer"))
        self.btn_Logar_3.setText(_translate("MainWindows", "Stats"))
        self.btn_Logar_4.setText(_translate("MainWindows", "Instructions"))
        self.btn_Logar_5.setText(_translate("MainWindows", "Options"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindows = QtWidgets.QMainWindow()
    ui = Ui_MainWindows()
    ui.setupUi(MainWindows)
    MainWindows.show()
    sys.exit(app.exec_())
