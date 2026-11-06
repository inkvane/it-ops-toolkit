"""LC 349 两个数组的交集
[1,2,2,1] / [2,2]        → [2]
[4,9,5] / [9,4,9,8,4]    → [9,4] 或 [4,9]"""


def intersection(a1, a2):
    return list(set(a1) & set(a2))


if __name__ == "__main__":
    print(intersection([1, 2, 2, 1], [2, 2]))
    print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))
