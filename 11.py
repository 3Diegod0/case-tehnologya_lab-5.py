import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox


class MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("mainwindow.ui", self)

        # Подключите сигналы и слоты
        self.pushButton.clicked.connect(self.button_clicked)
        self.pushButton_2.clicked.connect(self.close)

    def button_clicked(self):
        if self.lineEdit.text() and self.lineEdit_2.text() and self.lineEdit_3.text() and self.lineEdit_4.text() and self.lineEdit_5.text() and self.lineEdit_6.text() and self.lineEdit_7.text() and self.lineEdit_8.text():
            QMessageBox.information(self, "Покупка", "Товар куплен")
        else:
            QMessageBox.warning(self, "Ошибка", "Заполните все строки формы")

    def show(self):
        super(MainWindow, self).show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())