import os

def search_files(path, keyword):
    # 遍历当前目录及其子目录
    for root, dirs, files in os.walk(path):
        # 遍历文件
        for name in files:
            # 如果文件包含关键词，则输出文件路径
            if keyword in name:
                print(os.path.join(root, name))

if __name__ == '__main__':
    # 输入要扫描的目录和关键词
    path = input("请输入要扫描的目录:")
    keyword = input("请输入关键字:")

    # 进行扫描并输出结果
    search_files(path, keyword)