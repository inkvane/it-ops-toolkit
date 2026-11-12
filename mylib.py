"""公共小工具"""


def by_size(x):
    return x[1]


def human_size(n):
    if n < 1024:
        return f"{n} B"
    elif n < 1024 * 1024:
        return f"{n / 1024:.1f} KB"
    elif n < 1024**3:
        return f"{n / 1024 / 1024:.1f} MB"
    else:
        return f"{n / 1024 / 1024 / 1024:.1f} GB"
