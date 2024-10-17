import re

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import requests


# Tao dataframe rong
d = pd.DataFrame({'name':[],'birth':[],'death':[], 'nationality':[]})
#khoi tao webdriver
driver = webdriver.Chrome();
driver.get("https://en.wikipedia.org/wiki/Edvard_Munch")
time.sleep(5)
# lay ten hoa si
try:
    name =driver.find_element(By.TAG_NAME, "h1").text
except:
    name = ""
# Lay ngay sinh
try:
    birth_element = driver.find_element(By.XPATH, "//th[text()='Born']/following-sibling::td")
    birth = birth_element.text
    birth = re.findall(r'[0-9]{1,2}+\s+[A-Za-z]+\s+[0-9]{4}', birth)[0]
except:
    birth = ""

# Lay ngay mat
try:
    death_element = driver.find_element(By.XPATH, "//th[text()='Died']/following-sibling::td")
    death = death_element.text
    death = re.findall(r'[0-9]{1,2}+\s+[A-Za-z]+\s+[0-9]{4}', death)[0]
except:
    death = ""


# Lay ngay mat
try:
    nationality_element = driver.find_element(By.XPATH, "//th[text()='Nationality']/following-sibling::td")
    nationality = nationality_element.text
except:
    nationality = ""
# Tao dictionary thong tin cua hoa si
painter = {'name' : name, 'birth': birth, 'death': death, 'nationality':nationality}

# CHuyen doi dictionary thanh DataFrame
painter_df = pd.DataFrame([painter])

# Them thong tin vao DF chinh
d = pd.concat([d, painter_df], ignore_index=True)

# In ra DF
print(d)

# Dong web driver
driver.quit()
