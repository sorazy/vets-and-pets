import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    
import database

class SignupWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(320, 140))    
        self.setWindowTitle("Create a New User") 

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

        loginButton = QPushButton('Signup!', self)
        loginButton.clicked.connect(self.on_signupButton_clicked)
        loginButton.move(20, 100)        
        loginButton.resize(120,30)

        exitButton = QPushButton('Back', self)
        exitButton.clicked.connect(self.exitMethod)
        exitButton.move(180, 100)        
        exitButton.resize(120,30)

    def on_signupButton_clicked(self):
        database.createUser(self.usernameLine.text(), self.passwordLine.text())

    def exitMethod(self):
        self.close()