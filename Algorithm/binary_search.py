from typing import List


def binary_search(list_of_items: List[int], item: int):
    low = 0
    high = len(list_of_items) - 1

    while low <= high:
        mid = (low + high) // 2
        if item == list_of_items[mid]:
            return mid
        elif item > list_of_items[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return None
