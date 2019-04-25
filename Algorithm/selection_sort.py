import unittest
from typing import Sequence


def selection_sort(sequence: Sequence, ascending: bool = True) -> Sequence:
    """Sorting sequence selection sort

    Args:
        sequence (Sequence): sequence of numeric or integer
        ascending (bool): sorting sequence by ascending order. Default: True

    Returns:
        sequence (Sequence): sorted sequence
    """
    if ascending:
        for i in range(len(sequence) - 1):
            min_idx = i

            for j in range(i+1, len(sequence)):
                if sequence[min_idx] >= sequence[j]:
                    min_idx = j
            else:
                sequence[i], sequence[min_idx] = sequence[min_idx], sequence[i]
    else:
        for i in range(len(sequence) - 1):
            max_idx = i

            for j in range(i+1, len(sequence)):
                if sequence[max_idx] < sequence[j]:
                    max_idx = j
            else:
                sequence[i], sequence[max_idx] = sequence[max_idx], sequence[i]

    return sequence


class Test(unittest.TestCase):
    def test_function(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], selection_sort([4, 6, 1, 3, 5, 2]))
        self.assertEqual([6, 5, 4, 3, 2, 1], selection_sort([6, 4, 3, 1, 2, 5], ascending=False))
        self.assertEqual([1, 2, 3, 4, 5, 6], selection_sort([6, 5, 4, 3, 2, 1]))


if __name__ == '__main__':
    unittest.main()
