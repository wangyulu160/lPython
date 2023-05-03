# 写一个python，要求将指定文件夹内包含文件夹子文件夹符合关键字清单的任一关键字的文件全部复制到指定名称的文件夹

import os
import shutil


def move_files_with_keywords(src_folder, dst_folder, keywords_list):
    """
    将符合给定关键字的文件从源文件夹中移动到目标文件夹中。

    Args:
        src_folder (str): 源文件夹路径。
        dst_folder (str): 目标文件夹路径。
        keywords_list (list): 包含要匹配的关键字的列表。
    """
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            # 检查是否有匹配的关键字
            if any(keyword in file for keyword in keywords_list):
                src_path = os.path.join(root, file)
                dst_path = os.path.join(dst_folder, file)

                # 移动文件
                shutil.move(src_path, dst_path)


# 示例用法
src_folder = "/Users/qmac/Desktop/a"
dst_folder = "/Users/qmac/Downloads/f"
keywords_list = [".azw"]

move_files_with_keywords(src_folder, dst_folder, keywords_list)
