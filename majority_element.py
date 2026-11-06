"""LC 169 多数元素

[3,2,3]          → 3
[2,2,1,1,1,2,2]  → 2"""


def majority_element(nums):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    pairs = sorted(counts.items(), key=by_count, reverse=True)
    return pairs[0][0]  # 按"值"取最大，返回对应的键


def by_count(x):
    return x[1]


def majority(nums):
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate


if __name__ == "__main__":
    print(majority_element([3, 2, 3]))
    print(majority_element([2, 2, 1, 1, 1, 2, 2]))
    print(majority_element([1, 1, 2]))
    print(majority([3, 2, 3]))
    print(majority([2, 2, 1, 1, 1, 2, 2]))
    print(majority([1, 1, 2]))
