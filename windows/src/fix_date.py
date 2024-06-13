import os
import glob

# 读取config.txt文件中的fixdate值
with open("config.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        if 'fixdate=' in line:
            fixdate = line.split('=')[1].strip()

# 查找当前文件夹中的所有.pdf文件
pdf_files = glob.glob('*.pdf')

# 遍历所有.pdf文件
for file in pdf_files:
    # 提取文件名中的日期部分
    date = file.split(' ')[0]
    # 如果文件名中的日期部分和fixdate值不同，则修改文件名
    if date != fixdate:
        new_file = file.replace(date, fixdate)
        os.rename(file, new_file)
