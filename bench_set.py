import time


def one_liner(nums):
    return len(nums) != len(set(nums))


def early_exit(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# nums = [1, 1] + list(range(500000))
nums = list(range(500000))
for fn in (one_liner, early_exit):
    t = time.perf_counter()
    fn(nums)
    print(f"{fn.__name__:12s} {(time.perf_counter() - t) * 1000:9.2f}ms")
