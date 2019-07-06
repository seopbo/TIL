"""
    implementing binary search
"""
from typing import List, Union


def binary_search(list_of_items: List[int], item: int) -> Union[int, None]:
    """Search index of target item in list of items

    Args:
        list_of_items : list of items
        item: target item

    Returns: index

    """

    low = 0
    high = len(list_of_items) - 1

    while low <= high:
        mid = (low + high) // 2
        if item == list_of_items[mid]:
            return mid
        if item > list_of_items[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return None


def test_binary_search():
    """test binary_search"""
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    assert binary_search([1, 2, 3, 4, 5], 10) is None
