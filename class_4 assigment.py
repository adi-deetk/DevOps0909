from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#1.1
driver = webdriver.Chrome(executable_path="C:///temp/chromedriver.exe")
driver.get("http://www.walla.co.il")
#1.2
driver = webdriver.Chrome(executable_path="C:///temp/chromedriver.exe")
driver.get("http://www.ynet.co.il")

#2.
title = driver.title
driver.refresh()
#print(title)
if title==driver.title:
   print("equal")

#3.
#yes its the same
#explorer-/html/body/div[8]/div/div/div[1]/div[2]/div/span/div/span/span/div/div[1]/div[2]/a/img
#Chrome - /html/body/div[8]/div/div/div[1]/div[2]/div/span/div/span/span/div/div[1]/div[2]/a/img

#4.
driver = webdriver.Chrome(executable_path="C:///temp/chromedriver.exe")
driver.get("https://translate.google.com/")
driver.find_element_by_id("source").send_keys("עדי היה שם עכשיו הוא פה")
driver.find_element_by_id("gt-submit").click()
# לא מצאתי איפה לעשות קליק? .submit?

#5.
driver = webdriver.Chrome(executable_path="C:///temp/chromedriver.exe")
driver.get("https://www.youtube.com//")
driver.find_element_by_id("search").send_keys("Oxia - Domino")
driver.find_element_by_id("gt-submit").click()

#6.

driver.find_element_by_id("search")
driver.find_element_by_xpath(//*[@id="search"])
driver.find_element_by_class_name("gsfi ytd-searchbox")

#7.
driver.get("https://www.facebook.com/")
driver.find_element_by_id("email").send_keys("deetk555@gmail.com")
driver.find_element_by_id("pass").send_keys("********")

#8.
driver = webdriver.Chrome(executable_path="C:///temp/chromedriver.exe")
driver.get()
driver.delete_all_cookies()

#9.
driver.get("https://github.com/")
driver.find_element_by_class_name("form-control input-sm header-search-input jump-to-field js-jump-to-field js-site-search-focus").send_keys(selenium)
driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]").submit()

#10.
driver = webdriver.Chrome(executable_path="C:///temp/chromedriver.exe")
driver.get()
--disable-extensions