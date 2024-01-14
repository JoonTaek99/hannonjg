import sys
import time
import PyQt5
import re
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from bs4 import BeautifulSoup
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow
from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.parse import quote_plus
from selenium import webdriver
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl
import urllib.request
from PyQt5.QtGui import QPixmap 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt,QUrl, pyqtSlot
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtWebEngineCore
from PyQt5.QtWebEngineWidgets import QWebEngineSettings

testingui = uic.loadUiType("testing.ui")[0]

class MyWindow(QDialog, testingui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        browser = webdriver.Chrome() 
        url = 'https://www.coupang.com/np/search?component=&q=%EB%82%98%EC%9D%B4%ED%82%A4+%EB%AA%A8%EC%9E%90&channel=user'
        browser.get(url)
        imgs = browser.find_elements_by_class_name('search-product-wrap-img')
        data_prices = browser.find_elements_by_class_name('price-value')
        data_name = browser.find_elements_by_class_name('name')
        Img_results = []
        for i in imgs:     
                Img_results.append(i.get_attribute('src')) 

        self.name_1.setText(data_name[0].text)
        self.name_1.setStyleSheet("Text-align: left")
        self.name_1.setStyleSheet("Font: 9pt Yu Gothic")
        self.price_1.setText(data_prices[0].text + '원')
        self.price_1.setStyleSheet("Text-align: left")
        self.price_1.setStyleSheet("Font: 9pt Yu Gothic")

        def loadImage_1(self):
            urlstring = Img_results[3]
            imageFromWeb = urllib.request.urlopen(urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(251, 121)
            self.photo_1.setPixmap(self.qPixmapWebVar)

        loadImage_1(self)
        
        browser.close()

app = QApplication(sys.argv)
myWindow = MyWindow()
myWindow.show()
app.exec_()