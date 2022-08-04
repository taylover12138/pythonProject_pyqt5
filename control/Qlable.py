# -*-coding:utf-8-*-

'''
Qlable常用事件：
1. 当鼠标划过Qlable时触发：LinkHovered
2. 当鼠标点击Qlable时出发：LinkActivated
待解决：setAlignment()没有用
'''
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QLabel, QMainWindow, QVBoxLayout
from PyQt5.QtGui import QPalette,QPixmap#绘画板和离屏图像显示
from PyQt5 import QtCore#常量

class qlabel(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600,500)
        self.initUI()
    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        # label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color=yellow>这是一个文本标签.</font>")
        label1.setAutoFillBackground(True)#自动添加背景
        palette = QPalette()
        palette.setColor(QPalette.Window,QtCore.Qt.blue)#设置背景色
        label1.setPalette(palette)

        label1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)#对其方式排列剧中

        label2.setText("<a href='#'>欢迎使用Python GUI程序</a>")

        # label3.setAlignment(Qt.AlignCenter)
        #
        # label3.setToolTip('这是一个图片标签')
        # label3.setPixmap(QPixmap("./images/016bd356de84bc32f875520fe641e2.png@1280w_1l_2o_100sh.png"))
        label4.setOpenExternalLinks(True)#Ture点击触发超链接False触发事件
        label4.setText("<a href='https://item.jd.com/12417265.html'>感谢关注《Python从菜鸟到高手》</a>")
        label4.setAlignment(QtCore.Qt.AlignRight)
        label4.setToolTip('这是一个超级链接')

        vbox=QVBoxLayout()#垂直布局
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        # vbox.addWidget(label3)
        vbox.addWidget(label4)



        #信号与槽
        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)
    def linkHovered(self):
        print("当鼠标滑过label2时，触发事件")
    def linkClicked(self):
        print("当鼠标点击label4时，触发事件")
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=qlabel()
    main.show()
    sys.exit(app.exec())