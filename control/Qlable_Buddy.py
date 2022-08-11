# -*-coding:utf-8-*-
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QDialog, QLineEdit,QPushButton,QGridLayout
import sys

class QLabelBuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("QLabel与伙伴关系")
        nameLabel=QLabel('&Name',self)
        nameLineEdit=QLineEdit(self)
        nameLabel.setBuddy(nameLineEdit)#设置伙伴

        passwordsLabel=QLabel('&Passwords',self)
        passwordsLineEdit = QLineEdit(self)
        passwordsLabel.setBuddy(passwordsLineEdit)

        btnOK=QPushButton('&OK')
        btnCancel=QPushButton('&Cancel')

        mainLayout=QGridLayout(self)
        mainLayout.addWidget(nameLabel,0,0)#一行一列
        mainLayout.addWidget(nameLineEdit,0,1,1,2)#一行二列1行宽2列宽
        mainLayout.addWidget(passwordsLabel,1,0)
        mainLayout.addWidget(passwordsLineEdit,1,1,1,2)
        mainLayout.addWidget(btnOK,2,1)
        mainLayout.addWidget(btnCancel,2,2)
if __name__ =='__main__':
    app=QApplication(sys.argv)
    main=QLabelBuddy()
    main.show()
    sys.exit(app.exec())