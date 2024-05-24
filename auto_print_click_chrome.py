from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service  
import time

# 创建一个 Chrome WebDriver 实例
options = Options()
# options.add_argument("--headless")  # 启用无头模式

# 设置 Chrome 选项
prefs = {
    "download.prompt_for_download": False,
    "savefile.default_directory": "/home/hql/git/my_git/csl_auto_print",  # 请替换为你的下载目录
    "download.directory_upgrade": True,
    "download.extensions_to_open": "pdf",
}
options.add_experimental_option("prefs", prefs)

# 使用 --kiosk-printing 来启用 "silent printing"
options.add_argument("--kiosk-printing")

# 请确保 chrome_driver_path 指向正确的 ChromeDriver 位置
chrome_driver_path = "./chromedriver"  # 请替换为你的 ChromeDriver 路径
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# 打开指定的 URL
url = "https://print.yingyutifen.cn/print/pc.html?aptmId=3229529"  # 请替换为你的 URL
driver.get(url)

# 等待页面加载
time.sleep(5)  # 根据实际情况调整等待时间

driver.execute_script("window.print();")  # 执行 window.print() 函数

driver.quit()
