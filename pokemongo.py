from PyQt4 import QtCore, QtGui
from runserver import run
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(360, 191)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 81, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 81, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.Auth = QtGui.QComboBox(self.centralwidget)
        self.Auth.setGeometry(QtCore.QRect(100, 20, 181, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Auth.setFont(font)
        self.Auth.setObjectName(_fromUtf8("Auth"))
        self.Auth.addItem(_fromUtf8(""))
        self.Auth.addItem(_fromUtf8(""))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 160, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.handelButton)
        self.UserName = QtGui.QPlainTextEdit(self.centralwidget)
        self.UserName.setGeometry(QtCore.QRect(100, 50, 181, 21))
        self.UserName.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.UserName.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.UserName.setObjectName(_fromUtf8("UserName"))
        self.Password = QtGui.QPlainTextEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(100, 80, 181, 21))
        self.Password.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Password.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Password.setObjectName(_fromUtf8("Password"))
        self.Location = QtGui.QPlainTextEdit(self.centralwidget)
        self.Location.setGeometry(QtCore.QRect(100, 110, 181, 21))
        self.Location.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Location.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Location.setObjectName(_fromUtf8("Location"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 81, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.Steps = QtGui.QPlainTextEdit(self.centralwidget)
        self.Steps.setGeometry(QtCore.QRect(100, 140, 181, 21))
        self.Steps.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Steps.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Steps.setObjectName(_fromUtf8("Steps"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "PokemonGO Map", None))
        self.label.setText(_translate("MainWindow", "Type of Account", None))
        self.label_2.setText(_translate("MainWindow", "User Name", None))
        self.label_3.setText(_translate("MainWindow", "Location", None))
        self.label_4.setText(_translate("MainWindow", "Password", None))
        self.Auth.setItemText(0, _translate("MainWindow", "                 google", None))
        self.Auth.setItemText(1, _translate("MainWindow", "                  ptc", None))
        self.pushButton.setText(_translate("MainWindow", "Launch", None))
        self.label_5.setText(_translate("MainWindow", "Steps", None))
    def handelButton(self):
        username=str(self.UserName.toPlainText()).strip()
        password=str(self.Password.toPlainText()).strip()
        choice=str(self.Auth.currentText()).strip()
        steps=str(self.Steps.toPlainText())
        location=str(self.Location.toPlainText())
        run(choice,username,password,location,steps)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

