from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service  
from selenium.webdriver.common.by import By
import time
import os
import datetime

# 创建一个 Chrome WebDriver 实例
options = Options()
# options.add_argument("--headless")  # 启用无头模式
def read_config(file_path):
    # 读取config.txt文件并解析内容
    with open(file_path, 'r') as file:
        lines = file.readlines()

    config = {}
    for line in lines:
        line = line.strip()  # 去除首尾空白字符

        # 如果是空行、以[config]开头的行、以#开头的注释行或者不包含等号的行，则跳过
        if not line or line.startswith("[config]") or line.startswith("#") or '=' not in line:
            continue

        key, value = line.split('=', 1)  # 限制分割次数为1，防止多个等号导致的错误
        config[key.strip()] = value.strip()

    return config


def file_rename(config , Type):
    current_date = datetime.datetime.now().strftime("%Y%m%d")
# 获取name参数
    name = config.get('name', '')

# 查找当前目录练习开头的.pdf文件
    for file_name in os.listdir('.'):
        if file_name.startswith('练习') and file_name.endswith('.pdf'):
        # 构造新的文件名
            new_file_name = f"{current_date} {name}{Type}.pdf"
        # 重命名文件
            os.rename(os.path.join('.', file_name), os.path.join('.', new_file_name))
            print(f"文件 {file_name} 已重命名为 {new_file_name}")
            break  # 如果只想处理一个文件，可以加上break来提前结束循环

config = read_config('./config.txt')
# 获取参数
name = config.get('name', '')
Type = config.get('type', '')
net = config.get('net', '')

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
driver.get(net)

# 等待页面加载
time.sleep(5)  # 根据实际情况调整等待时间

# 定义包含查找关键字的列表
search_texts = ["打印中英文", "打印中文", "打印英文", "打印音标"]
texts = ["中英", "中文", "英文", "音标"]

for text, Type in zip(search_texts, texts):
    try:
        # 动态构建XPath表达式并查找元素
        element = driver.find_element(By.XPATH, f"//button[contains(text(), '{text}')]")
        element.click()
        # 在这里可以对找到的元素执行操作，比如点击
        driver.execute_script("window.print();")
        file_rename(config, Type)

    except Exception as e:
        print(f"未找到元素：'{text}', 错误信息：{e}")

driver.execute_script("window.print();")  # 执行 window.print() 函数

driver.quit()
