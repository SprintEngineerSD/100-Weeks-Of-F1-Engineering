#checkboxes,radio button, line edits, CSS styles
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton  # QCheckBox
from PyQt5.QtCore import Qt



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)
    #    self.checkbox = QCheckBox("Do you like food?", self)
        self.initUI()


    def initUI(self):
        self.line_edit.setGeometry(10,10,200,40)
        self.button.setGeometry(210,10,100,40)
        self.line_edit.setStyleSheet("font-size: 25px;"
                                     "font-family: Arial;")
        self.button.setStyleSheet("font-size: 25px;"
                                     "font-family: Arial;")
        self.button.clicked.connect(self.submit)
        self.line_edit.setPlaceholderText("Enter your name")


    def submit(self):
        text = self.line_edit.text()
        print(f"Hello {text}")


    #    self.checkbox.setGeometry(10,0,500,100)
    #    self.checkbox.setStyleSheet("font-size: 30px;"
    #                                "font-family: Ariel;")
    #    self.checkbox.setChecked(False)
    #    self.checkbox.stateChanged.connect(self.checkbox_changed)

    #def checkbox_changed(self,state):
    #    if state == Qt.Checked:
    #        print("You like food")
    #    else:
    #        print("You dont like food")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())