import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

import requests

BASE_URL = 'http://127.0.0.1:8000/'


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("login.ui", self)
        self.login_btn.clicked.connect(self.login_function)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.redirect_signup_btn.clicked.connect(self.redirect_signup_function)

    def login_function(self):
        try:
            username = self.username.text()
            password = self.password.text()

            res = requests.post(
                BASE_URL + 'api-token-auth/', json={"username": username, "password": password})

            data = res.json()
            if res.status_code == 200:
                with open('.token.txt', "w") as f:
                    f.write(data['token'])
            if res.status_code == 400:
                self.server_msg.setText("Incorrect username or password")

        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    def redirect_signup_function(self):
        signup_window = Signup()
        widget.addWidget(signup_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Signup(QDialog):
    def __init__(self):
        super(Signup, self).__init__()
        loadUi("signup.ui", self)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup_btn.clicked.connect(self.signup_function)
        self.redirect_login_btn.clicked.connect(self.redirect_login_function)

    def signup_function(self):
        email = self.username.text()
        if self.password.text() == self.confirm_password.text():
            password = self.password.text()
            print("Signup Success")
            login_window = Login()
            widget.addWidget(login_window)
            widget.setCurrentIndex(widget.currentIndex() + 1)

    def redirect_login_function(self):
        login_window = Login()
        widget.addWidget(login_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


app = QApplication(sys.argv)
mv = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mv)
widget.setFixedWidth(480)
widget.setFixedHeight(620)
widget.show()
app.exec_()
