import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from funcao import *
from designer import Ui_MainWindow

'''Para funcionamento do programa é preciso instalar pyqt5, pygame, webbrowser, playsound.
   Para edição da interface instale Qtdesigner
   Caso deseja criar um executável com esse programa leia o README'''


class novo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        # Funções caso o botão seja clicado
        if self.btngoogle.clicked:
            # Imagem que irá aparecer no label
            self.btngoogle.clicked.connect(
                lambda: self.labelimg.setStyleSheet('background-image: url(img/googlep.jpg)'))
            # Abrir página
            self.btngoogle.clicked.connect(lambda: google())
            # Sai som
            self.btngoogle.clicked.connect(lambda: goo())
        if self.btnyoutube.clicked:
            self.btnyoutube.clicked.connect(
                lambda: self.labelimg.setStyleSheet('background-image: url(img/youtubep.jpg)'))
            self.btnyoutube.clicked.connect(lambda: youtube())
            self.btnyoutube.clicked.connect(lambda: you())
        if self.btntwitch_2.clicked:
            self.btntwitch_2.clicked.connect(
                lambda: self.labelimg.setStyleSheet('background-image: url(img/twitchp.jpg)'))
            self.btntwitch_2.clicked.connect(lambda: twitch())
            self.btntwitch_2.clicked.connect(lambda: twi())
        if self.btnnetflix.clicked:
            self.btnnetflix.clicked.connect(
                lambda: self.labelimg.setStyleSheet('background-image: url(img/netflixp.jpg)'))
            self.btnnetflix.clicked.connect(lambda: netflix())
            self.btnnetflix.clicked.connect(lambda: net())
        if self.btnamazom.clicked:
            self.btnamazom.clicked.connect(
                lambda: self.labelimg.setStyleSheet('background-image: url(img/amazomp.jpg)'))
            self.btnamazom.clicked.connect(lambda: prime())
            self.btnamazom.clicked.connect(lambda: pri())
        if self.btndisney.clicked:
            self.btndisney.clicked.connect(
                lambda: self.labelimg.setStyleSheet('background-image: url(img/disneyp.jpg)'))
            self.btndisney.clicked.connect(lambda: disney())
            self.btndisney.clicked.connect(lambda: dis())
        # Estilização do label e botões
        self.setStyleSheet('background: black')
        self.btnnetflix.setStyleSheet('background: white; color:#E70906; font-weight: 1000;font-size:14px')
        self.labelimg.setStyleSheet('background-image: url(img/t1.jpg)')
        self.btngoogle.setStyleSheet('background: white; color:#CB8110; font-weight: 1000;font-size:14px')
        self.btntwitch_2.setStyleSheet('background: white; color:purple; font-weight: 1000;font-size:14px')
        self.btndisney.setStyleSheet('background: white; color:#0660CB; font-weight: 1000;font-size:14px')
        self.btnamazom.setStyleSheet('background: white; color:#1F8A97; font-weight: 1000;font-size:14px')
        self.btnyoutube.setStyleSheet('background: white; color:#C20E0B; font-weight: 1000;font-size:14px')


# Iniciamento


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = novo()
    novo.show()
    qt.exec_()

'''Autor do icon <a href="https://www.flaticon.com/br/icones-gratis/serpente" 
           title="serpente ícones">Serpente ícones criados por Freepik - Flaticon</a>'''
