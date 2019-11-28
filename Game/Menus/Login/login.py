


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindows(object):
    def setupUi(self, MainWindows):
        MainWindows.setObjectName("MainWindows")
        MainWindows.resize(637, 557)
        self.centralwidget = QtWidgets.QWidget(MainWindows)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_Logar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Logar.setGeometry(QtCore.QRect(240, 420, 151, 51))
        self.btn_Logar.setObjectName("btn_Logar")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(160, 280, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(160, 350, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 290, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 340, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 490, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(549, 500, 81, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 0, 331, 271))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("image.png"))
        self.label_4.setObjectName("label_4")
        MainWindows.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindows)
        self.statusbar.setObjectName("statusbar")
        MainWindows.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindows)
        QtCore.QMetaObject.connectSlotsByName(MainWindows)

    def retranslateUi(self, MainWindows):
        _translate = QtCore.QCoreApplication.translate
        MainWindows.setWindowTitle(_translate("MainWindows", "POC - Pacman Online Challenge"))
        self.btn_Logar.setText(_translate("MainWindows", "Login"))
        self.label.setText(_translate("MainWindows", "Email:"))
        self.label_2.setText(_translate("MainWindows", "Password:"))
        self.label_3.setText(_translate("MainWindows", "Don\'t have account yet?"))
        self.pushButton.setText(_translate("MainWindows", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindows = QtWidgets.QMainWindow()
    ui = Ui_MainWindows()
    ui.setupUi(MainWindows)
    MainWindows.show()
    sys.exit(app.exec_())
