
from PyQt5 import QtWidgets
from GradeyPyGui import Ui_MainWindow
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = Ui_MainWindow()
    application.show()
    sys.exit(app.exec_())