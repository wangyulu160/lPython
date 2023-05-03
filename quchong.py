import os
import hashlib

# 设置要查找的文件夹路径
folder_path = "/Volumes/U3/books&paper只允许拷入复制---------books"

# 用一个字典来记录每个文件的哈希值
file_hashes = {}

# 定义一个函数来递归地获取所有文件
def get_files_from_folder(folder):
    files = []
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        if os.path.isdir(file_path):
            # 如果是子文件夹，递归获取子文件夹内的文件
            files.extend(get_files_from_folder(file_path))
        else:
            # 如果是文件，计算该文件的哈希值并记录到字典中
            with open(file_path, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
            if file_hash in file_hashes:
                # 如果发现了重复的哈希值，则删除该文件
                print("Delete:", file_path)
                os.remove(file_path)
            else:
                file_hashes[file_hash] = file_path
    return files

# 执行程序
get_files_from_folder(folder_path)
