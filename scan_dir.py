"""脚本 1: 扫描一个目录，列出最大的5个文件。"""

import os
import sys

from mylib import by_size, human_size


def scan(path):
    result = []
    try:
        names = os.listdir(path)
    except FileNotFoundError:
        print(f"路径不存在：{path}")
        return None
    for name in names:
        full_path = os.path.join(path, name)
        result.append((name, os.path.getsize(full_path)))
    return result


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
