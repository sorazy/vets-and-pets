import sys
from loginScreen import loginScreen
from createUser import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets
import database as db

class Main(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__()
        
        # build ui
        self.ui = loginScreen()
        self.ui.setupUi(self)

        # connect signals
        self.ui.pushButton.clicked.connect(self.on_login_button)
        self.ui.pushButton_2.clicked.connect(self.on_singup_button)
        self.ui.pushButton_3.clicked.connect(self.on_exit_button)

    def on_singup_button(self):
        self.dialog = Ui_MainWindow()
        self.dialog.setupUi(self.dialog)
        self.dialog.show()   

        self.dialog.pushButton.clicked.connect(self.on_register_button)
        self.dialog.pushButton_2.clicked.connect(self.on_back_button)

    def on_exit_button(self):
        sys.exit()

    def on_back_button(self):
        self.dialog.close()
    
    def on_register_button(self):
        u = self.dialog.lineEdit.text()
        p = self.dialog.lineEdit_2.text()
        e = self.dialog.lineEdit_3.text()
        n = self.dialog.lineEdit_4.text()

        db.createUser(u, p, e, n)

    def on_login_button(self):
        if db.contains(self.ui.lineEdit.text(), self.ui.lineEdit_2.text()):
            print("it is there")
        else:
            print("it's not in the database")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())