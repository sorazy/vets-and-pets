import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    
from createUser import SignupWindow
import database

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(320, 140))    
        self.setWindowTitle("Vets n Pets") 

        self.usernameLabel = QLabel(self)
        self.usernameLabel.setText('Username:')
        self.usernameLine = QLineEdit(self)

        self.usernameLine.move(90, 20)
        self.usernameLine.resize(200, 30)
        self.usernameLabel.move(20, 20)

        self.passwordLabel = QLabel(self)
        self.passwordLabel.setText('Password:')
        self.passwordLine = QLineEdit(self)

        self.passwordLine.move(90, 60)
        self.passwordLine.resize(200, 30)
        self.passwordLabel.move(20, 60)

        self.loginButton = QPushButton('Login', self)
        self.loginButton.clicked.connect(self.on_loginButton_clicked)
        self.dialog = SignupWindow(self)
        self.loginButton.move(20, 100)        
        self.loginButton.resize(120,30)
        
        self.exitButton = QPushButton('Signup', self)
        self.exitButton.clicked.connect(self.exitMethod)
        self.exitButton.move(180, 100)        
        self.exitButton.resize(120,30)

    def on_loginButton_clicked(self):
        self.dialog.show()

    def exitMethod(self):
        sys.exit()

try:
    database.createTable()
except:
    print("Table already exists. Continuing normally.")

app = QtWidgets.QApplication([])
mainWin = MainWindow()
mainWin.show()
app.exec_()