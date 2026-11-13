"""输入：一个日志文件路径
输出：日志里出现过的所有机器标识（形如 PC-xxx），去重后按名字排序，一行一个"""

import re
import sys


def hosts_from_log(path):
    hosts = set()  # 用 set，天然去重
    bad = 0
    try:
        f = open(path, encoding="utf-8", errors="replace")
    except OSError as e:
        print(f"文件无法读取 {path}: {e}")
        return None

    with f:
        for line in f:
            bad += line.count("\ufffd")
            for h in re.findall(r"\bPC-\d+", line):
                hosts.add(h)
    if bad:
        print(f"注意：{bad} 处按替换字符处理，结果可能偏少", file=sys.stderr)
    return sorted(hosts)  # 排序后返回 list


if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        print("请传入正确的参数！用法：python hosts_from_log.py <日志文件>")
        sys.exit(2)
    hosts = hosts_from_log(path)
    if hosts is None:
        sys.exit(1)
    for host in hosts:
        print(host)
