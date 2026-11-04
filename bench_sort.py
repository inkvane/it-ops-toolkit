# import time


# def sorted_version(s, t):
#     return sorted(s) == sorted(t)


# def dict_version(s, t):
#     if len(s) != len(t):
#         return False
#     s_counts = {}
#     t_counts = {}
#     for s_item in s:
#         s_counts[s_item] = s_counts.get(s_item, 0) + 1
#     for t_item in t:
#         t_counts[t_item] = t_counts.get(t_item, 0) + 1
#     return s_counts == t_counts


# s = "abcdefghij" * 50000  # 50 万字符
# t = "jihgfedcba" * 50000

# for fn in (sorted_version, dict_version):
#     t0 = time.perf_counter()
#     fn(s, t)
#     print(f"{fn.__name__:15s} {(time.perf_counter() - t0) * 1000:9.2f} ms")


import random
import time


def sorted_version(s, t):
    return sorted(s) == sorted(t)


def dict_version(s, t):
    c = {}
    for ch in s:
        c[ch] = c.get(ch, 0) + 1
    for ch in t:
        c[ch] = c.get(ch, 0) - 1
    return all(v == 0 for v in c.values())


random.seed(1)
s = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=500000))
t = "".join(random.sample(s, len(s)))
for fn in (sorted_version, dict_version):
    t0 = time.perf_counter()
    fn(s, t)
    print(f"{fn.__name__:15s} {(time.perf_counter() - t0) * 1000:9.2f} ms")
