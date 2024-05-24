from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service  
import time

# 创建一个 Chrome WebDriver 实例
options = Options()
# options.add_argument("--headless")  # 启用无头模式

# 请确保 chrome_driver_path 指向正确的 ChromeDriver 位置
chrome_driver_path = "/home/hql/git/my_git/csl_auto_print/chromedriver"  # 请替换为你的 ChromeDriver 路径
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# 打开指定的 URL
url = "https://print.yingyutifen.cn/print/pc.html?aptmId=3229529"  # 请替换为你的 URL
driver.get(url)

# 等待页面加载
time.sleep(5)  # 根据实际情况调整等待时间

# buttons = ["中英文", "英文", "中文", "音标"]  # 请根据实际的按钮文本进行调整
# for button_text in buttons:
#     button = driver.find_element_by_link_text(button_text)
#     button.click()
#     time.sleep(2)  # 等待页面响应
driver.execute_script("window.print();")  # 执行 window.print() 函数
#     time.sleep(2)  # 等待打印对话框打开


# 关闭 WebDriver 实例
# driver.quit()
