import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage, QWebEngineProfile
from PyQt5.QtCore import QUrl, QStandardPaths

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Example")
        self.setGeometry(100, 100, 1200, 800)

        storage_path = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
        os.makedirs(storage_path, exist_ok=True)

        self.profile = QWebEngineProfile("MyBrowserProfile", self)
        self.profile.setPersistentCookiesPolicy(QWebEngineProfile.ForcePersistentCookies)
        self.profile.setPersistentStoragePath(storage_path)

        self.page = QWebEnginePage(self.profile, self)

        self.browser = QWebEngineView()
        self.browser.setPage(self.page)
        self.browser.setUrl(QUrl("http://127.0.0.1:3001"))
        self.setCentralWidget(self.browser)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Browser()
    window.show()
    sys.exit(app.exec_())
