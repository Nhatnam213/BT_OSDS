from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khoi tao WebDriver
driver = webdriver.Chrome()

for i in range(65,91):
    url = "https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22"+chr(i)+"%22"
    try:
        driver.get(url)

        # doi khoang chung 2s
        time.sleep(3)
        #lay ra tat ca the ul
        ul_tags = driver.find_elements(By.TAG_NAME, "ul" )
        print(len(ul_tags))



        #chon the ul thu21
        ul_painters = ul_tags[20] #List start with index=0

        # Lay ra tat ca the<li> thuoc ul_painters
        li_tags = ul_painters.find_elements(By.TAG_NAME, "li")

        #tao ra danh sach url
        links = [tag.find_element(By.TAG_NAME, "a").get_attribute("href")for tag in li_tags]
        #tao ra danh sach title
        titles = [tag.find_element(By.TAG_NAME, "a").get_attribute("title")for tag in li_tags]
        #in ra
        for link in links:
            print(link)
        for title in titles:
            print(title)
    except:
        print("error")

#dong
driver.quit()
