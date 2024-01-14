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

ui = uic.loadUiType("hannun_main.ui")[0]
uiNext = uic.loadUiType("second_page.ui")[0]
uiReview = uic.loadUiType("Review_page.ui")[0]
H_uiLast = uic.loadUiType("H_last_page.ui")[0]
D_uiLast = uic.loadUiType("D_last_page.ui")[0]
C_uiLast = uic.loadUiType("C_last_page.ui")[0]
G_uiLast = uic.loadUiType("G_last_page.ui")[0]
Y_uiLast = uic.loadUiType("Y_last_page.ui")[0]

H_btncount = 0
H_href = ""
D_btncount = 0
D_href = ""
C_btncount = 0
C_href = ""
G_btncount = 0
G_href = ""
Y_btncount = 0
Y_href = ""

# 첫 번째 UI(통합 검색)
class MyWindow(QDialog, ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        find_text = self.lineEdit.text()
        
        self.btn_Product.clicked.connect(self.NextOpen)
        self.btn_Review.clicked.connect(self.ReviewOpen)
        
    def NextOpen(self):
        Next_Area(self)

    def ReviewOpen(self):
        Review_Area(self)

#두 번째 UI(각 사이트별 매물)
class Next_Area(QDialog, uiNext):
    def __init__(self, parent):
        super(Next_Area, self).__init__(parent)
        self.setupUi(self)
        self.show()

        self.lblTitle.setText(parent.lineEdit.text() + "에 대한 검색결과")
        self.lblTitle.setStyleSheet("Text-align: center")

        # g마켓
        G_options = webdriver.ChromeOptions()
        G_options.add_argument('headless')
        G_browser = webdriver.Chrome(options = G_options)
        G_url = 'https://browse.gmarket.co.kr/search?keyword=' + parent.lineEdit.text()
        G_browser.get(G_url)
        G_browser.execute_script('window.scrollBy(0, 540);')
        time.sleep(1)
        G_browser.execute_script('window.scrollBy(0, 540);')
        time.sleep(1)
        G_browser.execute_script('window.scrollBy(0, 540);')
        time.sleep(1)

        Gmarket_block = G_browser.find_element_by_id('region__content-body')
        G_imgs = Gmarket_block.find_elements_by_class_name('image__item')
        G_href = Gmarket_block.find_elements_by_class_name('box__image')
        G_Href_results = []
        for i in range(9):
            G_Href_results.append(G_href[i].find_element_by_tag_name('a').get_attribute('href'))
        G_Img_results = []
        for i in G_imgs:     
            G_Img_results.append(i.get_attribute('src'))

        G_browser.close()  

        # 각 버튼마다 btncount에 다른 값을 부여, btncount값에 따라 상세설명창에서 띄우는 값 다르게 시도할 것
        def G1_LastOpen(self):  
            global G_btncount
            G_btncount = 0
            global G_href
            G_href = G_Href_results[G_btncount]
            
        def G2_LastOpen(self):  
            global G_btncount
            G_btncount = 1
            global G_href
            G_href = G_Href_results[G_btncount]

        def G3_LastOpen(self):  
            global G_btncount
            G_btncount = 2
            global G_href
            G_href = G_Href_results[G_btncount]

        def G4_LastOpen(self):  
            global G_btncount
            G_btncount = 3
            global G_href
            G_href = G_Href_results[G_btncount]

        def G5_LastOpen(self):  
            global G_btncount
            g_btncount = 4
            global G_href
            G_href = G_Href_results[G_btncount]

        def G6_LastOpen(self):  
            global G_btncount
            G_btncount = 5
            global G_href
            G_href = G_Href_results[G_btncount]

        def G7_LastOpen(self):  
            global G_btncount
            G_btncount = 6
            global G_href
            G_href = G_Href_results[G_btncount]

        def G8_LastOpen(self):  
            global G_btncount
            G_btncount = 7
            global G_href
            G_href = G_Href_results[G_btncount]

        def G9_LastOpen(self):  
            global G_btncount
            G_btncount = 8
            global G_href
            G_href = G_Href_results[G_btncount]

        # g마켓 img 출력
        def G_loadImageFromWeb_01(self):
            G_urlstring = G_Img_results[0]
            G_imageFromWeb = urllib.request.urlopen(G_urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(G_imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.Gmarket_Product_Image_1.setPixmap(self.qPixmapWebVar)

        G_loadImageFromWeb_01(self)
    
        def G_loadImageFromWeb_02(self):
            G_urlstring = G_Img_results[1]
            G_imageFromWeb = urllib.request.urlopen(G_urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(G_imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.Gmarket_Product_Image_2.setPixmap(self.qPixmapWebVar)

        G_loadImageFromWeb_02(self)

        def G_loadImageFromWeb_03(self):
            G_urlstring = G_Img_results[2]
            G_imageFromWeb = urllib.request.urlopen(G_urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(G_imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.Gmarket_Product_Image_3.setPixmap(self.qPixmapWebVar)

        G_loadImageFromWeb_03(self)

        def G_loadImageFromWeb_04(self):
            G_urlstring = G_Img_results[3]
            G_imageFromWeb = urllib.request.urlopen(G_urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(G_imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.Gmarket_Product_Image_4.setPixmap(self.qPixmapWebVar)

        G_loadImageFromWeb_04(self)

        def G_loadImageFromWeb_05(self):
            G_urlstring = G_Img_results[4]
            G_imageFromWeb = urllib.request.urlopen(G_urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(G_imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.Gmarket_Product_Image_5.setPixmap(self.qPixmapWebVar)

        G_loadImageFromWeb_05(self)

        def G_loadImageFromWeb_06(self):
            G_urlstring = G_Img_results[5]
            G_imageFromWeb = urllib.request.urlopen(G_urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(G_imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.Gmarket_Product_Image_6.setPixmap(self.qPixmapWebVar)

        G_loadImageFromWeb_06(self)

        def G_loadImageFromWeb_07(self):
            G_urlstring = G_Img_results[6]
            G_imageFromWeb = urllib.request.urlopen(G_urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(G_imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.Gmarket_Product_Image_7.setPixmap(self.qPixmapWebVar)

        G_loadImageFromWeb_07(self)

        def G_loadImageFromWeb_08(self):
            G_urlstring = G_Img_results[7]
            G_imageFromWeb = urllib.request.urlopen(G_urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(G_imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.Gmarket_Product_Image_8.setPixmap(self.qPixmapWebVar)

        G_loadImageFromWeb_08(self)

        def G_loadImageFromWeb_09(self):
            G_urlstring = G_Img_results[8]
            G_imageFromWeb = urllib.request.urlopen(G_urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(G_imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.Gmarket_Product_Image_9.setPixmap(self.qPixmapWebVar)

        G_loadImageFromWeb_09(self)



        page = requests.get('https://browse.gmarket.co.kr/search?keyword=' + parent.lineEdit.text())
        soup = BeautifulSoup(page.content, 'html.parser')

        G_data_name = soup.find_all('span', class_='text__item')            #상품이름
        G_data_price = soup.find_all('strong', class_='text text__value')   #상품가격


        #상품이름출력
        self.Gmarket_Product_Name_1.setText(str(G_data_name[0].get_text()))
        self.Gmarket_Product_Name_1.setStyleSheet("Text-align: left")
        self.Gmarket_Product_Name_1.setStyleSheet("Font: 9pt Yu Gothic")
        self.Gmarket_Product_Name_1.clicked.connect(G1_LastOpen)
        self.Gmarket_Product_Name_1.clicked.connect(self.G_LastOpen)
        self.Gmarket_Product_Name_2.setText(str(G_data_name[1].get_text()))
        self.Gmarket_Product_Name_2.setStyleSheet("Text-align: left")  
        self.Gmarket_Product_Name_2.setStyleSheet("Font: 9pt Yu Gothic")
        self.Gmarket_Product_Name_2.clicked.connect(G2_LastOpen)
        self.Gmarket_Product_Name_2.clicked.connect(self.G_LastOpen)
        self.Gmarket_Product_Name_3.setText(str(G_data_name[2].get_text()))
        self.Gmarket_Product_Name_3.setStyleSheet("Text-align: left")
        self.Gmarket_Product_Name_3.setStyleSheet("Font: 9pt Yu Gothic")
        self.Gmarket_Product_Name_3.clicked.connect(G3_LastOpen)
        self.Gmarket_Product_Name_3.clicked.connect(self.G_LastOpen)
        self.Gmarket_Product_Name_4.setText(str(G_data_name[3].get_text()))
        self.Gmarket_Product_Name_4.setStyleSheet("Text-align: left")
        self.Gmarket_Product_Name_4.setStyleSheet("Font: 9pt Yu Gothic")
        self.Gmarket_Product_Name_4.clicked.connect(G4_LastOpen)
        self.Gmarket_Product_Name_4.clicked.connect(self.G_LastOpen)
        self.Gmarket_Product_Name_5.setText(str(G_data_name[4].get_text()))
        self.Gmarket_Product_Name_5.setStyleSheet("Text-align: left")  
        self.Gmarket_Product_Name_5.setStyleSheet("Font: 9pt Yu Gothic")
        self.Gmarket_Product_Name_5.clicked.connect(G5_LastOpen)
        self.Gmarket_Product_Name_5.clicked.connect(self.G_LastOpen)
        self.Gmarket_Product_Name_6.setText(str(G_data_name[5].get_text()))
        self.Gmarket_Product_Name_6.setStyleSheet("Text-align: left")
        self.Gmarket_Product_Name_6.setStyleSheet("Font: 9pt Yu Gothic")
        self.Gmarket_Product_Name_6.clicked.connect(G6_LastOpen)
        self.Gmarket_Product_Name_6.clicked.connect(self.G_LastOpen)
        self.Gmarket_Product_Name_7.setText(str(G_data_name[6].get_text()))
        self.Gmarket_Product_Name_7.setStyleSheet("Text-align: left")
        self.Gmarket_Product_Name_7.setStyleSheet("Font: 9pt Yu Gothic")
        self.Gmarket_Product_Name_7.clicked.connect(G7_LastOpen)
        self.Gmarket_Product_Name_7.clicked.connect(self.G_LastOpen)
        self.Gmarket_Product_Name_8.setText(str(G_data_name[7].get_text()))
        self.Gmarket_Product_Name_8.setStyleSheet("Text-align: left") 
        self.Gmarket_Product_Name_8.setStyleSheet("Font: 9pt Yu Gothic") 
        self.Gmarket_Product_Name_8.clicked.connect(G8_LastOpen)
        self.Gmarket_Product_Name_8.clicked.connect(self.G_LastOpen)
        self.Gmarket_Product_Name_9.setText(str(G_data_name[8].get_text()))
        self.Gmarket_Product_Name_9.setStyleSheet("Text-align: left")  
        self.Gmarket_Product_Name_9.setStyleSheet("Font: 9pt Yu Gothic") 
        self.Gmarket_Product_Name_9.clicked.connect(G9_LastOpen)
        self.Gmarket_Product_Name_9.clicked.connect(self.G_LastOpen)

        #상품가격출력
        self.Gmarket_Product_Price_1.setText(str(G_data_price[0]) + '원')
        self.Gmarket_Product_Price_1.setStyleSheet("Text-align: left")
        self.Gmarket_Product_Price_1.setStyleSheet("Font: 9pt Yu Gothic")
        self.Gmarket_Product_Price_2.setText(str(G_data_price[1]) + '원')
        self.Gmarket_Product_Price_2.setStyleSheet("Text-align: left")
        self.Gmarket_Product_Price_2.setStyleSheet("Font: 9pt Yu Gothic")
        self.Gmarket_Product_Price_3.setText(str(G_data_price[2]) + '원')
        self.Gmarket_Product_Price_3.setStyleSheet("Text-align: left")
        self.Gmarket_Product_Price_3.setStyleSheet("Font: 9pt Yu Gothic")
        self.Gmarket_Product_Price_4.setText(str(G_data_price[3]) + '원')
        self.Gmarket_Product_Price_4.setStyleSheet("Text-align: left")
        self.Gmarket_Product_Price_4.setStyleSheet("Font: 9pt Yu Gothic")
        self.Gmarket_Product_Price_5.setText(str(G_data_price[4]) + '원')
        self.Gmarket_Product_Price_5.setStyleSheet("Text-align: left")
        self.Gmarket_Product_Price_5.setStyleSheet("Font: 9pt Yu Gothic")
        self.Gmarket_Product_Price_6.setText(str(G_data_price[5]) + '원')
        self.Gmarket_Product_Price_6.setStyleSheet("Text-align: left")
        self.Gmarket_Product_Price_6.setStyleSheet("Font: 9pt Yu Gothic")
        self.Gmarket_Product_Price_7.setText(str(G_data_price[6]) + '원')
        self.Gmarket_Product_Price_7.setStyleSheet("Text-align: left")
        self.Gmarket_Product_Price_7.setStyleSheet("Font: 9pt Yu Gothic")
        self.Gmarket_Product_Price_8.setText(str(G_data_price[7]) + '원')
        self.Gmarket_Product_Price_8.setStyleSheet("Text-align: left")
        self.Gmarket_Product_Price_8.setStyleSheet("Font: 9pt Yu Gothic")
        self.Gmarket_Product_Price_9.setText(str(G_data_price[8]) + '원')
        self.Gmarket_Product_Price_9.setStyleSheet("Text-align: left")
        self.Gmarket_Product_Price_9.setStyleSheet("Font: 9pt Yu Gothic")

        #쿠팡
        browser = webdriver.Chrome() 
        url = 'https://www.coupang.com/np/search?component=&q=' + parent.lineEdit.text()
        browser.get(url)

        block = browser.find_element_by_class_name('search-product-list')
        imgs = block.find_elements_by_class_name('search-product-wrap-img')
        data_prices = block.find_elements_by_class_name('price-value')
        C_href = block.find_elements_by_class_name('search-product-link')
        data_name = block.find_elements_by_class_name('name')
        Img_results = []
        C_Href_results = []
        for i in imgs:     
            Img_results.append(i.get_attribute('src')) 

        for i in C_href:  
            C_Href_results.append(i.get_attribute('href')) 

        # 쿠팡 img 출력
        def loadImageFromWeb_01(self):
            urlstring = Img_results[0]
            imageFromWeb = urllib.request.urlopen(urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.Cupang_Product_Image_1.setPixmap(self.qPixmapWebVar)

        loadImageFromWeb_01(self)
    
        def loadImageFromWeb_02(self):
            urlstring = Img_results[1]
            imageFromWeb = urllib.request.urlopen(urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.Cupang_Product_Image_2.setPixmap(self.qPixmapWebVar)

        loadImageFromWeb_02(self)

        def loadImageFromWeb_03(self):
            urlstring = Img_results[2]
            imageFromWeb = urllib.request.urlopen(urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.Cupang_Product_Image_3.setPixmap(self.qPixmapWebVar)

        loadImageFromWeb_03(self)

        def loadImageFromWeb_04(self):
            urlstring = Img_results[3]
            imageFromWeb = urllib.request.urlopen(urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.Cupang_Product_Image_4.setPixmap(self.qPixmapWebVar)

        loadImageFromWeb_04(self)

        def loadImageFromWeb_05(self):
            urlstring = Img_results[4]
            imageFromWeb = urllib.request.urlopen(urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.Cupang_Product_Image_5.setPixmap(self.qPixmapWebVar)

        loadImageFromWeb_05(self)

        def loadImageFromWeb_06(self):
            urlstring = Img_results[5]
            imageFromWeb = urllib.request.urlopen(urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.Cupang_Product_Image_6.setPixmap(self.qPixmapWebVar)

        loadImageFromWeb_06(self)

        def loadImageFromWeb_07(self):
            urlstring = Img_results[6]
            imageFromWeb = urllib.request.urlopen(urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.Cupang_Product_Image_7.setPixmap(self.qPixmapWebVar)

        loadImageFromWeb_07(self)

        def loadImageFromWeb_08(self):
            urlstring = Img_results[7]
            imageFromWeb = urllib.request.urlopen(urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.Cupang_Product_Image_8.setPixmap(self.qPixmapWebVar)

        loadImageFromWeb_08(self)

        def loadImageFromWeb_09(self):
            urlstring = Img_results[8]
            imageFromWeb = urllib.request.urlopen(urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.Cupang_Product_Image_9.setPixmap(self.qPixmapWebVar)

        loadImageFromWeb_09(self)

        # 각 버튼마다 btncount에 다른 값을 부여, btncount값에 따라 상세설명창에서 띄우는 값 다르게 시도할 것
        def C1_LastOpen(self):  
            global C_btncount
            C_btncount = 0
            global C_href
            C_href = C_Href_results[C_btncount]
            
        def C2_LastOpen(self):  
            global C_btncount
            C_btncount = 1
            global C_href
            C_href = C_Href_results[C_btncount]
            
        def C3_LastOpen(self):  
            global C_btncount
            C_btncount = 2
            global C_href
            C_href = C_Href_results[C_btncount]
        
        def C4_LastOpen(self):  
            global C_btncount
            C_btncount = 3
            global C_href
            C_href = C_Href_results[C_btncount]

        def C5_LastOpen(self):  
            global C_btncount
            C_btncount = 4
            global C_href
            C_href = C_Href_results[C_btncount]
        
        def C6_LastOpen(self):  
            global C_btncount
            C_btncount = 5
            global C_href
            C_href = C_Href_results[C_btncount]
        
        def C7_LastOpen(self):  
            global C_btncount
            C_btncount = 6
            global C_href
            C_href = C_Href_results[C_btncount]
        
        def C8_LastOpen(self):  
            global C_btncount
            C_btncount = 7
            global C_href
            C_href = C_Href_results[C_btncount]
        
        def C9_LastOpen(self):  
            global C_btncount
            C_btncount = 8
            global C_href
            C_href = C_Href_results[C_btncount]

        #상품이름출력
        self.Cupang_Product_Name_1.setText(str(data_name[0].text))
        self.Cupang_Product_Name_1.setStyleSheet("Text-align: left")
        self.Cupang_Product_Name_1.clicked.connect(C1_LastOpen)
        self.Cupang_Product_Name_1.clicked.connect(self.C_LastOpen)
        self.Cupang_Product_Name_2.setText(str(data_name[1].text))
        self.Cupang_Product_Name_2.setStyleSheet("Text-align: left")
        self.Cupang_Product_Name_2.clicked.connect(C2_LastOpen)
        self.Cupang_Product_Name_2.clicked.connect(self.C_LastOpen)
        self.Cupang_Product_Name_3.setText(str(data_name[2].text))
        self.Cupang_Product_Name_3.setStyleSheet("Text-align: left")
        self.Cupang_Product_Name_3.clicked.connect(C3_LastOpen)  
        self.Cupang_Product_Name_3.clicked.connect(self.C_LastOpen)
        self.Cupang_Product_Name_4.setText(str(data_name[3].text))
        self.Cupang_Product_Name_4.setStyleSheet("Text-align: left")
        self.Cupang_Product_Name_4.clicked.connect(C4_LastOpen)
        self.Cupang_Product_Name_4.clicked.connect(self.C_LastOpen)
        self.Cupang_Product_Name_5.setText(str(data_name[4].text))
        self.Cupang_Product_Name_5.setStyleSheet("Text-align: left")
        self.Cupang_Product_Name_5.clicked.connect(C5_LastOpen)
        self.Cupang_Product_Name_5.clicked.connect(self.C_LastOpen)
        self.Cupang_Product_Name_6.setText(str(data_name[5].text))
        self.Cupang_Product_Name_6.setStyleSheet("Text-align: left")  
        self.Cupang_Product_Name_6.clicked.connect(C6_LastOpen)
        self.Cupang_Product_Name_6.clicked.connect(self.C_LastOpen)
        self.Cupang_Product_Name_7.setText(str(data_name[6].text))
        self.Cupang_Product_Name_7.setStyleSheet("Text-align: left")
        self.Cupang_Product_Name_7.clicked.connect(C7_LastOpen)
        self.Cupang_Product_Name_7.clicked.connect(self.C_LastOpen)
        self.Cupang_Product_Name_8.setText(str(data_name[7].text))
        self.Cupang_Product_Name_8.setStyleSheet("Text-align: left")
        self.Cupang_Product_Name_8.clicked.connect(C8_LastOpen)
        self.Cupang_Product_Name_8.clicked.connect(self.C_LastOpen)
        self.Cupang_Product_Name_9.setText(str(data_name[8].text))
        self.Cupang_Product_Name_9.setStyleSheet("Text-align: left") 
        self.Cupang_Product_Name_9.clicked.connect(C9_LastOpen)
        self.Cupang_Product_Name_9.clicked.connect(self.C_LastOpen)      

        #상품가격출력
        self.Cupang_Product_Price_1.setText(data_prices[0].text + '원')
        self.Cupang_Product_Price_1.setStyleSheet("Text-align: left")
        self.Cupang_Product_Price_1.setStyleSheet("font-weight: bold")
        self.Cupang_Product_Price_2.setText(data_prices[1].text + '원')
        self.Cupang_Product_Price_2.setStyleSheet("Text-align: left")
        self.Cupang_Product_Price_2.setStyleSheet("font-weight: bold")
        self.Cupang_Product_Price_3.setText(data_prices[2].text + '원')
        self.Cupang_Product_Price_3.setStyleSheet("Text-align: left")
        self.Cupang_Product_Price_3.setStyleSheet("font-weight: bold")
        self.Cupang_Product_Price_4.setText(data_prices[3].text + '원')
        self.Cupang_Product_Price_4.setStyleSheet("Text-align: left")
        self.Cupang_Product_Price_4.setStyleSheet("font-weight: bold")
        self.Cupang_Product_Price_5.setText(data_prices[4].text + '원')
        self.Cupang_Product_Price_5.setStyleSheet("Text-align: left")
        self.Cupang_Product_Price_5.setStyleSheet("font-weight: bold")
        self.Cupang_Product_Price_6.setText(data_prices[5].text + '원')
        self.Cupang_Product_Price_6.setStyleSheet("Text-align: left")
        self.Cupang_Product_Price_6.setStyleSheet("font-weight: bold")
        self.Cupang_Product_Price_7.setText(data_prices[6].text + '원')
        self.Cupang_Product_Price_7.setStyleSheet("Text-align: left")
        self.Cupang_Product_Price_7.setStyleSheet("font-weight: bold")
        self.Cupang_Product_Price_8.setText(data_prices[7].text + '원')
        self.Cupang_Product_Price_8.setStyleSheet("Text-align: left")
        self.Cupang_Product_Price_8.setStyleSheet("font-weight: bold")
        self.Cupang_Product_Price_9.setText(data_prices[8].text + '원')
        self.Cupang_Product_Price_9.setStyleSheet("Text-align: left")
        self.Cupang_Product_Price_9.setStyleSheet("font-weight: bold")

        browser.close()
        
        # 헬로마켓
        H_browser = webdriver.Chrome()
        H_url = 'https://www.hellomarket.com/search?q=' + parent.lineEdit.text()
        H_browser.get(H_url)
        H_browser.execute_script('window.scrollBy(0, 540);')
        time.sleep(1)
        H_browser.execute_script('window.scrollBy(0, 540);')
        time.sleep(1)

        Hello_block = H_browser.find_element_by_css_selector('div.list_area')
        H_prices = Hello_block.find_elements_by_class_name('item_price')
        H_imgs = Hello_block.find_elements_by_class_name('thumbnail_img')
        H_href = Hello_block.find_elements_by_class_name('card.card_list')
        H_Img_results = []
        H_Text_results = []  
        H_Href_results = []

        for i in H_imgs:          
            H_Img_results.append(i.get_attribute('src'))
            H_Text_results.append(i.get_attribute('alt'))

        for i in H_href:  
            H_Href_results.append(i.get_attribute('href')) 

        # 각 버튼마다 btncount에 다른 값을 부여, btncount값에 따라 상세설명창에서 띄우는 값 다르게 시도할 것
        def H1_LastOpen(self):
            global H_btncount
            H_btncount = 0
            global H_href
            H_href = H_Href_results[H_btncount]
            
        def H2_LastOpen(self):
            global H_btncount
            H_btncount = 1
            global H_href
            H_href = H_Href_results[H_btncount]
            
        def H3_LastOpen(self):  
            global H_btncount
            H_btncount = 2
            global H_href
            H_href = H_Href_results[H_btncount]

        def H4_LastOpen(self):  
            global H_btncount
            H_btncount = 3
            global H_href
            H_href = H_Href_results[H_btncount]

        def H5_LastOpen(self):  
            global H_btncount
            H_btncount = 4
            global H_href
            H_href = H_Href_results[H_btncount]

        def H6_LastOpen(self):  
            global H_btncount
            H_btncount = 5
            global H_href
            H_href = H_Href_results[H_btncount]

        def H7_LastOpen(self):  
            global H_btncount
            H_btncount = 6
            global H_href
            H_href = H_Href_results[H_btncount]

        def H8_LastOpen(self):  
            global H_btncount
            H_btncount = 7
            global H_href
            H_href = H_Href_results[H_btncount]

        def H9_LastOpen(self):  
            global H_btncount
            H_btncount = 8
            global H_href
            H_href = H_Href_results[H_btncount]

        # 각 항목별 text, 다음창과 연결되는 버튼
        self.Hello_Product_Name_1.setText(H_Text_results[0])
        self.Hello_Product_Name_1.setStyleSheet("Text-align: left")
        self.Hello_Product_Name_1.clicked.connect(H1_LastOpen)
        self.Hello_Product_Name_1.clicked.connect(self.H_LastOpen)
        self.Hello_Product_Name_2.setText(H_Text_results[1])
        self.Hello_Product_Name_2.setStyleSheet("Text-align: left")
        self.Hello_Product_Name_2.clicked.connect(H2_LastOpen)
        self.Hello_Product_Name_2.clicked.connect(self.H_LastOpen)
        self.Hello_Product_Name_3.setText(H_Text_results[2])
        self.Hello_Product_Name_3.setStyleSheet("Text-align: left")
        self.Hello_Product_Name_3.clicked.connect(H3_LastOpen)
        self.Hello_Product_Name_3.clicked.connect(self.H_LastOpen)
        self.Hello_Product_Name_4.setText(H_Text_results[3])
        self.Hello_Product_Name_4.setStyleSheet("Text-align: left")
        self.Hello_Product_Name_4.clicked.connect(H4_LastOpen)
        self.Hello_Product_Name_4.clicked.connect(self.H_LastOpen)
        self.Hello_Product_Name_5.setText(H_Text_results[4])
        self.Hello_Product_Name_5.setStyleSheet("Text-align: left")
        self.Hello_Product_Name_5.clicked.connect(H5_LastOpen)
        self.Hello_Product_Name_5.clicked.connect(self.H_LastOpen)
        self.Hello_Product_Name_6.setText(H_Text_results[5])
        self.Hello_Product_Name_6.setStyleSheet("Text-align: left")
        self.Hello_Product_Name_6.clicked.connect(H6_LastOpen)
        self.Hello_Product_Name_6.clicked.connect(self.H_LastOpen)
        self.Hello_Product_Name_7.setText(H_Text_results[6])
        self.Hello_Product_Name_7.setStyleSheet("Text-align: left")
        self.Hello_Product_Name_7.clicked.connect(H7_LastOpen)
        self.Hello_Product_Name_7.clicked.connect(self.H_LastOpen)
        self.Hello_Product_Name_8.setText(H_Text_results[7])
        self.Hello_Product_Name_8.setStyleSheet("Text-align: left")
        self.Hello_Product_Name_8.clicked.connect(H8_LastOpen)
        self.Hello_Product_Name_8.clicked.connect(self.H_LastOpen)
        self.Hello_Product_Name_9.setText(H_Text_results[8])
        self.Hello_Product_Name_9.setStyleSheet("Text-align: left")
        self.Hello_Product_Name_9.clicked.connect(H9_LastOpen)
        self.Hello_Product_Name_9.clicked.connect(self.H_LastOpen)
        
        self.Hello_Product_Price_1.setText(H_prices[0].text)
        self.Hello_Product_Price_1.setStyleSheet("Text-align: left")
        self.Hello_Product_Price_1.setStyleSheet("font-weight: bold")
        self.Hello_Product_Price_2.setText(H_prices[1].text)
        self.Hello_Product_Price_2.setStyleSheet("Text-align: left")
        self.Hello_Product_Price_2.setStyleSheet("font-weight: bold")
        self.Hello_Product_Price_3.setText(H_prices[2].text)
        self.Hello_Product_Price_3.setStyleSheet("Text-align: left")
        self.Hello_Product_Price_3.setStyleSheet("font-weight: bold")
        self.Hello_Product_Price_4.setText(H_prices[3].text)
        self.Hello_Product_Price_4.setStyleSheet("Text-align: left")
        self.Hello_Product_Price_4.setStyleSheet("font-weight: bold")
        self.Hello_Product_Price_5.setText(H_prices[4].text)
        self.Hello_Product_Price_5.setStyleSheet("Text-align: left")
        self.Hello_Product_Price_5.setStyleSheet("font-weight: bold")
        self.Hello_Product_Price_6.setText(H_prices[5].text)
        self.Hello_Product_Price_6.setStyleSheet("Text-align: left")
        self.Hello_Product_Price_6.setStyleSheet("font-weight: bold")
        self.Hello_Product_Price_7.setText(H_prices[6].text)
        self.Hello_Product_Price_7.setStyleSheet("Text-align: left")
        self.Hello_Product_Price_7.setStyleSheet("font-weight: bold")
        self.Hello_Product_Price_8.setText(H_prices[7].text)
        self.Hello_Product_Price_8.setStyleSheet("Text-align: left")
        self.Hello_Product_Price_8.setStyleSheet("font-weight: bold")
        self.Hello_Product_Price_9.setText(H_prices[8].text)
        self.Hello_Product_Price_9.setStyleSheet("Text-align: left")
        self.Hello_Product_Price_9.setStyleSheet("font-weight: bold")

        # 헬로마켓 img 출력
        def Hello_loadImageFromWeb_01(self):
            urlstring = H_Img_results[0]
            imageFromWeb = urllib.request.urlopen(urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.Hello_Product_image_1.setPixmap(self.qPixmapWebVar)

        Hello_loadImageFromWeb_01(self)

        def Hello_loadImageFromWeb_02(self):
            urlstring = H_Img_results[1]
            imageFromWeb = urllib.request.urlopen(urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.Hello_Product_image_2.setPixmap(self.qPixmapWebVar)

        Hello_loadImageFromWeb_02(self)

        def Hello_loadImageFromWeb_03(self):
            urlstring = H_Img_results[2]
            imageFromWeb = urllib.request.urlopen(urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.Hello_Product_image_3.setPixmap(self.qPixmapWebVar)

        Hello_loadImageFromWeb_03(self)

        def Hello_loadImageFromWeb_04(self):
            urlstring = H_Img_results[3]
            imageFromWeb = urllib.request.urlopen(urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.Hello_Product_image_4.setPixmap(self.qPixmapWebVar)

        Hello_loadImageFromWeb_04(self)

        def Hello_loadImageFromWeb_05(self):
            urlstring = H_Img_results[4]
            imageFromWeb = urllib.request.urlopen(urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.Hello_Product_image_5.setPixmap(self.qPixmapWebVar)

        Hello_loadImageFromWeb_05(self)

        def Hello_loadImageFromWeb_06(self):
            urlstring = H_Img_results[5]
            imageFromWeb = urllib.request.urlopen(urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.Hello_Product_image_6.setPixmap(self.qPixmapWebVar)

        Hello_loadImageFromWeb_06(self)

        def Hello_loadImageFromWeb_07(self):
            urlstring = H_Img_results[6]
            imageFromWeb = urllib.request.urlopen(urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.Hello_Product_image_7.setPixmap(self.qPixmapWebVar)

        Hello_loadImageFromWeb_07(self)

        def Hello_loadImageFromWeb_08(self):
            urlstring = H_Img_results[7]
            imageFromWeb = urllib.request.urlopen(urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.Hello_Product_image_8.setPixmap(self.qPixmapWebVar)

        Hello_loadImageFromWeb_08(self)

        def Hello_loadImageFromWeb_09(self):
            urlstring = H_Img_results[8]
            imageFromWeb = urllib.request.urlopen(urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.Hello_Product_image_9.setPixmap(self.qPixmapWebVar)

        Hello_loadImageFromWeb_09(self)

        H_browser.close()

        # 당근마켓
        D_browser = webdriver.Chrome()
        D_url = 'https://www.daangn.com/search/' + parent.lineEdit.text()
        D_browser.get(D_url)
        Danggeun_block = D_browser.find_element_by_id('flea-market-wrap')
        D_imgs = Danggeun_block.find_elements_by_css_selector('div.card-photo>img')
        D_href = Danggeun_block.find_elements_by_class_name('flea-market-article-link')
        D_Img_results = []
        D_Href_results = []

        for i in D_imgs:     
            D_Img_results.append(i.get_attribute('src'))

        for i in D_href:  
            D_Href_results.append(i.get_attribute('href'))

        D_browser.close()

        # 각 버튼마다 btncount에 다른 값을 부여, btncount값에 따라 상세설명창에서 띄우는 값 다르게 시도할 것
        def D1_LastOpen(self):  
            global D_btncount
            D_btncount = 0
            global D_href
            D_href = D_Href_results[D_btncount]
            
        def D2_LastOpen(self):  
            global D_btncount
            D_btncount = 1
            global D_href
            D_href = D_Href_results[D_btncount]

        def D3_LastOpen(self):  
            global D_btncount
            D_btncount = 2
            global D_href
            D_href = D_Href_results[D_btncount]

        def D4_LastOpen(self):  
            global D_btncount
            D_btncount = 3
            global D_href
            D_href = D_Href_results[D_btncount]

        def D5_LastOpen(self):  
            global D_btncount
            D_btncount = 4
            global D_href
            D_href = D_Href_results[D_btncount]

        def D6_LastOpen(self):  
            global D_btncount
            D_btncount = 5
            global D_href
            D_href = D_Href_results[D_btncount]

        # 당근마켓 img 출력
        def D_loadImageFromWeb_01(self):
            D_urlstring = D_Img_results[0]
            D_imageFromWeb = urllib.request.urlopen(D_urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(D_imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.Danggeun_Product_Image_1.setPixmap(self.qPixmapWebVar)

        D_loadImageFromWeb_01(self)
    
        def D_loadImageFromWeb_02(self):
            D_urlstring = D_Img_results[1]
            D_imageFromWeb = urllib.request.urlopen(D_urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(D_imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.Danggeun_Product_Image_2.setPixmap(self.qPixmapWebVar)

        D_loadImageFromWeb_02(self)

        def D_loadImageFromWeb_03(self):
            D_urlstring = D_Img_results[2]
            D_imageFromWeb = urllib.request.urlopen(D_urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(D_imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.Danggeun_Product_Image_3.setPixmap(self.qPixmapWebVar)

        D_loadImageFromWeb_03(self)

        def D_loadImageFromWeb_04(self):
            D_urlstring = D_Img_results[3]
            D_imageFromWeb = urllib.request.urlopen(D_urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(D_imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.Danggeun_Product_Image_4.setPixmap(self.qPixmapWebVar)

        D_loadImageFromWeb_04(self)

        def D_loadImageFromWeb_05(self):
            D_urlstring = D_Img_results[4]
            D_imageFromWeb = urllib.request.urlopen(D_urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(D_imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.Danggeun_Product_Image_5.setPixmap(self.qPixmapWebVar)

        D_loadImageFromWeb_05(self)

        def D_loadImageFromWeb_06(self):
            D_urlstring = D_Img_results[5]
            D_imageFromWeb = urllib.request.urlopen(D_urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(D_imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.Danggeun_Product_Image_6.setPixmap(self.qPixmapWebVar)

        D_loadImageFromWeb_06(self)

        page = requests.get('https://www.daangn.com/search/' + parent.lineEdit.text())
        soup = BeautifulSoup(page.content, 'html.parser')

        data_name = soup.find_all('span', class_='article-title') #상품이름
        data_price = soup.find_all('p', class_='article-price')   #상품가격
        

        #상품이름출력
        self.Danggeun_Product_Name_1.setText(str(data_name[0].get_text()))
        self.Danggeun_Product_Name_1.setStyleSheet("Text-align: left")
        self.Danggeun_Product_Name_1.clicked.connect(D1_LastOpen)
        self.Danggeun_Product_Name_1.clicked.connect(self.D_LastOpen)
        self.Danggeun_Product_Name_2.setText(str(data_name[1].get_text()))
        self.Danggeun_Product_Name_2.setStyleSheet("Text-align: left")
        self.Danggeun_Product_Name_2.clicked.connect(D2_LastOpen)
        self.Danggeun_Product_Name_2.clicked.connect(self.D_LastOpen)
        self.Danggeun_Product_Name_3.setText(str(data_name[2].get_text()))
        self.Danggeun_Product_Name_3.setStyleSheet("Text-align: left") 
        self.Danggeun_Product_Name_3.clicked.connect(D3_LastOpen)   
        self.Danggeun_Product_Name_3.clicked.connect(self.D_LastOpen)
        self.Danggeun_Product_Name_4.setText(str(data_name[3].get_text()))
        self.Danggeun_Product_Name_4.clicked.connect(D4_LastOpen)
        self.Danggeun_Product_Name_4.setStyleSheet("Text-align: left")
        self.Danggeun_Product_Name_4.clicked.connect(self.D_LastOpen)
        self.Danggeun_Product_Name_5.setText(str(data_name[4].get_text()))
        self.Danggeun_Product_Name_5.setStyleSheet("Text-align: left")
        self.Danggeun_Product_Name_5.clicked.connect(D5_LastOpen)
        self.Danggeun_Product_Name_5.clicked.connect(self.D_LastOpen)
        self.Danggeun_Product_Name_6.setText(str(data_name[5].get_text()))
        self.Danggeun_Product_Name_6.setStyleSheet("Text-align: left") 
        self.Danggeun_Product_Name_6.clicked.connect(D6_LastOpen)
        self.Danggeun_Product_Name_6.clicked.connect(self.D_LastOpen)
 

        #상품가격출력
        self.Danggeun_Product_Price_1.setText(str(data_price[0]))
        self.Danggeun_Product_Price_1.setStyleSheet("Text-align: left")
        self.Danggeun_Product_Price_1.setStyleSheet("font-weight: bold")
        self.Danggeun_Product_Price_2.setText(str(data_price[1]))
        self.Danggeun_Product_Price_2.setStyleSheet("Text-align: left")
        self.Danggeun_Product_Price_2.setStyleSheet("font-weight: bold")
        self.Danggeun_Product_Price_3.setText(str(data_price[2]))
        self.Danggeun_Product_Price_3.setStyleSheet("Text-align: left")
        self.Danggeun_Product_Price_3.setStyleSheet("font-weight: bold")
        self.Danggeun_Product_Price_4.setText(str(data_price[3]))
        self.Danggeun_Product_Price_4.setStyleSheet("Text-align: left")
        self.Danggeun_Product_Price_4.setStyleSheet("font-weight: bold")
        self.Danggeun_Product_Price_5.setText(str(data_price[4]))
        self.Danggeun_Product_Price_5.setStyleSheet("Text-align: left")
        self.Danggeun_Product_Price_5.setStyleSheet("font-weight: bold")
        self.Danggeun_Product_Price_6.setText(str(data_price[5]))
        self.Danggeun_Product_Price_6.setStyleSheet("Text-align: left")
        self.Danggeun_Product_Price_6.setStyleSheet("font-weight: bold")

    # 세 번째 UI(매물 상세설명창)
    def D_LastOpen(self):
        D_Last_Area(self)
        # self.close()

    def H_LastOpen(self):
        H_Last_Area(self)
        # self.close()  # 두번째 페이지 닫기

    def C_LastOpen(self):
        C_Last_Area(self)

    def G_LastOpen(self):
        G_Last_Area(self)

# 유튜브 리뷰
class Review_Area(QDialog, uiReview):
    def __init__(self, parent):
        super(Review_Area, self).__init__(parent)
        self.setupUi(self)
        self.show()

        self.lblTitle.setText(parent.lineEdit.text() + "에 대한 리뷰결과")
        self.lblTitle.setStyleSheet("Text-align: center")
        
        Y_browser = webdriver.Chrome()
        url = 'https://www.youtube.com/results?search_query=' + parent.lineEdit.text()
        Y_browser.get(url)
        Y_browser.execute_script('window.scrollBy(0, 540);')
        time.sleep(1)
        Y_block = Y_browser.find_element_by_id('contents')
        Y_imgs = Y_block.find_elements_by_id('video-title')
        Y_Hits = Y_browser.find_elements_by_css_selector('span.style-scope.ytd-video-meta-block')
        Y_href = Y_block.find_elements_by_class_name('yt-simple-endpoint.style-scope.ytd-video-renderer')
        Y_Img_results = []
        Y_Href_results = []

        for i in range(0, 6):          
            Y_Title = Y_imgs[i].get_attribute('title')
            Y_Img_results.append(Y_Title)

        for i in Y_href:  
            Y_Href_results.append(i.get_attribute('href'))

        def Y1_LastOpen(self):  
            global Y_btncount
            Y_btncount = 0
            global Y_href
            Y_href = Y_Href_results[Y_btncount]

        def Y2_LastOpen(self):  
            global Y_btncount
            Y_btncount = 2
            global Y_href
            Y_href = Y_Href_results[Y_btncount]

        def Y3_LastOpen(self):  
            global Y_btncount
            Y_btncount = 4
            global Y_href
            Y_href = Y_Href_results[Y_btncount]

        def Y4_LastOpen(self):  
            global Y_btncount
            Y_btncount = 6
            global Y_href
            Y_href = Y_Href_results[Y_btncount]

        self.btn_Title_1.setText(Y_Img_results[0])
        self.btn_Title_1.setStyleSheet("Text-align: left")
        self.btn_Title_1.clicked.connect(Y1_LastOpen)
        self.btn_Title_1.clicked.connect(self.webviewOpen)
        self.btn_Title_2.setText(Y_Img_results[1])
        self.btn_Title_2.setStyleSheet("Text-align: left")
        self.btn_Title_2.clicked.connect(Y2_LastOpen)
        self.btn_Title_2.clicked.connect(self.webviewOpen)
        self.btn_Title_3.setText(Y_Img_results[2])
        self.btn_Title_3.setStyleSheet("Text-align: left")
        self.btn_Title_3.clicked.connect(Y3_LastOpen)
        self.btn_Title_3.clicked.connect(self.webviewOpen)
        self.btn_Title_4.setText(Y_Img_results[3])
        self.btn_Title_4.setStyleSheet("Text-align: left")
        self.btn_Title_4.clicked.connect(Y4_LastOpen)
        self.btn_Title_4.clicked.connect(self.webviewOpen)

        self.lbl_Hits_1.setText(Y_Hits[0].text)
        self.lbl_Hits_1.setStyleSheet("Text-align: left")
        self.lbl_Hits_2.setText(Y_Hits[1].text)
        self.lbl_Hits_2.setStyleSheet("Text-align: left")
        self.lbl_Hits_3.setText(Y_Hits[2].text)
        self.lbl_Hits_3.setStyleSheet("Text-align: left")
        self.lbl_Hits_4.setText(Y_Hits[3].text)
        self.lbl_Hits_4.setStyleSheet("Text-align: left")
        self.lbl_Hits_5.setText(Y_Hits[4].text)
        self.lbl_Hits_5.setStyleSheet("Text-align: left")
        self.lbl_Hits_6.setText(Y_Hits[5].text)
        self.lbl_Hits_6.setStyleSheet("Text-align: left")
        self.lbl_Hits_7.setText(Y_Hits[6].text)
        self.lbl_Hits_7.setStyleSheet("Text-align: left")
        self.lbl_Hits_8.setText(Y_Hits[7].text)
        self.lbl_Hits_8.setStyleSheet("Text-align: left")

        image_list = []
        x = 1
        for i in range(6):
            img_xpath = '/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer['+str(x)+']/div[1]/ytd-thumbnail/a/yt-img-shadow/img' 
            image = Y_browser.find_element_by_xpath(img_xpath)
            img_url = image.get_attribute('src')
            image_list.append(img_url)
            x = x+1

        def Y_loadImageFromWeb_01(self):
            Y_urlstring = image_list[0]
            Y_imageFromWeb = urllib.request.urlopen(Y_urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(Y_imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(181, 101)
            self.img_Thumnail_1.setPixmap(self.qPixmapWebVar)

        Y_loadImageFromWeb_01(self)

        def Y_loadImageFromWeb_02(self):
            Y_urlstring = image_list[1]
            Y_imageFromWeb = urllib.request.urlopen(Y_urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(Y_imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(181, 101)
            self.img_Thumnail_2.setPixmap(self.qPixmapWebVar)

        Y_loadImageFromWeb_02(self)

        def Y_loadImageFromWeb_03(self):
            Y_urlstring = image_list[2]
            Y_imageFromWeb = urllib.request.urlopen(Y_urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(Y_imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(181, 101)
            self.img_Thumnail_3.setPixmap(self.qPixmapWebVar)

        Y_loadImageFromWeb_03(self)

        def Y_loadImageFromWeb_04(self):
            Y_urlstring = image_list[3]
            Y_imageFromWeb = urllib.request.urlopen(Y_urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(Y_imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(181, 101)
            self.img_Thumnail_4.setPixmap(self.qPixmapWebVar)

        Y_loadImageFromWeb_04(self)

        Y_browser.close()

    def webviewOpen(self):
        window(self)

# 쿠팡 세 번째 페이지
class C_Last_Area(QDialog, C_uiLast):
    def __init__(self, parent):
        super(C_Last_Area, self).__init__(parent)
        self.setupUi(self)
        self.show()
        self.btnPurchase.clicked.connect(self.btn_buy)

        global C_href
        T_C_browser = webdriver.Chrome()
        T_C_browser.get(C_href)
        time.sleep(5)
        while(1):
            try:
                T_C_title = T_C_browser.find_element_by_class_name('prod-buy-header__title')
                T_C_price = T_C_browser.find_element_by_class_name('total-price')  
                T_C_img = T_C_browser.find_element_by_class_name('prod-image__detail')
                # T_C_Img_result = T_C_img.get_attribute('src')
                T_C_block = T_C_browser.find_element_by_class_name('prod-description-attribute')
                T_C_delivery = T_C_browser.find_element_by_class_name('prod-txt-onyx.prod-txt-font-14')
                T_C_Img = T_C_browser.find_elements_by_css_selector('div.prod-image__item')
                T_C_Img_Btns = T_C_browser.find_element_by_class_name('prod-image__items').find_elements_by_tag_name('div')

                break
            except Exception:
                wait = WebDriverWait(T_C_browser, 5).until(EC.expected_conditions.alert_is_present)
                T_C_browser.switch_to.alert.accept()
                time.sleep(3)
                continue

        T_C_Img_results = []
        for i in range(len(T_C_Img)):
            T_C_Img_Btns[i].click()
            time.sleep(1)
            T_C_Img_results.append(T_C_img.get_attribute('src'))

        def loadImageFromWeb_01(self):
            if(len(T_C_Img_results) > 0):
                urlstring = T_C_Img_results[0]
                imageFromWeb = urllib.request.urlopen(urlstring).read()
                self.qPixmapWebVar = QPixmap()
                self.qPixmapWebVar.loadFromData(imageFromWeb)
                self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(400, 130)
                self.Product_img.setPixmap(self.qPixmapWebVar)

        loadImageFromWeb_01(self)

        def loadImageFromWeb_02(self):
            if(len(T_C_Img_results) > 1):
                urlstring = T_C_Img_results[1]
                imageFromWeb = urllib.request.urlopen(urlstring).read()
                self.qPixmapWebVar = QPixmap()
                self.qPixmapWebVar.loadFromData(imageFromWeb)
                self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(400, 130)
                self.label_2.setPixmap(self.qPixmapWebVar)

        loadImageFromWeb_02(self)

        def loadImageFromWeb_03(self):
            if(len(T_C_Img_results) > 2):
                urlstring = T_C_Img_results[2]
                imageFromWeb = urllib.request.urlopen(urlstring).read()
                self.qPixmapWebVar = QPixmap()
                self.qPixmapWebVar.loadFromData(imageFromWeb)
                self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(400, 130)
                self.label_3.setPixmap(self.qPixmapWebVar)

        loadImageFromWeb_03(self)

        def loadImageFromWeb_04(self):
            if(len(T_C_Img_results) > 3):
                urlstring = T_C_Img_results[3]
                imageFromWeb = urllib.request.urlopen(urlstring).read()
                self.qPixmapWebVar = QPixmap()
                self.qPixmapWebVar.loadFromData(imageFromWeb)
                self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(400, 130)
                self.label_4.setPixmap(self.qPixmapWebVar)

        loadImageFromWeb_04(self)

        def loadImageFromWeb_05(self):
            if(len(T_C_Img_results) > 4):
                urlstring = T_C_Img_results[4]
                imageFromWeb = urllib.request.urlopen(urlstring).read()
                self.qPixmapWebVar = QPixmap()
                self.qPixmapWebVar.loadFromData(imageFromWeb)
                self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(400, 130)
                self.label_5.setPixmap(self.qPixmapWebVar)

        loadImageFromWeb_05(self)

        def loadImageFromWeb_06(self):
            if(len(T_C_Img_results) > 5):
                urlstring = T_C_Img_results[5]
                imageFromWeb = urllib.request.urlopen(urlstring).read()
                self.qPixmapWebVar = QPixmap()
                self.qPixmapWebVar.loadFromData(imageFromWeb)
                self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(400, 130)
                self.label_6.setPixmap(self.qPixmapWebVar)

        loadImageFromWeb_06(self)

        self.Title_Text.setText(T_C_title.text)       # 상품명
        self.Price_Text.setText(T_C_price.text)       # 가격
        self.Explain_Text.setText(T_C_block.text)
        self.Delivery_Text.setText(T_C_delivery.text + " 도착예정")

        T_C_browser.close()

    def btn_buy(self):
        C_browser = webdriver.Chrome()
        C_url = C_href
        C_browser.get(C_url)

# g마켓 세 번째 페이지      
class G_Last_Area(QDialog, G_uiLast):
    def __init__(self, parent):
        super(G_Last_Area, self).__init__(parent)
        self.setupUi(self)
        self.show()
        self.btnPurchase.clicked.connect(self.btn_buy)

        T_G_browser = webdriver.Chrome()
        T_G_browser.get(G_href)
        time.sleep(6)

        T_G_Price = T_G_browser.find_element_by_class_name('price_real')
        T_G_title = T_G_browser.find_element_by_class_name('itemtit')
        T_G_block = T_G_browser.find_element_by_class_name('viewer')  # thumb-gallery uxecarousel alone
        T_G_delivery = T_G_browser.find_element_by_class_name('txt_emp')
        T_G_img = T_G_block.find_elements_by_tag_name('li')
        T_G_Img_results = []
        for i in T_G_img:
            T_G_Img_results.append(i.find_element_by_tag_name('img').get_attribute('src'))
 
        # 상품 이미지 띄우기
        def loadImageFromWeb_01(self):
            if(len(T_G_Img_results) > 0):
                urlstring = T_G_Img_results[0]
                imageFromWeb = urllib.request.urlopen(urlstring).read()
                self.qPixmapWebVar = QPixmap()
                self.qPixmapWebVar.loadFromData(imageFromWeb)
                self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(400, 130)
                self.Product_img.setPixmap(self.qPixmapWebVar)

        loadImageFromWeb_01(self)

        def loadImageFromWeb_02(self):
            if(len(T_G_Img_results) > 1):
                urlstring = T_G_Img_results[1]
                imageFromWeb = urllib.request.urlopen(urlstring).read()
                self.qPixmapWebVar = QPixmap()
                self.qPixmapWebVar.loadFromData(imageFromWeb)
                self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(400, 130)
                self.label_2.setPixmap(self.qPixmapWebVar)

        loadImageFromWeb_02(self)

        def loadImageFromWeb_03(self):
            if(len(T_G_Img_results) > 2):
                urlstring = T_G_Img_results[2]
                imageFromWeb = urllib.request.urlopen(urlstring).read()
                self.qPixmapWebVar = QPixmap()
                self.qPixmapWebVar.loadFromData(imageFromWeb)
                self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(400, 130)
                self.label_3.setPixmap(self.qPixmapWebVar)

        loadImageFromWeb_03(self)

        def loadImageFromWeb_04(self):
            if(len(T_G_Img_results) > 3):
                urlstring = T_G_Img_results[3]
                imageFromWeb = urllib.request.urlopen(urlstring).read()
                self.qPixmapWebVar = QPixmap()
                self.qPixmapWebVar.loadFromData(imageFromWeb)
                self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(400, 130)
                self.label_4.setPixmap(self.qPixmapWebVar)

        loadImageFromWeb_04(self)

        def loadImageFromWeb_05(self):
            if(len(T_G_Img_results) > 4):
                urlstring = T_G_Img_results[4]
                imageFromWeb = urllib.request.urlopen(urlstring).read()
                self.qPixmapWebVar = QPixmap()
                self.qPixmapWebVar.loadFromData(imageFromWeb)
                self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(400, 130)
                self.label_5.setPixmap(self.qPixmapWebVar)

        loadImageFromWeb_05(self)

        def loadImageFromWeb_06(self):
            if(len(T_G_Img_results) > 5):
                urlstring = T_G_Img_results[5]
                imageFromWeb = urllib.request.urlopen(urlstring).read()
                self.qPixmapWebVar = QPixmap()
                self.qPixmapWebVar.loadFromData(imageFromWeb)
                self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(400, 130)
                self.label_6.setPixmap(self.qPixmapWebVar)

        loadImageFromWeb_06(self)
        
        self.Title_Text.setText(T_G_title.text)       # 상품명
        self.Price_Text.setText(T_G_Price.text)       # 가격
        self.Delivery_Text.setText(T_G_delivery.text) # 배송


        #관련 인기상품 이미지 텍스트 띄우는코드
        T_G_block1 = T_G_browser.find_element_by_class_name('vip-togetheritems.uxecarousel')
        
        T_G_img1 = T_G_block1.find_elements_by_tag_name('li')
        T_G_img2 = T_G_block1.find_elements_by_tag_name('a')
        T_G_Prices = []
        T_G_Img_results1 = []
        T_G_title1 = []
        T_G_href = []
        
        for i in range(len(T_G_img1)):
            T_G_Img_results1.append(T_G_img1[i].find_element_by_tag_name('img').get_attribute('src'))
            T_G_title1.append(T_G_img1[i].find_element_by_tag_name('p').text)
            T_G_Prices.append(T_G_img1[i].find_element_by_tag_name('strong'))
            T_G_href.append(T_G_img2[i].get_attribute('href'))

        def btn_Gbuy1(self):
            G_browser = webdriver.Chrome()
            G_url = T_G_href[1]
            G_browser.get(G_url)

        def btn_Gbuy2(self):
            G_browser = webdriver.Chrome()
            G_url = T_G_href[2]
            G_browser.get(G_url)

        def btn_Gbuy3(self):
            G_browser = webdriver.Chrome()
            G_url = T_G_href[3]
            G_browser.get(G_url)

        def btn_Gbuy4(self):
            G_browser = webdriver.Chrome()
            G_url = T_G_href[4]
            G_browser.get(G_url)

        def btn_Gbuy5(self):
            G_browser = webdriver.Chrome()
            G_url = T_G_href[5]
            G_browser.get(G_url)

        self.T_Gmarket_Product_Name_1.setText(T_G_title1[0])
        self.T_Gmarket_Product_Name_1.setStyleSheet("Text-align: left")
        self.T_Gmarket_Product_Name_1.clicked.connect(btn_Gbuy1)
        self.T_Gmarket_Product_Name_2.setText(T_G_title1[1])
        self.T_Gmarket_Product_Name_2.setStyleSheet("Text-align: left")
        self.T_Gmarket_Product_Name_2.clicked.connect(btn_Gbuy2)
        self.T_Gmarket_Product_Name_3.setText(T_G_title1[2])
        self.T_Gmarket_Product_Name_3.setStyleSheet("Text-align: left")
        self.T_Gmarket_Product_Name_3.clicked.connect(btn_Gbuy3)
        self.T_Gmarket_Product_Name_4.setText(T_G_title1[3])
        self.T_Gmarket_Product_Name_4.setStyleSheet("Text-align: left")
        self.T_Gmarket_Product_Name_4.clicked.connect(btn_Gbuy4)
        self.T_Gmarket_Product_Name_5.setText(T_G_title1[4])
        self.T_Gmarket_Product_Name_5.setStyleSheet("Text-align: left")
        self.T_Gmarket_Product_Name_5.clicked.connect(btn_Gbuy5)

        self.T_Gmarket_Product_Price_1.setText(T_G_Prices[0].text)
        self.T_Gmarket_Product_Price_1.setStyleSheet("Text-align: left")
        self.T_Gmarket_Product_Price_2.setText(T_G_Prices[1].text)
        self.T_Gmarket_Product_Price_2.setStyleSheet("Text-align: left")
        self.T_Gmarket_Product_Price_3.setText(T_G_Prices[2].text)
        self.T_Gmarket_Product_Price_3.setStyleSheet("Text-align: left")
        self.T_Gmarket_Product_Price_4.setText(T_G_Prices[3].text)
        self.T_Gmarket_Product_Price_4.setStyleSheet("Text-align: left")
        self.T_Gmarket_Product_Price_5.setText(T_G_Prices[4].text)
        self.T_Gmarket_Product_Price_5.setStyleSheet("Text-align: left")

        # 관련 이미지 띄우기
        def T_G_loadImageFromWeb_01(self):
            T_G_urlstring = T_G_Img_results1[0]
            T_G_imageFromWeb = urllib.request.urlopen(T_G_urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(T_G_imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.T_Gmarket_Product_Image_1.setPixmap(self.qPixmapWebVar)

        T_G_loadImageFromWeb_01(self)
    
        def T_G_loadImageFromWeb_02(self):
            T_G_urlstring = T_G_Img_results1[1]
            T_G_imageFromWeb = urllib.request.urlopen(T_G_urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(T_G_imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.T_Gmarket_Product_Image_2.setPixmap(self.qPixmapWebVar)

        T_G_loadImageFromWeb_02(self)

        def T_G_loadImageFromWeb_03(self):
            T_G_urlstring = T_G_Img_results1[2]
            T_G_imageFromWeb = urllib.request.urlopen(T_G_urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(T_G_imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.T_Gmarket_Product_Image_3.setPixmap(self.qPixmapWebVar)

        T_G_loadImageFromWeb_03(self)

        def T_G_loadImageFromWeb_04(self):
            T_G_urlstring = T_G_Img_results1[3]
            T_G_imageFromWeb = urllib.request.urlopen(T_G_urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(T_G_imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.T_Gmarket_Product_Image_4.setPixmap(self.qPixmapWebVar)

        T_G_loadImageFromWeb_04(self)

        def T_G_loadImageFromWeb_05(self):
            T_G_urlstring = T_G_Img_results1[4]
            T_G_imageFromWeb = urllib.request.urlopen(T_G_urlstring).read()
            self.qPixmapWebVar = QPixmap()
            self.qPixmapWebVar.loadFromData(T_G_imageFromWeb)
            self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(183, 72)
            self.T_Gmarket_Product_Image_5.setPixmap(self.qPixmapWebVar)

        T_G_loadImageFromWeb_05(self)
    
        T_G_browser.close()

    def btn_buy(self):
        G_browser = webdriver.Chrome()
        G_url = G_href
        G_browser.get(G_url)

# 헬로마켓 세 번째 페이지
class H_Last_Area(QDialog, H_uiLast):
    def __init__(self, parent):
        super(H_Last_Area, self).__init__(parent)
        self.setupUi(self)
        self.show()
        self.btnPurchase.clicked.connect(self.btn_buy)
        global H_href
        T_H_browser = webdriver.Chrome()
        T_H_browser.get(H_href)
        time.sleep(2)

        T_Hello_block = T_H_browser.find_element_by_css_selector('div.detail_box')
        T_H_tilte = T_Hello_block.find_element_by_class_name('item_title')
        T_H_explain = T_Hello_block.find_element_by_class_name('description_text')
        T_H_Price = T_Hello_block.find_element_by_class_name('item_price.item_price_bottom')
        T_H_Imgs_Tag = T_Hello_block.find_elements_by_class_name('centered')
        T_H_Imgs_Btn_Next = T_Hello_block.find_element_by_class_name('swiper-button-next.auto_swiper_next')
        T_H_Img_results = []
        
        for i in T_H_Imgs_Tag:
            if(T_H_Imgs_Btn_Next.get_attribute('aria-disabled') == 'false'):
                T_H_Imgs_Btn_Next.click()
                time.sleep(1)
            T_H_Img_results.append(i.find_element_by_tag_name('img').get_attribute('src'))

        # 상품 이미지 띄우기
        def loadImageFromWeb_01(self):
            if(len(T_H_Img_results) > 0):
                urlstring = T_H_Img_results[0]
                imageFromWeb = urllib.request.urlopen(urlstring).read()
                self.qPixmapWebVar = QPixmap()
                self.qPixmapWebVar.loadFromData(imageFromWeb)
                self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(400, 130)
                self.Product_img.setPixmap(self.qPixmapWebVar)

        loadImageFromWeb_01(self)

        def loadImageFromWeb_02(self):
            if(len(T_H_Img_results) > 1):
                urlstring = T_H_Img_results[1]
                imageFromWeb = urllib.request.urlopen(urlstring).read()
                self.qPixmapWebVar = QPixmap()
                self.qPixmapWebVar.loadFromData(imageFromWeb)
                self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(400, 130)
                self.label_2.setPixmap(self.qPixmapWebVar)

        loadImageFromWeb_02(self)

        def loadImageFromWeb_03(self):
            if(len(T_H_Img_results) > 2):
                urlstring = T_H_Img_results[2]
                imageFromWeb = urllib.request.urlopen(urlstring).read()
                self.qPixmapWebVar = QPixmap()
                self.qPixmapWebVar.loadFromData(imageFromWeb)
                self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(400, 130)
                self.label_3.setPixmap(self.qPixmapWebVar)

        loadImageFromWeb_03(self)

        def loadImageFromWeb_04(self):
            if(len(T_H_Img_results) > 3):
                urlstring = T_H_Img_results[3]
                imageFromWeb = urllib.request.urlopen(urlstring).read()
                self.qPixmapWebVar = QPixmap()
                self.qPixmapWebVar.loadFromData(imageFromWeb)
                self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(400, 130)
                self.label_4.setPixmap(self.qPixmapWebVar)

        loadImageFromWeb_04(self)

        def loadImageFromWeb_05(self):
            if(len(T_H_Img_results) > 4):
                urlstring = T_H_Img_results[4]
                imageFromWeb = urllib.request.urlopen(urlstring).read()
                self.qPixmapWebVar = QPixmap()
                self.qPixmapWebVar.loadFromData(imageFromWeb)
                self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(400, 130)
                self.label_5.setPixmap(self.qPixmapWebVar)

        loadImageFromWeb_05(self)

        def loadImageFromWeb_06(self):
            if(len(T_H_Img_results) > 5):
                urlstring = T_H_Img_results[5]
                imageFromWeb = urllib.request.urlopen(urlstring).read()
                self.qPixmapWebVar = QPixmap()
                self.qPixmapWebVar.loadFromData(imageFromWeb)
                self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(400, 130)
                self.label_6.setPixmap(self.qPixmapWebVar)

        loadImageFromWeb_06(self)

        self.Title_Text.setText(T_H_tilte.text)             # 상품명
        self.Explain_Text.setText(T_H_explain.text)         # 설명창
        self.Price_Text.setText(T_H_Price.text + '원')      # 가격

        T_H_browser.close()

    # 구매하러가기 함수
    def btn_buy(self):
        C_browser = webdriver.Chrome()
        C_url = H_href
        C_browser.get(C_url)

# 당근마켓 세 번째 페이지
class D_Last_Area(QDialog, D_uiLast):
    def __init__(self, parent):
        super(D_Last_Area, self).__init__(parent)
        self.setupUi(self)
        self.show()
        self.btnPurchase.clicked.connect(self.btn_buy)

        global D_href
        T_D_browser = webdriver.Chrome()
        T_D_browser.get(D_href)
        time.sleep(4)
        
        T_D_explain = T_D_browser.find_element_by_id('article-detail')
        T_D_Price = T_D_browser.find_element_by_id('article-price')
        T_D_title = T_D_browser.find_element_by_id('article-title')
        T_D_block = T_D_browser.find_element_by_class_name('slider-wrap')
        T_D_Img_Nextbutton = T_D_browser.find_element_by_class_name('slick-next.slick-arrow')
        Count_Imgs = T_D_block.find_element_by_class_name('slick-dots').find_elements_by_tag_name('li')
        T_D_Img_results = []
        
        for i in range(len(Count_Imgs)):
            T_D_Img = T_D_block.find_element_by_class_name('slick-slide.slick-current.slick-active')  # 각 img태그를 담고 있는 상위 태그
            T_D_Img_result = T_D_Img.find_element_by_tag_name('img').get_attribute('src') 
            while(T_D_Img_result == 'https://dnvefa72aowie.cloudfront.net/hoian/category/thumbnails/v2/img_thumb_mens_fashion.png'): # img의 src값이 빈 img값이 아닐 때
                time.sleep(1)
                T_D_Img_result = T_D_Img.find_element_by_tag_name('img').get_attribute('src')
            T_D_Img_results.append(T_D_Img_result)  # 검색 결과에 추가
            T_D_Img_Nextbutton.click()
            time.sleep(1)

        # 상품 이미지 띄우기
        def loadImageFromWeb_01(self):
            if(len(T_D_Img_results) > 0):
                urlstring = T_D_Img_results[0]
                imageFromWeb = urllib.request.urlopen(urlstring).read()
                self.qPixmapWebVar = QPixmap()
                self.qPixmapWebVar.loadFromData(imageFromWeb)
                self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(400, 130)
                self.Product_img.setPixmap(self.qPixmapWebVar)

        loadImageFromWeb_01(self)

        def loadImageFromWeb_02(self):
            if(len(T_D_Img_results) > 1):
                urlstring = T_D_Img_results[1]
                imageFromWeb = urllib.request.urlopen(urlstring).read()
                self.qPixmapWebVar = QPixmap()
                self.qPixmapWebVar.loadFromData(imageFromWeb)
                self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(400, 130)
                self.label_2.setPixmap(self.qPixmapWebVar)

        loadImageFromWeb_02(self)

        def loadImageFromWeb_03(self):
            if(len(T_D_Img_results) > 2):
                urlstring = T_D_Img_results[2]
                imageFromWeb = urllib.request.urlopen(urlstring).read()
                self.qPixmapWebVar = QPixmap()
                self.qPixmapWebVar.loadFromData(imageFromWeb)
                self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(400, 130)
                self.label_3.setPixmap(self.qPixmapWebVar)

        loadImageFromWeb_03(self)
        
        def loadImageFromWeb_04(self):
            if(len(T_D_Img_results) > 3):
                urlstring = T_D_Img_results[3]
                imageFromWeb = urllib.request.urlopen(urlstring).read()
                self.qPixmapWebVar = QPixmap()
                self.qPixmapWebVar.loadFromData(imageFromWeb)
                self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(400, 130)
                self.label_4.setPixmap(self.qPixmapWebVar)

        loadImageFromWeb_04(self)

        def loadImageFromWeb_05(self):
            if(len(T_D_Img_results) > 4):
                urlstring = T_D_Img_results[4]
                imageFromWeb = urllib.request.urlopen(urlstring).read()
                self.qPixmapWebVar = QPixmap()
                self.qPixmapWebVar.loadFromData(imageFromWeb)
                self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(400, 130)
                self.label_5.setPixmap(self.qPixmapWebVar)

        loadImageFromWeb_05(self)

        def loadImageFromWeb_06(self):
            if(len(T_D_Img_results) > 5):
                urlstring = T_D_Img_results[5]
                imageFromWeb = urllib.request.urlopen(urlstring).read()
                self.qPixmapWebVar = QPixmap()
                self.qPixmapWebVar.loadFromData(imageFromWeb)
                self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(400, 130)
                self.label_6.setPixmap(self.qPixmapWebVar)

        loadImageFromWeb_06(self)

        self.Title_Text.setText(T_D_title.text)       # 상품명
        self.Explain_Text.setText(T_D_explain.text)   # 설명창
        self.Price_Text.setText(T_D_Price.text)       # 가격

        T_D_browser.close()
        
    def btn_buy(self):
        D_browser = webdriver.Chrome()
        D_url = D_href
        D_browser.get(D_url)

class window(QDialog, Y_uiLast):
    def __init__(self, parent):
        QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.PluginsEnabled,True)
        super(window, self).__init__(parent)
        self.setupUi(self)
        global Y_href
        T_Y_browser = webdriver.Chrome()
        T_Y_browser.get(Y_href)
        time.sleep(4)
        self.centralwid=QtWidgets.QWidget(self)        
        self.vlayout=QtWidgets.QVBoxLayout()
        self.webview=QtWebEngineWidgets.QWebEngineView()
        self.webview.setUrl(QUrl("https://www.youtube.com/embed/" + Y_href.split('=')[1].split('&')[0]))
        self.vlayout.addWidget(self.webview)
        self.centralwid.setLayout(self.vlayout)
        self.show()

        T_Y_titleblock = T_Y_browser.find_element_by_css_selector('h1.title.style-scope.ytd-video-primary-info-renderer')
        T_Y_text = T_Y_titleblock.find_element_by_css_selector('yt-formatted-string.style-scope.ytd-video-primary-info-renderer')

        T_Y_block = T_Y_browser.find_element_by_css_selector('div.style-scope.ytd-video-primary-info-renderer')
        T_Y_Hits = T_Y_block.find_element_by_class_name('view-count.style-scope.ytd-video-view-count-renderer')

        self.lbl_title.setText(T_Y_text.text)
        self.lbl_title.setStyleSheet("Text-align: left")  # 제목
        self.lbl_hits.setText(T_Y_Hits.text)
        self.lbl_hits.setStyleSheet("Text-align: left")  # 조회수

        T_Y_browser.close()

app = QApplication(sys.argv)
myWindow = MyWindow()
myWindow.show()
app.exec_()