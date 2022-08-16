# -*-coding:utf-8-*-
from PyQt5.QtWidgets import *
import sys

class QtextEditDemo(QWidget):
    def __init__(self):
        super(QtextEditDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('textEdit控件演示')
        self.resize(300,280)
        self.textEdit=QTextEdit()
        self.buttonText=QPushButton('显示文本')
        self.buttonHTML=QPushButton('显示HTML')
        self.buttonToText=QPushButton('获取文本')
        self.buttonToHTML=QPushButton('获取HTML')
        layout=QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.buttonText)
        layout.addWidget(self.buttonHTML)
        layout.addWidget(self.buttonToText)
        layout.addWidget(self.buttonToHTML)
        self.setLayout(layout)
        #链接槽
        self.buttonText.clicked.connect(self.onClick_ButtonText)
        self.buttonHTML.clicked.connect(self.onClick_ButtonHTML)
        self.buttonToText.clicked.connect(self.onClick_ButtonToText)
        self.buttonToHTML.clicked.connect(self.onClick_buttonToHTML)
    #建槽
    def onClick_ButtonText(self):
        self.textEdit.setPlainText('hello world,世界你好')
    def onClick_ButtonHTML(self):
        self.textEdit.setHtml('<font color="blue"size="5">hello world</font>')
    def onClick_ButtonToText(self):
        print(self.textEdit.toPlainText())
    def onClick_buttonToHTML(self):
        print(self.textEdit.toHtml())
if __name__=="__main__":
    app=QApplication(sys.argv)
    main=QtextEditDemo()
    main.show()
    sys.exit(app.exec())