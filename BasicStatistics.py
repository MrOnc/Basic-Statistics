#Sayfa düzen yapılacak
#Malzeme ve stok pencersine tıladığımda açılan penverede EOQ , Yeniden sipariş bnoktası blablabla seçmek için bir encere daha çıakcak.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout, QGroupBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import numpy as np
class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.setWindowTitle("Giriş")
        self.setWindowIcon(QIcon("icon.png"))
        self.setGeometry(400, 200, 300, 150)

        layout = QVBoxLayout()
        form_layout = QFormLayout()

        self.username = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)

        form_layout.addRow("Kullanıcı Adı:", self.username)
        form_layout.addRow("Şifre:", self.password)

        self.login_button = QPushButton("Giriş")
        self.login_button.clicked.connect(self.login)

        layout.addLayout(form_layout)
        layout.addWidget(self.login_button)
        self.setLayout(layout)

    def login(self):
        username = self.username.text()
        password = self.password.text()

        if username == "Onc" and password == "OncOnc":
            self.accept()
        else:
            self.username.clear()
            self.password.clear()
class IstatistikselHesaplamalar(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Temel İstatistiksel Hesaplamalar")
        self.setGeometry(450, 300, 400, 200)

        layout = QVBoxLayout()

        self.input_label = QLabel("Veri Giriniz (Virgülle Ayrılmış):")
        self.input_line = QLineEdit()

        self.calculate_button = QPushButton("Hesapla")
        self.calculate_button.clicked.connect(self.calculate_statistics)

        self.result_label = QLabel("Sonuçlar:")

        layout.addWidget(self.input_label)
        layout.addWidget(self.input_line)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate_statistics(self):
        data = [float(x.strip()) for x in self.input_line.text().split(',')]
        mean = np.mean(data)
        std_dev = np.std(data)
        variance = np.var(data)
        mode = self.calculate_mode(data)
        median = np.median(data)
        sigma2 = variance*2
        sigma3 = variance*3
        sigma4 = variance*4
        sigma5 = variance*5
        sigma6 = variance*6

        results = f"Girdiler: {data} \nOrtalama: {mean}\nStandart Sapma: {std_dev}\nVaryans: {variance}\nMod: {mode}\nMedyan: {median} \n2sigma : {sigma2} \n3sigma {sigma3}\n4sigma {sigma4} \n5sigma {sigma5} \n6sigma {sigma6}"
        self.result_label.setText("Sonuçlar:\n" + results)

    def calculate_mode(self, data):
        (values, counts) = np.unique(data, return_counts=True)
        index = np.argmax(counts)
        return values[index]
class MalzemeVeStok(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Malzeme ve Stok")
        self.setGeometry(450, 300, 400, 350)

        layout = QVBoxLayout()
        form_layout = QFormLayout()

        self.talep = QLineEdit()
        self.siparis_maliyeti = QLineEdit()
        self.elde_tutma_maliyeti = QLineEdit()
        self.sure = QLineEdit()

        form_layout.addRow("Talep (D):", self.talep)
        form_layout.addRow("Sipariş Maliyeti (S):", self.siparis_maliyeti)
        form_layout.addRow("Elde Tutma Maliyeti (H):", self.elde_tutma_maliyeti)
        form_layout.addRow("Süre (T):", self.sure)

        self.eoq_button = QPushButton("EOQ")
        self.eoq_button.clicked.connect(self.calculate_eoq)

        self.tc_button = QPushButton("Total Cost")
        self.tc_button.clicked.connect(self.calculate_total_cost)

        self.tbo_button = QPushButton("TBO")
        self.tbo_button.clicked.connect(self.calculate_tbo)

        self.result_label = QLabel("Sonuçlar:")

        layout.addLayout(form_layout)
        layout.addWidget(self.eoq_button)
        layout.addWidget(self.tc_button)
        layout.addWidget(self.tbo_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate_eoq(self):
        talep = float(self.talep.text())
        siparis_maliyeti = float(self.siparis_maliyeti.text())
        elde_tutma_maliyeti = float(self.elde_tutma_maliyeti.text())

        eoq = ((2 * talep * siparis_maliyeti) / elde_tutma_maliyeti) ** 0.5

        self.result_label.setText(f"Sonuç: EOQ = {eoq}")
        return eoq

    def calculate_total_cost(self):
        eoq = self.calculate_eoq()
        talep = float(self.talep.text())
        siparis_maliyeti = float(self.siparis_maliyeti.text())
        elde_tutma_maliyeti = float(self.elde_tutma_maliyeti.text())

        total_cost = (eoq / 2 * elde_tutma_maliyeti) + (talep / eoq * siparis_maliyeti)

        self.result_label.setText(f"Sonuçlar:\nEOQ = {eoq}\nTotal Cost = {total_cost}")
    
    def calculate_tbo(self):
        eoq = self.calculate_eoq()
        talep = float(self.talep.text())
        sure = float(self.sure.text())

        tbo = (eoq / talep) * sure

        self.result_label.setText(f"Sonuçlar:\nEOQ = {eoq}\nTBO = {tbo}")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Hesaplama Uygulaması")
        self.setWindowIcon(QIcon("icon.png"))
        self.setGeometry(500, 200, 300, 150)

        self.statusBar().showMessage("Hoşgeldiniz!")

        self.btn_istatistiksel = QPushButton("İstatistiksel Hesaplamalar", self)
        self.btn_istatistiksel.clicked.connect(self.open_statistical_calculator)
        self.btn_istatistiksel.resize(self.btn_istatistiksel.sizeHint())
        self.btn_istatistiksel.move(50, 50)

        self.btn_malzemestok = QPushButton("Malzeme ve Stok", self)
        self.btn_malzemestok.clicked.connect(self.open_material_stock)
        self.btn_malzemestok.resize(self.btn_malzemestok.sizeHint())
        self.btn_malzemestok.move(50, 100)

    def open_statistical_calculator(self):
        self.dialog = IstatistikselHesaplamalar()
        self.dialog.exec_()

    def open_material_stock(self):
        self.dialog = MalzemeVeStok()
        self.dialog.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    login_dialog = LoginDialog()
    if login_dialog.exec_() == QDialog.Accepted:
        main_window = MainWindow()
        main_window.show()
        sys.exit(app.exec_())


