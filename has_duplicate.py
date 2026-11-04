"""给你一个整数列表 nums。
如果任意一个数出现了至少两次，返回 True；全部互不相同，返回 False。

[1, 2, 3, 1]              → True
[1, 2, 3, 4]              → False
[1, 1, 1, 3, 3, 4, 3, 2]  → True"""


def has_duplicate(nums):

    # return len(nums) != len(set(nums))  一行版本
    seen = set()
    for num in nums:
        if num in seen:  # 见过吗
            return True
        seen.add(num)  # 没见过就放进去
    return False


if __name__ == "__main__":
    print(has_duplicate([1, 2, 3, 1]))  # True
    print(has_duplicate([1, 2, 3, 4]))  # False
    print(has_duplicate([1, 1, 1, 3, 3, 4, 3, 2]))  # True
