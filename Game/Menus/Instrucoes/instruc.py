
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindows(object):
    def setupUi(self, MainWindows):
        MainWindows.setObjectName("MainWindows")
        MainWindows.resize(629, 454)
        self.centralwidget = QtWidgets.QWidget(MainWindows)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 641, 361))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("inst.png"))
        self.label_4.setObjectName("label_4")
        self.btn_Logar_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Logar_3.setGeometry(QtCore.QRect(250, 380, 151, 51))
        self.btn_Logar_3.setObjectName("btn_Logar_3")
        self.btn_Logar_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Logar_4.setGeometry(QtCore.QRect(410, 380, 211, 51))
        self.btn_Logar_4.setObjectName("btn_Logar_4")
        self.btn_Logar_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Logar_5.setGeometry(QtCore.QRect(90, 380, 151, 51))
        self.btn_Logar_5.setObjectName("btn_Logar_5")
        MainWindows.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindows)
        self.statusbar.setObjectName("statusbar")
        MainWindows.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindows)
        QtCore.QMetaObject.connectSlotsByName(MainWindows)

    def retranslateUi(self, MainWindows):
        _translate = QtCore.QCoreApplication.translate
        MainWindows.setWindowTitle(_translate("MainWindows", "POC - Instructions"))
        self.btn_Logar_3.setText(_translate("MainWindows", "Save"))
        self.btn_Logar_4.setText(_translate("MainWindows", "Default  Definition"))
        self.btn_Logar_5.setText(_translate("MainWindows", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindows = QtWidgets.QMainWindow()
    ui = Ui_MainWindows()
    ui.setupUi(MainWindows)
    MainWindows.show()
    sys.exit(app.exec_())
