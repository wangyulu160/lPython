import os
import shutil

# 删除文件到回收站/垃圾箱
def delete_to_recycle_bin(filepath):
    try:
        if os.name == 'nt':  # Windows
            # 使用winshell模块删除文件到回收站
            import winshell
            winshell.delete_file(filepath, no_confirm=True)
        elif os.name == 'posix':  # Mac
            # 使用send2trash模块删除文件到垃圾箱
            import send2trash
            send2trash.send2trash(filepath)
        else:
            # 不支持的操作系统
            raise NotImplementedError("Unsupported OS")
    except Exception as e:
        print(f"Error deleting file to recycle bin: {str(e)}")


# 恢复指定路径下所有删除的文件
def restore_deleted_files(dirpath):
    for root, dirs, files in os.walk(dirpath):
        # 扫描所有文件
        for file in files:
            filepath = os.path.join(root, file)
            if not os.path.exists(filepath):  # 如果文件不存在，则检查它是否删除.
                try:
                    # 尝试将文件从回收站/垃圾箱恢复
                    shutil.move(filepath + ".lnk", filepath)  # Windows
                    continue  # 下一个文件
                except FileNotFoundError:
                    pass  # 磁盘上没有 .lnk 文件或没有这样的链接
                print(f"{filepath} 未找到，可能已被永久删除")

        # 不再搜索子目录
        break


# 示例用法
if __name__ == "__main__":
    dirpath = "/Users/qmac/Downloads/fol"
    restore_deleted_files(dirpath)
