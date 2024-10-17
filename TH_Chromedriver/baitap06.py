from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import re

######################################################
# I. Tạo nơi chứa links và Tạo dataframe rỗng
all_links = []
d = pd.DataFrame({'name': [], 'birth': [], 'death': [], 'nationality': []})
######################################################
# II. Lấy ra tất cả đường dẫn để truy cập đến painters
# Khởi tạo Webdriver
for i in range(65, 89):
    driver = webdriver.Chrome()
    url = "https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22" + chr(i) + "%22"
    try:
        # Mở trang
        driver.get(url)

        # Đợi một chút để trang tải
        time.sleep(3)

        # Lấy ra tất cả các thẻ ul
        ul_tags = driver.find_elements(By.TAG_NAME, "ul")
        print(len(ul_tags))

        # Chọn thẻ ul thứ 21
        ul_painters = ul_tags[20]  # list start with index=0

        # Lấy ra tất cả thẻ <li> thuộc ul_painters
        li_tags = ul_painters.find_elements(By.TAG_NAME, "li")

        # Tạo danh sách các url
        links = [tag.find_element(By.TAG_NAME, "a").get_attribute("href") for tag in li_tags]
        for x in links:
            all_links.append(x)
    except Exception as e:
        print(f"Error: {e}")

    # Đóng web driver
    driver.quit()

######################################################
# III. Lấy thông tin của từng hoạ sĩ
count = 0
for link in all_links:
    if count > 3:
        break
    count += 1

    print(link)
    try:
        # Khởi tạo webdriver
        driver = webdriver.Chrome()

        # Mở trang
        driver.get(link)

        # Đợi 2 giây
        time.sleep(2)

        # Lấy tên hoạ sĩ
        try:
            name = driver.find_element(By.TAG_NAME, "h1").text
        except:
            name = ""

        # Lấy ngày sinh
        try:
            birth_element = driver.find_element(By.XPATH, "//th[text()='Born']/following-sibling::td")
            birth = birth_element.text
            birth = re.findall(r'[0-9]{1,2}+\s+[A-Za-z]+\s+[0-9]{4}', birth)[0]  # regex
        except:
            birth = ""

        # Lấy ngày mất
        try:
            death_element = driver.find_element(By.XPATH, "//th[text()='Died']/following-sibling::td")
            death = death_element.text
            death = re.findall(r'[0-9]{1,2}+\s+[A-Za-z]+\s+[0-9]{4}', death)[0]
        except:
            death = ""

        # Lấy quốc tịch
        try:
            nationality_element = driver.find_element(By.XPATH, "//th[text()='Nationality']/following-sibling::td")
            nationality = nationality_element.text
        except:
            nationality = ""

        # Tạo dictionary thông tin của hoạ sĩ
        painter = {'name': name, 'birth': birth, 'death': death, 'nationality': nationality}

        # Chuyển dictionary thành DataFrame
        painter_df = pd.DataFrame([painter])

        # Thêm thông tin vào DataFrame chính
        d = pd.concat([d, painter_df], ignore_index=True)

        # Đóng web driver
        driver.quit()
    except Exception as e:
        print(f"Error: {e}")

    ######################################################
    # IV. In thông tin
    print(d)

    # Xác định tên file
    file_name = 'Painters.xlsx'

    # Lưu Excel
    d.to_excel(file_name, index=False)
    print('DataFrame is written to Excel File successfully.')