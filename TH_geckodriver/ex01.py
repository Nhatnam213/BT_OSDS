from  selenium import webdriver
from selenium.webdriver.chrome.service import  Service
import time

# Duong dan den file thuc thi geckodrive
gecko_path = "C:/project2/geckodriver.exe"

# Khoi tao doi tuong dich vu geckodriver
ser = Service(gecko_path)

# Tuy chon
options = webdriver.firefox.options.Options()
options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"
# Thiết lập firefox chỉ hiện thị giao diện
options.headless = False

# Khởi tạo driver
driver = webdriver.Firefox(options = options, service=ser)

# Tạo url
url = 'http://pythonscraping.com/pages/javascript/ajaxDemo.html'

# Truy cập
driver.get(url)

# In ra nội dung của trang web
print("Before: ================================\n")
print(driver.page_source)


# Tạm dừng khoảng 3 giây
time.sleep(3)

# In lai
print("\n\n\n\nAfter: ================================\n")
print(driver.page_source)


# Đóng browser
driver.quit()