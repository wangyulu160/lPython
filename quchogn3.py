import os
import hashlib
from tqdm import tqdm  # 导入tqdm，用于显示进度条

folder_path = "/Volumes/U3/books&paper只允许拷入复制---------books"#你的路径
checksums = {}

total_files = 0
for root, dirs, files in os.walk(folder_path):
    total_files += len(files)

pbar = tqdm(total=total_files, unit="files")

for current_dir, dirs, files in os.walk(folder_path):
  for file in files:
    filepath = os.path.join(current_dir,file)
    try:
        with open(filepath, 'rb') as f:
            checksum = hashlib.md5(f.read()).hexdigest()
            if checksum not in checksums:
                checksums[checksum] = filepath
            else:
                os.remove(filepath)
    except FileNotFoundError:
        print("File '{0}' not found. Skipping...".format(filepath))
    pbar.update(1)

pbar.close()

print("Duplicates removed.")
