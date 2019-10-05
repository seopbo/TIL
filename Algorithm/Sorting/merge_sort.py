def merge_sort(seq):
    if len(seq) < 2:
        return seq

    mid = len(seq) // 2
    left, right = seq[:mid], seq[mid:]

    if len(left) > 1:
        left = merge_sort(left)
    if len(right) > 1:
        right = merge_sort(right)

    res = []
    while left and right:
        if left[-1] >= right[-1]:
            res.append(left.pop())
        else:
            res.append(right.pop())
    res.reverse()

    return (left or right) + res


def test_merge_sort():
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    assert merge_sort(seq) == sorted(seq)


if __name__ == "__main__":
    test_merge_sort()
