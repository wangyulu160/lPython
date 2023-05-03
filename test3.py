# 写一个python代码，命令行显示磁盘速率、cpu占用、内存占用，每秒刷新
# import psutil
# import time
#
# while True:
#     # 获取CPU占用率
#     cpu_usage = psutil.cpu_percent()
#
#     # 获取内存占用率
#     memory_stats = psutil.virtual_memory()
#     memory_usage = memory_stats.percent
#
#     # 获取磁盘IO信息并计算读写速度
#     disk_stats = psutil.disk_io_counters()
#     read_speed = disk_stats.read_bytes / 1024 / 1024  # 读取速度，单位为MB/s
#     write_speed = disk_stats.write_bytes / 1024 / 1024  # 写入速度，单位为MB/s
#
#     print(f"CPU Usage: {cpu_usage:.1f}%\tMemory Usage: {memory_usage:.1f}%\tDisk Read Speed: {read_speed:.2f}MB/s\tDisk Write Speed: {write_speed:.2f}MB/s")
#
#     time.sleep(1)

# 写一个python代码，命令行显示磁盘速率、cpu占用、内存占用，每秒刷新, 只一行显示
import psutil
import time

while True:
    # 获取CPU占用率
    cpu_usage = psutil.cpu_percent()

    # 获取内存占用率
    memory_stats = psutil.virtual_memory()
    memory_usage = memory_stats.percent

    # 获取磁盘IO信息并计算读写速度
    disk_stats = psutil.disk_io_counters()
    read_speed = disk_stats.read_bytes / 1024 / 1024  # 读取速度，单位为MB/s
    write_speed = disk_stats.write_bytes / 1024 / 1024  # 写入速度，单位为MB/s

    print(f"\rCPU Usage: {cpu_usage:.1f}%\tMemory Usage: {memory_usage:.1f}%\tDisk Read Speed: {read_speed:.2f}MB/s\tDisk Write Speed: {write_speed:.2f}MB/s", end="")

    time.sleep(1)

