import sys


from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import  uic


class Principal(QMainWindow):
    def __init__(self): 
        super().__init__()
        uic.loadUi("Sesion20/first.ui", self)
        self.setupUi()


    def setupUi(self):
        self.calculate.clicked.connect(self.calulate)
        self.show()


    def calulate(self):
        try:
            first_num = float(self.first_num.text())
            second_num = float(self.second_num.text())

            if self.sum_check.isChecked():
                self.result.setText(str(first_num + second_num))

            elif self.res_check.isChecked():
                self.result.setText(str(first_num - second_num))

            elif self.mult_check.isChecked():
                self.result.setText(str(first_num * second_num))

            elif self.div_check.isChecked():
                self.result.setText(str(first_num / second_num))

        except ValueError:
            print("Value not valid")


def main():
    app = QApplication([])
    _ = Principal()
    sys.exit(app.exec_())


if __name__=="__main__":
    main()
