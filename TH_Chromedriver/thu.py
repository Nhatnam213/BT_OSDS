from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import re

# Tạo dataframe rỗng
all_links = []
d = pd.DataFrame({'name': [], 'birth': [], 'death': [], 'nationality': []})

# Khởi tạo webdriver bên ngoài vòng lặp
driver = webdriver.Chrome()

# Lấy tất cả các đường dẫn truy cập tới các trang họa sĩ theo ký tự từ A đến Z
for i in range(65, 91):
    url = "https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22" + chr(i) + "%22"

    driver.get(url)
    time.sleep(3)  # Chờ 3 giây để trang tải hoàn toàn

    try:
        # Lấy ra tất cả các thẻ ul
        ul_tags = driver.find_elements(By.TAG_NAME, "ul")

        # Kiểm tra nếu có ít nhất 21 thẻ ul
        if len(ul_tags) > 20:
            ul_painters = ul_tags[20]
            li_tags = ul_painters.find_elements(By.TAG_NAME, "li")

            # Tạo danh sách các đường dẫn tới từng trang họa sĩ
            links = [tag.find_element(By.TAG_NAME, "a").get_attribute("href") for tag in li_tags]
            all_links.extend(links)  # Thêm các liên kết vào danh sách tổng
        else:
            print(f"Không tìm thấy danh sách họa sĩ cho ký tự {chr(i)}")

    except Exception as e:
        print(f"Lỗi khi xử lý trang {chr(i)}: {e}")

# Duyệt qua tất cả các liên kết để lấy thông tin chi tiết của từng họa sĩ
for link in all_links:
    try:
        driver.get(link)
        time.sleep(2)

        # Lấy tên họa sĩ
        try:
            name = driver.find_element(By.TAG_NAME, "h1").text
        except:
            name = ""

        # Lấy ngày sinh
        try:
            birth_element = driver.find_element(By.XPATH, "//th[text()='Born']/following-sibling::td")
            birth = re.findall(r'[0-9]{1,2}+\s+[A-Za-z]+\s+[0-9]{4}', birth_element.text)[0]
        except:
            birth = ""

        # Lấy ngày mất
        try:
            death_element = driver.find_element(By.XPATH, "//th[text()='Died']/following-sibling::td")
            death = re.findall(r'[0-9]{1,2}+\s+[A-Za-z]+\s+[0-9]{4}', death_element.text)[0]
        except:
            death = ""

        # Lấy quốc tịch
        try:
            nationality_element = driver.find_element(By.XPATH, "//th[text()='Nationality']/following-sibling::td")
            nationality = nationality_element.text
        except:
            nationality = ""

        # Tạo dictionary thông tin họa sĩ
        painter = {'name': name, 'birth': birth, 'death': death, 'nationality': nationality}

        # Thêm thông tin vào dataframe
        d = pd.concat([d, pd.DataFrame([painter])], ignore_index=True)

    except Exception as e:
        print(f"Lỗi khi truy cập trang {link}: {e}")

# In thông tin ra file Excel
driver.quit()  # Đóng trình duyệt khi hoàn tất

# Đặt tên file Excel
file_name = "Painters.xlsx"
d.to_excel(file_name, index=False)
print('DataFrame đã được lưu thành công vào file Excel.')
driver.quit()