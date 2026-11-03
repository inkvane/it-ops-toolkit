"""脚本 2：扫目录，数每类文件有几个，多的排前面"""
import os
import sys

def count_by_ext(path):
    counts = {}
    try:
        names = os.listdir(path)
    except FileNotFoundError:
        print(f"路径不存在：{path}")
        return None
    for name in names:
        ext = os.path.splitext(name)[1]
        if ext == "":
            ext = "无扩展名"
        counts[ext] = counts.get(ext, 0) + 1

    return counts

def by_size(x):
    return x[1]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = "."
    counts = count_by_ext(path)
    if counts is None:
        sys.exit(1)

    pairs = sorted(counts.items(),key=by_size,reverse=True)
    for key, value in pairs:
        print(key,value)