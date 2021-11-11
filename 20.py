from selenium import webdriver
#from selenium import webdriver.
#from time import sleep
my_driver = webdriver.Chrome(executable_path="C:/Chromedriver.exe")
#my_driver.get("https://github.com")
#for i in range (5):
#    sleep(5)
#    my_driver.refresh()
#my_driver.close()

my_driver.get("file:///C:/tip_calc/index.html")
my_driver.find_element_by_id("billamt").send_keys("100")
my_driver.find_element_by_xpath('//*[@id="serviceQual"]/option[3]').click()
my_driver.find_element_by_id("peopleamt").send_keys("4")
my_driver.find_element_by_id("calculate").click()
pyexpat = "5.00"
actual = my_driver.find_element_by_id("tip").text
if pyexpat == actual:
    print("good job!")


