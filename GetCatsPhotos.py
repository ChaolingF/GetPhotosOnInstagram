from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

user_mail = "ybkh811@gmail.com"
#user_pwd = input("Please enter your password :")

driver = webdriver.Chrome('C:/Users/ybkh/Desktop/chromedriver.exe')
driver.get('https://www.instagram.com/explore/tags/cat/')

#https://toyo0103.blogspot.tw/2018/01/selenium-webdriver-instagram.html

hot_cats = driver.find_element_by_class_name("_21z45")
cats = hot_cats.find_elements_by_class_name("_si7dy")

for cat in cats:
    cat.click()
    driver.implicitly_wait(1)

    try:
        #class_name = "_nzn1h" : Like column
        likes = driver.find_element_by_class_name("_nzn1h")
        print(likes.text)
        if (likes.text!= None):
            img_url_container = driver.find_element_by_class_name("_sxolz ")
            #img_url_container = driver.find_element_by_class_name("_e3il2 _pmuf1")
            img_url = img_url_container.find_element_by_tag_name("img")
            print( "img:"+ img_url.get_attribute("src"))
    except:
        pass

    driver.find_element_by_class_name("_dcj9f").click()

#driver.quit()
