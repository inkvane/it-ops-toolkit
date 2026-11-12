#!/usr/bin/env python3
"""脚本 3：找出日志里出现最多的行。"""

import sys

from mylib import by_size


def top_lines(path, n=5):
    counts = {}
    skipped = 0
    try:
        f = open(path, encoding="utf-8")
    except FileNotFoundError:
        print(f"文件不存在：{path}")
        return None
    with f:
        for line in f:
            line = line.strip().split(maxsplit=2)
            if len(line) < 3:
                skipped += 1
                continue
            else:
                log = line[2]
            counts[log] = counts.get(log, 0) + 1

    pairs = sorted(counts.items(), key=by_size, reverse=True)
    total = sum(counts.values())
    return pairs[:n], skipped, total


if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = "."

    result = top_lines(path)
    if result is None:
        sys.exit(1)
    pairs, skipped, total = result

    for i, (key, value) in enumerate(pairs):
        print(f"{i + 1:>2}.{value:>5}次  {value / total * 100:>5.1f}%  {key:<40}")
    print(f"(跳过 {skipped} 行无效数据)")
