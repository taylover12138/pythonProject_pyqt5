# -*-coding:utf-8-*-
'''
4种回显模式
1.Normal(普通模式)
2.NoECho(不回显)
3.Password(密码模式)
4.PasswordEchoOnEdit(高级密码模式)
'''
from PyQt5.QtWidgets import *
import sys

class QLineEdit_EchoMOde(QWidget):
    def __init__(self):
        super(QLineEdit_EchoMOde,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('文本输入框回显模式')
        formatLayout = QFormLayout()

        normalLineEdit = QLineEdit()
        noEchoLineEdit =QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnEditLineEdit = QLineEdit()

        formatLayout.addRow("Normal",normalLineEdit)
        formatLayout.addRow("NoEcho",noEchoLineEdit)
        formatLayout.addRow("Password",passwordLineEdit)
        formatLayout.addRow("PasswordEchoOnEdit",passwordEchoOnEditLineEdit)
#设置placeholdertext
        normalLineEdit.setPlaceholderText("Normal")
        noEchoLineEdit.setPlaceholderText("NoEcho")
        passwordLineEdit.setPlaceholderText("Password")
        passwordEchoOnEditLineEdit.setPlaceholderText("PasswordEchoOnEdit")
#设置功能
        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formatLayout)
if __name__=="__main__":
    app=QApplication(sys.argv)
    main=QLineEdit_EchoMOde()
    main.show()
    sys.exit(app.exec())