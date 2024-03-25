import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

Ui_MainWindow, QtBaseClass = uic.loadUiType("./mainwindow.ui")

# at first convert qrc to py from 'pyrcc5 resources.qrc -o resources.py'
import resources

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.webview = QWebEngineView()
        self.url = QUrl("qrc:/map.html")
        self.webview.page().load(self.url)
        self.ui.verticalLayout.addWidget(self.webview)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()

    sys.exit(app.exec_())
