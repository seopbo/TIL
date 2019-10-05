def quick_sort(seq):
    if len(seq) < 2:
        return seq

    ipivot = len(seq) // 2
    pivot = seq[ipivot]

    left = [x for i, x in enumerate(seq) if x <= pivot and i != ipivot]
    right = [x for i, x in enumerate(seq) if x > pivot and i != ipivot]
    return quick_sort(left) + [pivot] + quick_sort(right)