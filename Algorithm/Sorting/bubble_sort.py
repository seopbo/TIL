def bubble_sort(seq):
    length = len(seq) - 1
    for num in range(length, 0, -1):
        for idx in range(num):
            if seq[idx] > seq[idx + 1]:
                seq[idx], seq[idx + 1] = seq[idx + 1], seq[idx]
    return seq


def test_bubble_sort():
    seq = [4, 5, 2, 1, 6, 2, 7, 10, 13, 8]
    assert bubble_sort(seq) == sorted(seq)


if __name__ == "__main__":
    test_bubble_sort()
