from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
from pyshorteners import Shortener
from PyQt5.QtCore import pyqtSlot
import qrcode
from os import path

def CREATE_SHORT_URL(url):
    link = Shortener()
    return link.tinyurl.short(url)

def CREATE_QRCODE(link):
    img = qrcode.make(link)
    img.save("qrcode.png")

def GET_LOCAL_PATH(myPath):
    return f''




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
            CREATE_QRCODE(url)
            self.setURLCurta(url)
            self.img.setPixmap(QPixmap("qrcode.png"))
            self.btnSalvar.setEnabled(True)
            
        else:
            self.showMessage("Errou", "Voce esquece de alguma coisa?")

    @pyqtSlot()
    def on_btnSalvar_clicked(self):
        self.salvar()

    def salvar(self):
        nomeArquivo, _ = QFileDialog.getSaveFileName(self, "Salvar Imagem")
        if nomeArquivo:
            caminho = path.dirname(nomeArquivo)
            nome = nomeArquivo.removeprefix(caminho)

            # ler a foto do QRCODE
            with open("qrcode.png", "rb") as fotoQrcode:
                dadosQrcode = fotoQrcode.read()

            # salvar a foto aonde o user escolheu
            with open(caminho+f"{nome}.png", "wb") as foto:
                foto.write(dadosQrcode)
            

    def showMessage(self, title, message):
        QMessageBox.information(self, title, message)



# -----------------------------
if __name__ == "__main__":
    app = QApplication([])
    window = QrCodeBuilder()
    window.show()
    app.exec_()