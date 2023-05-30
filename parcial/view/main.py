from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


from convert import dec2bin, dec2hex, bin2dec, hex2dec


class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initGui()


    def initGui(self):
        uic.loadUi('ui/parcial.ui',self)
        self.show()

        self.calculate.clicked.connect(lambda: self.calculo())
        self.error.setVisible(False)
        self.error_un.setVisible(False)


    def calculo(self):
        self.error.setVisible(False)
        self.error_un.setVisible(False)
        
        try:
            number = self.numero.text()

            if self.dec2bin.isChecked():
                res = str( dec2bin( int( number ) ) )
                self.resultado.setText( res )

            elif self.dec2hex.isChecked():
                res = str( dec2hex( int( number ) ) )
                self.resultado.setText( res )

            elif self.bin2dec.isChecked():
                res = str( bin2dec( int( number ) ) )
                self.resultado.setText( res )

            elif self.hex2dec.isChecked():
                res = str( hex2dec( number ) )
                self.resultado.setText( res )


        except ValueError:
            self.error.setVisible(True)
            print("Número ingresado o resultado no válido")


        except Exception as e:
            self.error_un.setVisible(True)
            print("Algo salió mal" + str(e))
