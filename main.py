import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(320, 140))    
        self.setWindowTitle("Vets n Pets") 

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Username:')
        self.line = QLineEdit(self)

        self.line.move(90, 20)
        self.line.resize(200, 30)
        self.nameLabel.move(20, 20)

        self.passLabel = QLabel(self)
        self.passLabel.setText('Password:')
        self.line = QLineEdit(self)

        self.line.move(90, 60)
        self.line.resize(200, 30)
        self.passLabel.move(20, 60)

        loginButton = QPushButton('Login', self)
        loginButton.clicked.connect(self.loginkMethod)
        loginButton.move(20, 100)        
        loginButton.resize(120,30)
        
        exitButton = QPushButton('Exit', self)
        exitButton.clicked.connect(self.exitMethod)
        exitButton.move(180, 100)        
        exitButton.resize(120,30)


    def loginkMethod(self):
        print('Your name: ' + self.line.text())

    def exitMethod(self):
        sys.exit()

app = QtWidgets.QApplication([])
mainWin = MainWindow()
mainWin.show()
app.exec_()