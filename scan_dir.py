"""脚本 1: 扫描一个目录，列出最大的5个文件。"""
import os
import sys

def scan(path):
    result=[]
    try:
        names = os.listdir(path)
    except FileNotFoundError:
        print(f"路径不存在：{path}")
        return None
    for name in names:
        full_path = os.path.join(path,name)
        result.append((name, os.path.getsize(full_path)))
    return result

def human_size(n):
    if n < 1024:
        return f"{n} B"
    elif n < 1024 * 1024:
        return f"{n / 1024:.1f} KB"
    elif n < 1024 ** 3:
        return f"{n / 1024 / 1024:.1f} MB"
    else:
        return f"{n / 1024 / 1024 / 1024:.1f} GB"



def by_size(x):
    return x[1]



if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = "."
    items = scan(path)
    if items is None:
        sys.exit(1)
    items.sort(key=by_size, reverse=True)
    for name, size in items[:5]:
        print(f"{human_size(size):>9} \t{name}")