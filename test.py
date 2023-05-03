'''
写一个python，要求将指定文件夹内符合关键字清单的任一关键字的文件全部复制到指定名称的文件夹
'''

import os
import shutil

# 指定关键字清单和目标文件夹
# keywords = ['餐', '饮','食','菜','香','烹','煮','味','饭','吃','口','营养','汤']#餐饮相关关键字
# keywords = ['专家','精','效率','时间','提高','提升','认','知','思','心','情','脑']
keywords = ['.azw','mobi',]
target_folder = '/Users/qmac/Downloads/f'

# 遍历指定文件夹中的所有文件
for root, dirs, files in os.walk('/Users/qmac/Downloads/fol2'):
    for file in files:
        # 判断文件名是否包含关键字
        if any(keyword in file for keyword in keywords):
            # 复制文件到目标文件夹
            shutil.move(os.path.join(root, file), os.path.join(target_folder, file))

