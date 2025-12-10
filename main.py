from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from pyshorteners import Shortener
from PyQt5.QtCore import pyqtSlot

def CREATE_SHORT_URL(url):
    link = Shortener()
    return link.tinyurl.short(url)


class QrCodeBuilder(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("interface.ui", self)

    def getURL(self):
        return self.txtUrl.text()
    
    def setURLCurta(self, url):
        self.txtUrlShort.setText(url)

    @pyqtSlot()
    def on_btnGerar_clicked(self):
        valor = self.getURL()
        if valor:
            url = CREATE_SHORT_URL(valor)
            self.setURLCurta(url)
            
        else:
            self.showMessage("Errou", "Voce esquece de alguma coisa?")

    
    def showMessage(self, title, message):
        QMessageBox.information(self, title, message)



# -----------------------------
if __name__ == "__main__":
    app = QApplication([])
    window = QrCodeBuilder()
    window.show()
    app.exec_()