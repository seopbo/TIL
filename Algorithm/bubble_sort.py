import unittest
from typing import Sequence


def bubble_sort(sequence: Sequence, ascending: bool = True) -> Sequence:
    """Sorting sequence by bubble sort

    Args:
        sequence (Sequence): sequence of numeric or integer
        ascending (bool): sorting sequence by ascending order. Default: True

    Returns:
        sequence (Sequence): sorted sequence
    """
    num_loop = 0

    if ascending:
        while num_loop < len(sequence):
            for idx in range(len(sequence) - 1):
                if sequence[idx] >= sequence[idx + 1]:
                    sequence[idx], sequence[idx + 1] = sequence[idx + 1], sequence[idx]
            num_loop += 1
    else:
        while num_loop < len(sequence):
            for idx in range(len(sequence) - 1):
                if sequence[idx] < sequence[idx + 1]:
                    sequence[idx], sequence[idx + 1] = sequence[idx + 1], sequence[idx]
            num_loop += 1

    return sequence


class Test(unittest.TestCase):
    def test_function(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], bubble_sort([4, 6, 1, 3, 5, 2]))
        self.assertEqual([6, 5, 4, 3, 2, 1], bubble_sort([6, 4, 3, 1, 2, 5], ascending=False))
        self.assertEqual([1, 2, 3, 4, 5, 6], bubble_sort([6, 5, 4, 3, 2, 1]))


if __name__ == '__main__':
    unittest.main()
