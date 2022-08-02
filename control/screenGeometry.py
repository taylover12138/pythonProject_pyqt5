# -*-coding:utf-8-*-
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QHBoxLayout,QMainWindow,QPushButton
def clickbutton():
    print("click")
    print("widget'sx=%d"% widget.x())#[窗口坐标]geometry.x()[工作区坐标],FrameGeometry.x()[窗口坐标]
    print("widget'sy=%d"% widget.y())
    print("widget'width=%d"% widget.width())#[工作区高宽]geometry.width()[工作区高宽],FrameGeometry.width()[窗口高宽]
    print("widget'sheight=%d"% widget.height())
app=QApplication(sys.argv)
widget=QWidget()
btn=QPushButton(widget)
btn.setText("按钮")
btn.clicked.connect(clickbutton)

btn.move(24,52)
widget.resize(300,200)
widget.move(250,200)
widget.setWindowTitle('屏幕坐标系')
widget.show()
sys.exit(app.exec())