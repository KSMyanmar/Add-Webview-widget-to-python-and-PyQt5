import sys
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication


app = QApplication(sys.argv)
web = QWebEngineView()
web.load(QUrl("https://build-system.fman.io/qt-designer-download"))
web.show()


sys.exit(app.exec_())
