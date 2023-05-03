import os
import shutil

# 设置要查找的文件夹路径和关键字
folder_path = "/Volumes/U3/books&paper只允许拷入复制---------books"
keyword = "笑的科学解"

# 定义一个函数来递归地获取所有文件
def get_files_from_folder(folder):
    files = []
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        if os.path.isdir(file_path):
            # 如果是子文件夹，递归获取子文件夹内的文件
            files.extend(get_files_from_folder(file_path))
        else:
            # 如果是文件，检查是否包含关键字
            if keyword in file_path:
                # 如果包含关键字，将该文件复制到目标文件夹中
                # /Volumes/U3/books&paper只允许拷入复制---------books/【编程语言】大合集
                dst_folder = "/Users/qmac/Downloads/文件"  # 替换为你的目标文件夹路径/Users/qmac/Downloads/fol
                shutil.copy(file_path, dst_folder)
    return files

# 执行程序
get_files_from_folder(folder_path)
