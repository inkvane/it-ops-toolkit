""" "给一个整数列表 nums 和一个整数 target，
找出列表里 两个数，加起来等于 target，返回它们的下标。"""


# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for n in range(i + 1, len(nums)):
#             if nums[i] + nums[n] == target:
#                 return [i, n]


def two_sum(nums, target):
    seen = {}  # 数 → 下标
    for i, num in enumerate(nums):  # ← 新东西，往下看
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # 期望 [0, 1]
    print(two_sum([3, 2, 4], 6))  # 期望 [1, 2]
    print(two_sum([3, 3], 6))  # 期望 [0, 1]
