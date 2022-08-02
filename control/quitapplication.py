# -*-coding:utf-8-*-
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QMainWindow,QPushButton,QHBoxLayout#水平布局

class quitapplication(QMainWindow):
    def __init__(self):
        super(quitapplication,self).__init__()
        self.resize(300,120)
        self.setWindowTitle('退出应用程序')
        #添加button
        self.button1=QPushButton('退出应用程序')
        self.button1.clicked.connect(self.on_click_button)
        layout=QHBoxLayout()
        layout.addWidget(self.button1)#按钮放在布局上
        mainFrame=QWidget()
        mainFrame.setLayout(layout)#布局放在框架上
        self.setCentralWidget(mainFrame)#框架放在窗口上
    #按钮单击事件的方法(自定义的槽）
    def on_click_button(self):
        sender=self.sender()#用于链接按钮
        print(sender.text()+'按钮被按下')
        app=QApplication.instance()
        app.quit()
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=quitapplication()
    main.show()
    sys.exit(app.exec())