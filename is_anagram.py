"""给两个字符串 s 和 t，判断 t 是不是 s 的字母异位词
（字母种类和数量完全相同，只是排列不同）

"anagram" / "nagaram"  → True
"rat" / "car"          → False"""


def sorted_version(s, t):
    return sorted(s) == sorted(t)


def dict_version(s, t):
    if len(s) != len(t):
        return False
    s_counts = {}
    t_counts = {}
    for s_item in s:
        s_counts[s_item] = s_counts.get(s_item, 0) + 1
    for t_item in t:
        t_counts[t_item] = t_counts.get(t_item, 0) + 1
    return s_counts == t_counts


if __name__ == "__main__":
    print(sorted_version("anagram", "nagaram"))  # True
    print(sorted_version("rat", "car"))  # False
    print(dict_version("anagram", "nagaram"))  # True
    print(dict_version("rat", "car"))  # False
