def quick_sort(seq):
    if len(seq) < 2:
        return seq

    ipivot = len(seq) // 2
    pivot = seq[ipivot]

    left = [x for i, x in enumerate(seq) if x <= pivot and i != ipivot]
    right = [x for i, x in enumerate(seq) if x > pivot and i != ipivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


def test_quick_sort():
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2]
    assert quick_sort(seq) == sorted(seq)


if __name__ == "__main__":
    test_quick_sort()
