# -*-coding:utf-8-*-
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget


class centerWin(QMainWindow):
    def __init__(self):
        super(centerWin,self).__init__()

        #设置主窗口应用
        self.setWindowTitle('窗口应用居中')
        #设置窗口尺寸
        self.resize(400,300)
    def center(self):
        #获取屏幕坐标系
        screen=QDesktopWidget().screenGeometry()
        #获取窗口坐标系
        size=self.geometry()
        newleft=(screen.width()-size.width())/2
        newtop=(screen.height()-size.height())/2
        self.move(newleft,newtop)
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=centerWin()
    main.show()
    sys.exit(app.exec())