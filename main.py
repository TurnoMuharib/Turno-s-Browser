from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #navbar
        navbar= QToolBar()
        self.addToolBar(navbar)


        #back
        back_btn =QAction('Back',self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)
        #Reload
        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)
        #Home
        home_btn=QAction('Home',self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # Yotube
        yt_btn = QAction('YouTube', self)
        yt_btn.triggered.connect(self.youtube_buttoon)
        navbar.addAction(yt_btn)
        # Instagram
        ig_btn = QAction('Instagram', self)
        ig_btn.triggered.connect(self.instagram_buttoon)
        navbar.addAction(ig_btn)

        #url bar
        self.url_bar =QLineEdit()
        navbar.addWidget(self.url_bar)
        self.url_bar.returnPressed.connect(self.navigate_to_url)


    def navigate_to_url(self):
        url =self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def instagram_buttoon(self):
        self.browser.setUrl(QUrl('http://www.instagram.com'))


    def youtube_buttoon(self):
       self.browser.setUrl(QUrl('http://www.youtube.com'))


    def navigate_home(self):
     self.browser.setUrl(QUrl("http://google.com"))

app =QApplication(sys.argv)
QApplication.setApplicationName('Muharib Internet')
window=MainWindow()
app.exec()


