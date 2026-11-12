"""列出当前目录所有的.py文件，按大小从大到小"""

import os

files = [n for n in os.listdir(".") if n.endswith(".py")]
files.sort(key=lambda n: os.path.getsize(n), reverse=True)
for n in files:
    print(f"{os.path.getsize(n):>8}  {n}")
