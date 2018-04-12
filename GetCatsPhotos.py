from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

user_mail = "ybkh811@gmail.com"
#user_pwd = input("Please enter your password :")

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/explore/tags/cat/')

#https://toyo0103.blogspot.tw/2018/01/selenium-webdriver-instagram.html
cats = driver.find_elements_by_class_name("_si7dy")

for cat in cats:
    cat.click()
    driver.implicitly_wait(2)

    try:
        likes = driver.find_element_by_class_name("_nzn1h")
        print(likes.text)
    except:
        pass
    driver.find_element_by_class_name("_dcj9f").click()

driver.quit()