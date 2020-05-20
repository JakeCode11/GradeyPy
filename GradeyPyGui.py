from PyQt5 import QtCore, QtGui, QtWidgets
import login as lg
import mainMenu as mm

# Global variables
username = ''
password = ''
pageMngr = None

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(903, 594)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(1280, 650))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(138, 212, 255, 255), stop:1 rgba(255, 255, 255, 255))")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.LoginPage = QtWidgets.QWidget()
        self.LoginPage.setObjectName("LoginPage")
        self.gridLayout = QtWidgets.QGridLayout(self.LoginPage)
        self.gridLayout.setObjectName("gridLayout")
        
        self.pwordInput = QtWidgets.QLineEdit(self.LoginPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pwordInput.sizePolicy().hasHeightForWidth())
        self.pwordInput.setSizePolicy(sizePolicy)
        self.pwordInput.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pwordInput.setStyleSheet("background: white")
        self.pwordInput.setInputMask("")
        self.pwordInput.setText("")
        self.pwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwordInput.setAlignment(QtCore.Qt.AlignCenter)
        self.pwordInput.setObjectName("pwordInput")
        self.gridLayout.addWidget(self.pwordInput, 5, 2, 1, 1)
        
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        
        self.exitBtn = QtWidgets.QPushButton(self.LoginPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitBtn.sizePolicy().hasHeightForWidth())
        self.exitBtn.setSizePolicy(sizePolicy)
        self.exitBtn.setStyleSheet("background-color: white")
        self.exitBtn.setObjectName("exitBtn")
        self.exitBtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.gridLayout.addWidget(self.exitBtn, 9, 2, 1, 1)
        
        self.loginBtn = QtWidgets.QPushButton(self.LoginPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginBtn.sizePolicy().hasHeightForWidth())
        self.loginBtn.setSizePolicy(sizePolicy)
        self.loginBtn.setStyleSheet("background-color: white")
        self.loginBtn.setObjectName("loginBtn")
        self.loginBtn.clicked.connect(lambda: lg.getCredentials(self.getuname(), self.getpword(), self.getpageManager(), self.getwelcomelbl()))
        self.gridLayout.addWidget(self.loginBtn, 8, 2, 1, 1)
        
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.unameInput = QtWidgets.QLineEdit(self.LoginPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unameInput.sizePolicy().hasHeightForWidth())
        self.unameInput.setSizePolicy(sizePolicy)
        self.unameInput.setStyleSheet("background: white")
        self.unameInput.setText("")
        self.unameInput.setAlignment(QtCore.Qt.AlignCenter)
        self.unameInput.setObjectName("unameInput")
        self.gridLayout.addWidget(self.unameInput, 2, 2, 2, 1)
        self.appTitle = QtWidgets.QLabel(self.LoginPage)
        
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.appTitle.setFont(font)
        self.appTitle.setStyleSheet("background: transparent")
        self.appTitle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.appTitle.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.appTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.appTitle.setObjectName("appTitle")
        self.gridLayout.addWidget(self.appTitle, 1, 2, 1, 1)
       
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 10, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.LoginPage)
        
        self.MenuPage = QtWidgets.QWidget()
        self.MenuPage.setObjectName("MenuPage")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.MenuPage)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.welcomeLabel = QtWidgets.QLabel(self.MenuPage)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(45)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setStyleSheet("background-color: transparent;")
        self.welcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.gridLayout_3.addWidget(self.welcomeLabel, 2, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.MenuPage)
        self.frame.setStyleSheet("background-color: transparent;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.addCourseBtn = QtWidgets.QPushButton(self.frame)
        self.addCourseBtn.setStyleSheet("background-color: white;")
        self.addCourseBtn.setObjectName("addCourseBtn")
        self.verticalLayout.addWidget(self.addCourseBtn)
        self.addAsgnTypeBtn = QtWidgets.QPushButton(self.frame)
        self.addAsgnTypeBtn.setStyleSheet("background-color: white;")
        self.addAsgnTypeBtn.setObjectName("addAsgnTypeBtn")
        self.verticalLayout.addWidget(self.addAsgnTypeBtn)
        self.addGradeBtn = QtWidgets.QPushButton(self.frame)
        self.addGradeBtn.setStyleSheet("background-color: white;")
        self.addGradeBtn.setObjectName("addGradeBtn")
        self.verticalLayout.addWidget(self.addGradeBtn)
        self.changeGradeBtn = QtWidgets.QPushButton(self.frame)
        self.changeGradeBtn.setStyleSheet("background-color: white;")
        self.changeGradeBtn.setObjectName("changeGradeBtn")
        self.verticalLayout.addWidget(self.changeGradeBtn)
        self.curGradeBtn = QtWidgets.QPushButton(self.frame)
        self.curGradeBtn.setStyleSheet("background-color: white;")
        self.curGradeBtn.setObjectName("curGradeBtn")
        self.verticalLayout.addWidget(self.curGradeBtn)
        self.logoutBtn = QtWidgets.QPushButton(self.frame)
        self.logoutBtn.setStyleSheet("background-color: white;")
        self.logoutBtn.setObjectName("logoutBtn")
        self.verticalLayout.addWidget(self.logoutBtn)

        self.gridLayout_3.addWidget(self.frame, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.MenuPage)
        self.gridLayout_2.addWidget(self.stackedWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GradeyPy"))
        self.pwordInput.setPlaceholderText(_translate("MainWindow", "Password"))
        self.exitBtn.setText(_translate("MainWindow", "Exit"))
        self.loginBtn.setText(_translate("MainWindow", "Login"))
        self.unameInput.setPlaceholderText(_translate("MainWindow", "Username"))
        self.appTitle.setText(_translate("MainWindow", "GradeyPy Login"))
        self.welcomeLabel.setText(_translate("MainWindow", "Welcome, y/n"))
        self.addCourseBtn.setText(_translate("MainWindow", "Add Course"))
        self.addAsgnTypeBtn.setText(_translate("MainWindow", "Add Assignment Type"))
        self.addGradeBtn.setText(_translate("MainWindow", "Add Grade"))
        self.changeGradeBtn.setText(_translate("MainWindow", "Change Grade"))
        self.curGradeBtn.setText(_translate("MainWindow", "Current Grades"))
        self.logoutBtn.setText(_translate("MainWindow", "Logout"))

    def getuname(self):
        return self.unameInput.text()

    def getpword(self):
        return self.pwordInput.text()
    
    def getwelcomelbl(self):
        return self.welcomeLabel
    
    def getpageManager(self):
        return self.stackedWidget
