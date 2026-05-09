#PyQt5 introduction
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget,
                             QVBoxLayout,QHBoxLayout,QGridLayout, QPushButton)

#from PyQt5.QtGui import QFont
#from PyQt5.QtCore import Qt
#from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700,300,500,500)
        self.button = QPushButton("click me!", self)
        #label = QLabel(self)
        self.initUI()


    def initUI(self):
        self.button.setGeometry(150,200,200,70)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)
        self.label = QLabel("Hello", self)

        self.label.setGeometry(150,300,200,100)
        self.label.setStyleSheet("font-size: 40px;")

    def on_click(self):
        self.label.setText("Goodbye!")
        print("button clicked!")
        self.button.setText("Clicked!")
        # self.button.setDisabled(True) 



        #label.setFont(QFont("Ariel", 30))
        #label.setGeometry(0,0,250,250)
        #label.setStyleSheet("color: #910001;"
        #                    "background-color: #6fdcf7;"
        #                    "font-weight: bold;"
        #                    "font-style: Italic;"
        #                    "text-decoration: underline;")

        #label.setAlignment(Qt.AlignTop)
        #label.setAlignment(Qt.AlignBottom)
        #label.setAlignment(Qt.AlignVCenter)
        #label.setAlignment(Qt.AlignRight)
        #label.setAlignment(Qt.AlignLeft)
        #label.setAlignment(Qt.AlignHCenter)
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)


        #pixmap = QPixmap("Screenshot (2).png")
        #label.setPixmap(pixmap)
        #label.setScaledContents(True)
        #label.setGeometry((self.width() - label.width()) // 2,
        #                  (self.height() - label.height())// 2,
        #                  label.width(),
        #                  label.height())


    #def initUI(self):
        #central_widget = QWidget()
        #self.setCentralWidget(central_widget)

        #label1 = QLabel("#1",self)
        #label2 = QLabel("#2",self)
        #label3 = QLabel("#3",self)
        #label4 = QLabel("#4",self)
        #label5 = QLabel("#5",self)

        #label1.setStyleSheet("background-color: red")
        #label2.setStyleSheet("background-color: green")
        #label3.setStyleSheet("background-color: yellow")
        #label4.setStyleSheet("background-color: lime")
        #label5.setStyleSheet("background-color: blue")
        #vbox = QVBoxLayout()
        #vbox.addWidget(label1)
        #vbox.addWidget(label2)
        #vbox.addWidget(label3)
        #vbox.addWidget(label4)
        #vbox.addWidget(label5)

        #hbox.addWidget(label1) We can also use hbox and grid system for the gui
        #grid.addWidget(label1,0,1)

        #central_widget.setLayout(vbox)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()