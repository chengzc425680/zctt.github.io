import sys
from PyQt5.QtWidgets import(QWidget,QPushButton,QApplication)
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):

        btn = QPushButton('BUTTON',self)
        btn.clicked(QCoreApplication.instance().quit)

        btn.resize(btn.sizeHint())
        btn.move(50,50)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('windows')
        self.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())
