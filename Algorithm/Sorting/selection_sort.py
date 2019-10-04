def selection_sort(seq):
    length = len(seq)

    for i in range(length - 1):
        min_idx = i
        for j in range(i + 1, length):
            if seq[min_idx] > seq[j]:
                min_idx = j
        seq[i], seq[min_idx] = seq[min_idx], seq[i]
    return seq


def test_selection_sort():
    seq = [11, 3, 28, 43, 9, 4]
    assert selection_sort(seq) == sorted(seq)


if __name__ == "__main__":
    test_selection_sort()
