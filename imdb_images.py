from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import wget


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("https://www.imdb.com/list/ls063067463/")

images = driver.find_elements_by_tag_name("img")

for image in images:
    
#    print(image.get_attribute("src"))
    try:
        wget.download(image.get_attribute("src"),'/home/fsociety/Documents/selenium/images/'+image.get_attribute("alt")+'.jpg')
    except:
        pass
        

