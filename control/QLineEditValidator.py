# -*-coding:utf-8-*-
'''
(校验器)限制只能输入整数，浮点数或满足一定条件的字符串
'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator #引用校验器QRegExp我们所输入的需要满足正则表达式
from PyQt5.QtCore import QRegExp#引入正则表达式
import sys
class QlineEditValidetor(QWidget):
    def __init__(self):
        super(QlineEditValidetor,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('校验器')

        formLayout=QFormLayout()

        intLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()
        regexpLineEdit = QLineEdit()

        formLayout.addRow('整数类型',intLineEdit)
        formLayout.addRow('浮点类型',doubleLineEdit)
        formLayout.addRow('数字和字母',regexpLineEdit)

        intLineEdit.setPlaceholderText('整型')
        doubleLineEdit.setPlaceholderText('浮点型')
        regexpLineEdit.setPlaceholderText('数字或字母')
        #整数校验器
        intValidator=QIntValidator(self)
        intValidator.setRange(1,99)
        #浮点校验器
        doubleValidator=QDoubleValidator(self)
        doubleValidator.setRange(-360,360)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        doubleValidator.setDecimals(2)#设置精度,小数点两位
        #字符和数字
        reg=QRegExp('[a-zA-Z0-9]+$')#正则表达式
        regValidator=QRegExpValidator(self)
        regValidator.setRegExp(reg)
        #设置校验器
        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        regexpLineEdit.setValidator(regValidator)
        self.setLayout(formLayout)
if __name__=="__main__":
    app=QApplication(sys.argv)
    main=QlineEditValidetor()
    main.show()
    sys.exit(app.exec())