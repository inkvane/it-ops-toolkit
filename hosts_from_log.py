"""输入：一个日志文件路径
输出：日志里出现过的所有机器标识（形如 PC-xxx），去重后按名字排序，一行一个"""

import sys


def hosts_from_log(path):
    hosts = set()  # 用 set，天然去重
    try:
        f = open(path, encoding="utf-8")
    except FileNotFoundError:
        print(f"文件不存在：{path}")
        return None

    with f:
        for line in f:
            for word in line.split():  # ← 每个词看一眼
                clean = word.strip("()[],:;.")
                if clean.startswith("PC-"):
                    hosts.add(clean)

    return sorted(hosts)  # 排序后返回 list


if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = "."
    hosts = hosts_from_log(path)
    if hosts is None:
        sys.exit(1)
    for host in hosts:
        print(host)
