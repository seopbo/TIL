"""
    implementing selection sort
"""
from typing import List


def find_smallest(list_of_items: List[int]) -> int:
    """find index of smallest item from the list of indices

    Args:
        list_of_items: list of items

    Returns: index
    """
    smallest_idx = 0
    smallest_item = list_of_items[smallest_idx]

    for idx in range(1, len(list_of_items)):

        if list_of_items[idx] < smallest_item:
            smallest_item = list_of_items[idx]
            smallest_idx = idx

    return smallest_idx


def selection_sort(list_of_items: List[int]) -> List[int]:
    """sort the list of items

    Args:
        list_of_items: unsorted list of items

    Returns: sorted list of items
    """

    sorted_list = []

    while list_of_items:
        smallest_idx = find_smallest(list_of_items)
        sorted_list.append(list_of_items.pop(smallest_idx))

    return sorted_list


def test_find_smallest():
    """test find_smallest function"""
    assert find_smallest(range(10)) == 0


def test_selection_sort():
    """test selection_sort function"""
    assert selection_sort([1, 4, 3, 2]) == [1, 2, 3, 4]
