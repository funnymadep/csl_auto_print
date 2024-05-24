from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import keyboard

# 读取配置文件
def read_config(file_path):
    config = {}
    current_section = None  # 记录当前节名
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('#'):  # 跳过空行和注释行
                continue
            if line.startswith('[') and line.endswith(']'):  # 开始一个新的节
                current_section = line[1:-1].strip()
            elif '=' in line:  # 处理键值对
                if current_section is None:
                    raise ValueError("Section header is missing.")
                key, value = line.split('=', 1)
                config.setdefault(current_section, {})[key.strip()] = value.strip()
    return config

# 读取配置
config = read_config('./config.txt')
print(config)
# 替换网址部分
url = "https://print.yingyutifen.cn/print/pc.html?aptmId=3229529"
if 'net' in config:
    url = config['net']

# 设置Firefox选项
firefox_options = Options()
firefox_options.headless = True
firefox_options.add_argument('-profile')
firefox_options.add_argument('/home/hql/snap/firefox/common/.mozilla/firefox')

# 启动浏览器并打开网页
driver = webdriver.Firefox(options=firefox_options)
driver.get(url)

try:
    profile = webdriver.FirefoxProfile()
    profile.set_preference("print.always_print_silent", True)
    # profile.set_preference("print.print_to_file", True)  # 启用打印到文件
    # profile.set_preference("print.print_to_filename", "/home/hql/git/my_git/csl_auto_click/1.pdf")  # 设置保存路径和文件名

    # 导航到网页并执行打印操作
    driver.execute_script("window.print();")
    # 等待一段时间，确保打印对话框已经出现
    # time.sleep(2)

    print("test")
    time.sleep(2)

    # 模拟按下回车键
    keyboard.press_and_release('enter')

    # 输入字符串
    input_string = "Your desired string"
    keyboard.write(input_string)

    # 再次按下回车键
    keyboard.press_and_release('enter')
    
except Exception as e:
        print("发生错误:", e)
finally:
    #关闭浏览器
    # driver.quit()
    print('over!\n')
