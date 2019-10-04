from collections import defaultdict


def count_sort(seq):
    b, c = [], defaultdict(list)
    for x in seq:
        c[x].append(x)
    for k in range(min(c), max(c) + 1):
        b.extend(c[k])
    return b


def test_count_sort():
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2, 5, 4, 1, 5, 3]
    assert count_sort(seq) == sorted(seq)


if __name__ == "__main__":
    test_count_sort()
