import GradeyPyGui as gp
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

username = ''
password = ''
pageManager = None

def getCredentials(uname, pword, pgMnger, wLabel):
    username = uname
    password = pword
    pageManager = pgMnger

    wLabel.setText("Welcome, " + uname)
    pgMnger.setCurrentIndex(1)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = gp.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    