"""
    implementing quick sort
"""
from typing import List


def quick_sort(list_of_items: List[int]) -> List[int]:

    if len(list_of_items) < 2:
        return list_of_items
    else:
        pivot = list_of_items[0]
        lower = [item for item in list_of_items[1:] if item <= pivot]
        upper = [item for item in list_of_items[1:] if item > pivot]
        return quick_sort(lower) + [pivot] + quick_sort(upper)


def test_quick_sort():
    """test quick_sort function"""
    assert quick_sort([1, 4, 3, 2]) == [1, 2, 3, 4]
